#!/usr/bin/env python3
"""
a measure_time function with integers n and max_delay as arguments that
measures the total execution time for wait_n(n, max_delay), and
returns total_time / n
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Args:
        n: number of times to call wait_random
        max_delay: max wait time for each call to wait_random
    Returns:
        total_time / n
    """
    s = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - s
    return elapsed / n
