#!/usr/bin/env python3
"""
    1-concurrent_coroutines
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        waits n times with the max delay and returns a list of sorted
        wait times

        Args:
            n: number of times to wait
            max_delay: maximum time to wait
    """
    return sorted([await wait_random(max_delay) for num in range(n)])
