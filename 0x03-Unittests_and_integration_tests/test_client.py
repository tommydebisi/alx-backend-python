#!/usr/bin/env python3
"""
    tests for client.py
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, param

GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        tests the githuborgclient class
    """
    @parameterized.expand([
            param('google'),
            param('abc')
        ])
    @patch('client.get_json')
    def test_org(self, org_name,  mock_get_json):
        """ test the org function for correct output """
        test_git = GithubOrgClient(org_name)
        # call the org method, by calling it get_json gets called
        test_git.org()
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """ tests the public repo output """
        with patch.object(GithubOrgClient, 'org',
                          new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {'repos_url': "legoo"}
            git_tes = GithubOrgClient('leggo')

            self.assertEqual(git_tes._public_repos_url, 'legoo')

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ more tests on public repos """
        dic_list = [{"repos_url": "on code"}, {'name': 'on code'}]
        mock_get_json.return_value = dic_list
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pub_repo:
            mock_pub_repo.return_value = "on c"
            tes_git = GithubOrgClient('doom')

            self.assertEqual(tes_git.repos_payload, dic_list)
            mock_pub_repo.assert_called_once()
            mock_get_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
