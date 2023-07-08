import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor
from typing import Any
import time


async def _async_helper(*coroutines) -> list[Any]:
    return await asyncio.gather(*coroutines)


def async_helper(*coroutines) -> list[Any]:
    # Setup async event loop.
    loop: AbstractEventLoop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Run async functions
    results: list[Any] = asyncio.run(_async_helper(*coroutines))
    loop.close()
    return results


async def task(seconds: int) -> None:
    print(f"Got task, waiting {seconds}s.")
    await asyncio.sleep(seconds)
    print(f"Finished task in {seconds}s.")
    return seconds


# Create a thread pool executor
executor = ThreadPoolExecutor()


async def async_wrapper(sync_function, *args, **kwargs):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, sync_function, *args, **kwargs)


async def async_func(seconds):
    sync_func(seconds)


def sync_func(seconds):
    print(f"Got task, waiting {seconds}s.")
    count = 0
    time.sleep(seconds)
    print(f"Finished task in {seconds}s.")
    return seconds


f0 = async_wrapper(sync_func, 3)
f1 = async_wrapper(sync_func, 2)
f2 = async_wrapper(sync_func, 1)

end = async_helper(f0, f1, f2)
print(end)
