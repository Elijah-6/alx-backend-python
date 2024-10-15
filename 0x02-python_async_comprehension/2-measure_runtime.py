#!/usr/bin/env python3
'''Import async_comprehension from the previous file and write a measure_runtime coroutine
that will execute async_comprehension four times in parallel
using asyncio.gather.

measure_runtime should measure
the total runtime and return it.
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''
    Measure the total runtime of async_comprehension four times in parallel using asyncio.gather.

    Returns:
        float: The total runtime in seconds.
    '''
    tasks = [async_comprehension() for _ in range(4)]
    start_time = time.perf_counter()
    await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time
