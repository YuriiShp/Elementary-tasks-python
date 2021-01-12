"""UNIT TESTS"""

import os
import unittest
from unittest import TestCase
from parameterized import parameterized

from tasks.task_09_palindromes.classes import Number
from tasks.task_09_palindromes.runner import TaskRunner
from .extra import from_file

VAR_DATA = os.path.join(os.path.dirname(__file__), 'test_data', 'task_09')


class TestMath(TestCase):
    """Test Number class methods"""

    @parameterized.expand(from_file(directory=VAR_DATA, file='is_palindrome.json'))
    def test_is_palindrome(self, inp, expected):

        actual = Number(inp).is_palindrome()
        self.assertEqual(actual, expected)

    @parameterized.expand(from_file(directory=VAR_DATA, file='get_palindromes.json'))
    def test_get_palindromes(self, inp, expected):

        actual = Number(inp).get_palindromes()
        expected = [Number(i) for i in expected]
        self.assertListEqual(actual, expected)


class TestRun(TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
