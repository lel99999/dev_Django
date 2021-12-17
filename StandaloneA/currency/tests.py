import unittest
from currency.templatetags.currency_tags import accounting

class TestTemplateFilters(unittest.TestCase):

    def test_positive_value(self):
        self.assertEqual("10",accounting(10))

    def test_zero_value(self):
        self.assertEqual("0",accounting(0))

    def test_negative_value(self):
        self.assertEqual("-10",accounting(-10))
