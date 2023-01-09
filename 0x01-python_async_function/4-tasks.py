#!/usr/bin/env python3
"""
    4-tasks mod
"""
import random
from typing import List
from asyncio import sleep


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        waits n times with the max delay and returns a list of sorted
        wait times

        Args:
            n: number of times to wait
            max_delay: maximum time to wait
    """
    rand_list = []
    for num in range(n):
        delay = random.uniform(0, max_delay)
        rand_list.append(delay)
        await sleep(delay)
    return sorted(rand_list)
