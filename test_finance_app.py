import unittest
import itertools

from finance_app import *


class BasicTest(unittest.TestCase):
    def test_all_categories(self):
        self.assertFalse(compare_expenses(expenses, expenses_user))


if __name__ == '__main__':
    unittest.main()
