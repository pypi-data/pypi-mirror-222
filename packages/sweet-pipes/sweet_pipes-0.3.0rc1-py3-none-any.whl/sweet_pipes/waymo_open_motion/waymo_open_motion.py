import asyncio
import io
import logging
import os
import sys
from concurrent.futures import Future, ThreadPoolExecutor
from tempfile import NamedTemporaryFile
from typing import Generator, IO, List, Literal, Optional, Tuple, TypeVar
from urllib.parse import urlparse

from gcloud.aio.storage import Storage
from torchdata.datapipes.iter import IterDataPipe
from torchdata.datapipes.utils import StreamWrapper
from tqdm import tqdm

T = TypeVar("T")
URL_TEMPLATE = (
    "gs://waymo_open_dataset_motion_v_1_2_0/uncompressed/tf_example/"
    "{name}/{name}_tfexample.tfrecord-{idx:05d}-of-01000"
)
SPLIT_TO_DATASET_NAME = {
    "train": "training",
    "validation": "validation",
    "test": "testing",
}


async def async_download_to_file(
    uri: str,
    fp: IO,
    timeout: int = sys.maxsize,
    chunk_size: int = 2**23,  # 8 MiB
    verbose: bool = False,
) -> None:
    _uri = urlparse(uri)

    total_bytes = 0
    total_mib = 0
    name = os.path.basename(uri)
    progbar = tqdm(
        desc=f"Download {name}",
        unit="MiB",
        unit_scale=True,
        disable=not verbose,
    )

    async with Storage() as storage:
        data: bytes = b""
        stream = await storage.download_stream(
            _uri.netloc, _uri.path[1:], timeout=timeout
        )

        while True:
            data = await stream.read(chunk_size)
            fp.write(data)

            total_bytes += len(data)
            mib = total_bytes // 2**20
            progbar.update(mib - total_mib)
            total_mib = max(total_mib, mib)

            if not data:
                break

    fp.seek(0)
    progbar.close()


class TFRecordOpener(IterDataPipe):
    def __init__(
        self,
        dp: IterDataPipe[Tuple[str, io.BufferedIOBase]],
        cache_dir: Optional[str] = None,
        prefetch_factor: int = 1,
        verbose: bool = False,
    ) -> None:
        super().__init__()
        self.dp = dp
        self.cache_dir = cache_dir
        self.prefetch_factor = prefetch_factor
        self.verbose = verbose

    def __iter__(self) -> Generator[Tuple[str, StreamWrapper], None, None]:
        pool = ThreadPoolExecutor(max_workers=self.prefetch_factor)
        iterator = iter(self.dp)

        cache: List[Tuple[str, IO, Future]] = []
        while True:
            while len(cache) < self.prefetch_factor:
                try:
                    url = next(iterator)
                except StopIteration:
                    continue

                fp: IO = NamedTemporaryFile(mode="wb+")
                path = fp.name
                future = pool.submit(
                    lambda: asyncio.run(
                        async_download_to_file(url, fp, verbose=self.verbose)
                    )
                )
                cache.append((path, fp, future))

            if not cache:
                break

            path, fp, future = cache.pop(0)
            _ = future.result()
            # Wrap the open (possibly temporary) file in 'StreamWrapper', so that
            # TorchData automatically cleans it up when it goes out of context.
            yield path, StreamWrapper(fp)


class OverflowErrorHandler(IterDataPipe[T]):
    def __init__(self, dp: IterDataPipe[T]) -> None:
        super().__init__()
        self.dp = dp

    def __iter__(self) -> Generator[T, None, None]:
        iterator = iter(self.dp)
        while True:
            try:
                yield next(iterator)
            except OverflowError:
                logging.error("OverflowError encountered, skipping sample")
            except StopIteration:
                break


def waymo_open_motion_datapipe(
    split: Literal["train", "validation", "test"],
    cache_dir: Optional[str] = None,
    shuffle: bool = False,
    shuffle_buffer_size: int = 128,
    prefetch_factor: int = 1,
    verbose: bool = False,
) -> IterDataPipe:
    name = SPLIT_TO_DATASET_NAME[split]
    tfrecord_urls = [URL_TEMPLATE.format(name=name, idx=idx) for idx in range(1000)]

    dp = IterableWrapper(tfrecord_urls)
    if shuffle:
        # Shuffle the order of the TFRecord files.  This costs us nothing, since we
        # already have all of the URLs in memory.  We will shuffle again later, once
        # the samples have been loaded, using a small buffer for memory constraints.
        dp.shuffle()

    dp = TFRecordOpener(
        dp,
        cache_dir=cache_dir,
        prefetch_factor=prefetch_factor,
        verbose=verbose,
    )
    dp = dp.load_from_tfrecord()
    dp = OverflowErrorHandler(dp)
    if shuffle:
        # Shuffle the loaded samples.  We use a small buffer to (hopefully) avoid
        # out-of-memory errors.  The entire dataset is
        dp = dp.shuffle(buffer_size=shuffle_buffer_size)

    return dp


if __name__ == "__main__":
    from torchdata.datapipes.iter import IterableWrapper
    from tqdm import tqdm

    dp = waymo_open_motion_datapipe(split="train", verbose=True)
    for x in tqdm(dp):
        pass
