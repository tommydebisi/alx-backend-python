#!/usr/bin/env python3
"""
    0-basic_async_syntax mod
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
        This function waits for a random delay between 0 and max_delay
        seconds and eventually returns it.

        Args:
            max_delay: maximum delay to wait
    """
    # get random number between 0 and range of max_delay
    delay_num = random.uniform(0, float(max_delay))
    await asyncio.sleep(delay_num)
    return delay_num
