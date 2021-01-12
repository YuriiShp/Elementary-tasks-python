"""UNIT TESTS"""

import os
import unittest
from unittest import TestCase
from parameterized import parameterized

from tasks.task_05_numbers.classes import NumEng, NumUa, TNumber
from tasks.task_05_numbers.runner import TaskRunner
from .extra import from_file

VAR_DATA = os.path.join(os.path.dirname(__file__), 'test_data', 'task_05')


class TestMath(TestCase):
    pass


class TestRun(TestCase):
    pass


if __name__ == '__main__':
    unittest.main()
