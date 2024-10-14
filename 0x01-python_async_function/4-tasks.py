#!/usr/bin/env python3
"""Asynchronously waits for `n` random delays
and returns a list of these delays in
ascending order.
"""


import heapq
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """
    Asynchronously waits for `n` random delays
    and returns a list of these delays in
    ascending order.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay value (in seconds) for each wait.

    Returns:
        list[float]: A list of `n` delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        heapq.heappush(delays, delay)
    return [heapq.heappop(delays) for _ in range(len(delays))]
