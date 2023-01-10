#!/usr/bin/env python3
"""
    0-async_generator mod
"""
import random
from asyncio import sleep
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
        this is an async generator that yields a random value
        from 0-10
    """
    for i in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
