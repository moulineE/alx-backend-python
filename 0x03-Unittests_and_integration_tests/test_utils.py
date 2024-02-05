#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests module"""
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union
import utils
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """unit test for utils.access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nested_map: Dict, path: Tuple[int],
                               expected: Union[Dict, int]) -> None:
        """unitest for utils.access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
