#!/usr/bin/env python3
from typing import List
"""
a type-annotated function sum_list which takes a list input_list of floats as
argument and returns their sum as a float.
"""


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list: list of floats
    Return:
        sum of the list : floats
    """
    return float(sum(input_list))
