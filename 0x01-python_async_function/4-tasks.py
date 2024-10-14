#!/usr/bin/env python3


import heapq
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    delays = []
    for _ in range(n):
        delay = await task_wait_random(max_delay)
        heapq.heappush(delays, delay)
    return [heapq.heappop(delays) for _ in range(len(delays))]
