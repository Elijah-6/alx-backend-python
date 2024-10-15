#!/usr/bin/env python3
"""This module Measures the average
runtime of executing wait_n function.
"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average runtime of executing wait_n function.

    Args:
        n (int): The number of times to execute wait_n.
        max_delay (int): The maximum delay for each wait_n call.

    Returns:
        float: The average runtime per execution of wait_n.
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
