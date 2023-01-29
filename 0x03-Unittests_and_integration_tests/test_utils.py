#!/usr/bin/env python3
"""
    test file for utils.py
"""
import unittest
from parameterized import parameterized, param
from unittest.mock import patch, Mock

access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """
        class to test all outputs for the access_nested_map
        function
    """
    @parameterized.expand([
            param({"a": 1}, ("a",), 1),
            param({"a": {"b": 2}}, ("a",), {'b': 2}),
            param({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map, path, result):
        """ checking function gets correct result """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
            param({}, ('a',)),
            param({'a': 1}, ('a', 'b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ checks for valid exception raise """
        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)
            self.assertEqual(str(exc.exception), 'a')


class TestGetJson(unittest.TestCase):
    """
        class to test inputs for the get_json
        function
    """
    @parameterized.expand([
            param('http://example.com', {"payload": True}),
            param('http://holberton.io', {"payload": False})
        ])
    def test_get_json(self,  test_url, test_payload):
        """ checks for correct output from func """
        with patch('utils.requests.get') as mock_util_req:
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = test_payload
            mock_util_req.return_value = mock_response

            self.assertEqual(get_json(test_url), test_payload)
            mock_util_req.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
        class to test inputs for the memoize function
        decorator
    """
    def test_memoize(self):
        """ checks for correct output from method """
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as a_meth:
            testy = TestClass()
            testy.a_property()
            testy.a_property()

            a_meth.assert_called_once()


if __name__ == "__main__":
    unittest.main()
