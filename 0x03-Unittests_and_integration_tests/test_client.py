#!/usr/bin/env python3
"""
    tests for client.py
"""
import unittest
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized, parameterized_class


GithubOrgClient = __import__('client').GithubOrgClient
TEST_PAYLOAD = __import__('fixtures').TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """
        tests the githuborgclient class
    """
    @parameterized.expand([
            ('google'),
            ('abc')
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
        dic_list = [{
                "repos_url": "https://good.com",
                "name": "Bruce"
            },
            {
                'repos_url': "https://bad.com",
                'name': 'on code'
                }]
        mock_get_json.return_value = dic_list
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_pub_repo:
            mock_pub_repo.return_value = "https://great.com"
            tes_git = GithubOrgClient('doom')

            self.assertEqual(tes_git.repos_payload, dic_list)
            mock_pub_repo.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, license, license_key, output):
        """ testing for repos license """
        self.assertEqual(GithubOrgClient.has_license(license,
                                                     license_key), output)


@parameterized_class(('org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
        Performing integration tests on GithubOrgClient
    """
    @classmethod
    def setUpClass(cls) -> None:
        mock_req_get = Mock()
        mock_req_get.json.return_value = cls.repos_payload
        cls.get_patcher = patch('requests.get', return_value=mock_req_get)
        cls.get_patcher.start()

    def test_public_repos(self):
        """ testing the public repos """
        test_git = GithubOrgClient(self)
        self.assertEqual(test_git.org, self.org_payload)
        self.assertEqual(test_git.public_repos(),
                         self.expected_repos)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
