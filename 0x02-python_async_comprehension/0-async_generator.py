#!/usr/bin/env python3
"""Write a coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times,
each time asynchronously wait 1 second,
then yield a random number between 0 and 10. Use the random module. 
"""
import random
import asyncio

async def async_generator():
    """
    An asynchronous generator that yields random numbers.

    This coroutine will asynchronously generate 10 random numbers between 0 and 10,
    yielding one number every second.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
