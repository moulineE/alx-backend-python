#!/usr/bin/env python3
"""
asynchronous coroutine wait_random that takes an integer max_delay and
wait for a random time between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine wait_random
    Args:
        max_delay (int, optional): maximum delay. Defaults to 10.
    Returns:
        float: random delay
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
