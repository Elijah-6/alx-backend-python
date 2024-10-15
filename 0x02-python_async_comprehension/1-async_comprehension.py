#!/usr/bin/env python3
"""Import async_generator from the previous task
and then write a coroutine called async_comprehension
that takes no arguments.

The coroutine will collect 10 random numbers
using an async comprehensing over async_generator,
then return the 10 random numbers.
"""

async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> list[float]:
    """
    An asynchronous comprehension that collects 10 random numbers.

    This coroutine will collect 10 random numbers using an async comprehension
    over the async_generator, returning the collected numbers.

    Returns:
        list[float]: A list of 10 random numbers between 0 and 10.
    """
    return [num async for num in async_generator()]
