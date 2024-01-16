#!/usr/bin/env python3
"""
function task_wait_n that is nearly identical to wait_n
except task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Args:
        n (int): number of times wait_random will be called
        max_delay (int): max wait time
    Returns: list of all the delays (float)
    """
    delays = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    delays = list(asyncio.as_completed(delays))
    delays = [await delay for delay in delays]
    return delays
