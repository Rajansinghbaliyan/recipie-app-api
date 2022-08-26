from django.test import SimpleTestCase
from app import calc


class TestClac(SimpleTestCase):
    def test_add_num(self):
        num1, num2 = 5, 6
        res = calc.add(num1, num2)
        self.assertEqual(num1 + num2, res)
