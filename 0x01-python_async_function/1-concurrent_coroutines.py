#!/usr/bin/env python3
"""
async routine called wait_n that takes in 2 int takes in 2 int arguments
n and max_delay and returns the list of all the delays (float values)
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): number of iterations
        max_delay (int): max delay of each iteration
    Returns:
        list of all the delays (float)
    """
    delays = []
    for i in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
