#!/usr/bin/env python3
"""
a type-annotated function floor which takes a float n as argument
and returns the floor of the float.
"""


def floor(n: float) -> int:
    """
    Args:
        n (float): float number
    Returns:
        int: floor of n
    """
    return int(n) if n >= 0 else int(n) - 1
