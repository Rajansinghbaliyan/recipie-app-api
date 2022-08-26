"""
Sample test module
"""
from django.test import SimpleTestCase
from app import calc


class CalculateTest(SimpleTestCase):
    def test_add_nums(self):
        num1, num2 = 5, 7
        res = calc.cal(num1, num2)
        self.assertEqual(num1 + num2, res)
