#!/usr/bin/env python3
"""
    3-tasks mod
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        returns a task to be waited for

        Args:
            max_delay: maximum time to be delayed
    """
    # creates a task to be executed
    return asyncio.create_task(wait_random(max_delay))
