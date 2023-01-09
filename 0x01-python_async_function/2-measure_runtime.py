#!/usr/bin/env python3
"""
    2-measure_time mod
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Measures and returns the appropriate time it takes an async function
        to run

        Args:
            n: number of times to wait
            max_delay: maximum time to wait
    """
    # gets the appropriate time before
    start_time = time.perf_counter()

    # to run the async function we put in an event loop as below
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()  # time after function runs
    return (end_time - start_time) / n
