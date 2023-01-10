#!/usr/bin/env python3
"""
    2-measure_runtime mod
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        coroutine that will execute async_comprehension four times in parallel
        using asyncio.gatherand measure the total runtime and return it.
    """
    start = time.perf_counter()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end = time.perf_counter()

    return (end - start)
