#!/usr/bin/env python3
"""
Measure the runtime of async_comprehension
"""
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will measure the total runtime of async_comprehension
    and return it.
    Returns:
        float: the total runtime
    """
    start = asyncio.get_event_loop().time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = asyncio.get_event_loop().time()
    return end - start
