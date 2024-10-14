#!/usr/bin/env python3
"""  Asynchronously waits for `n` random
delays and returns them in ascending order.
"""
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronously waits for `n` random delays and returns them in ascending
    order.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value in seconds.

    Returns:
        list[float]: A list of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        heapq.heappush(delays, delay)
    return [heapq.heappop(delays) for _ in range(len(delays))]
