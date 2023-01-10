#!/usr/bin/python3
"""
    0-async_generator mod
"""
import random
from asyncio import sleep
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
        this is an async generator that yields a random value
        from 0-10
    """
    for i in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
