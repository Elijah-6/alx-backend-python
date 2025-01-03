#!/usr/bin/env python3
""" Asynchronous function that waits
for a random delay between 0 and max_delay seconds.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that waits for a random delay between 0 and max_delay
    seconds.

    Args:
        max_delay (float): The maximum delay
        in seconds. Default is 10.00 seconds.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
