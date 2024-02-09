#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests module for client.py"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """unit test for client.GithubOrgClient class"""
    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True})
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, test_payload: Dict,
                 mock_get_json: MagicMock) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = test_payload
        test_class = GithubOrgClient(org_name)
        response = test_class.org

        self.assertEqual(response, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
