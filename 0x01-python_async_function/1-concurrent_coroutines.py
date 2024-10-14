#!/usr/bin/env python3

import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    delays = []
    for _ in range(n):
        delay = await wait_random(max_delay)
        heapq.heappush(delays, delay)
    return [heapq.heappop(delays) for _ in range(len(delays))]
