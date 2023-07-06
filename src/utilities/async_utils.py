import asyncio
from asyncio import AbstractEventLoop
from concurrent.futures import ThreadPoolExecutor
from typing import (
    Coroutine,
    Callable,
)


# Create a thread pool executor
EXECUTOR = ThreadPoolExecutor()


async def async_wrapper(
    sync_function: Callable, *args: tuple, **kwargs: dict
) -> Coroutine:
    """A wrapper function to run any synchronous function asynchronously."""
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(EXECUTOR, sync_function, *args, **kwargs)


def async_runner(*coroutines: tuple[Coroutine]) -> list:
    """Asyncronously runs all given coroutines. Returns a list of
    results in order of the given coroutines."""
    # Setup async event loop.
    loop: AbstractEventLoop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Run async functions
    results: list = asyncio.run(_async_runner(*coroutines))
    loop.close()
    return results


async def _async_runner(*coroutines: tuple[Coroutine]) -> list:
    """Helper function to await all coroutines."""
    return await asyncio.gather(*coroutines)
