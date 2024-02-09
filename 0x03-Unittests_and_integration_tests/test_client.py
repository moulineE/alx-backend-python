#!/usr/bin/env python3
"""0x03. Unittests and Integration Tests module for client.py"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """unit test for client.GithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={"value": True})
    def test_org(self, org_name: str, mock_get_json: MagicMock) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(org_name)
        response = test_class.org

        self.assertEqual(response, {"value": True})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
