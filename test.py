import unittest
from unittest.mock import patch, Mock

from calc import Calc
from main import main

c = Calc()


class TestCalculate(unittest.TestCase):

    def test_one_sigs(self):
        self.assertEqual(c.calculate("10"), 10)

    def test_many_signs(self):
        result = c.calculate("(2+3)-(4*5)")
        self.assertEqual(result, -15)

    def test_calculate_float(self):
        result = c.calculate("2.0 + 5.0")
        self.assertEqual(result, 7.0)

    def test_invalid_input(self):
        self.assertRaises(
            NameError, c.calculate, "four + five"
        )

    def test_multiply_method(self):
        result = c.calculate("5*3*2")
        self.assertEqual(result, 30)

    def test_sub_method(self):
        result = c.calculate("6-2")
        self.assertEqual(result, 4)

    def test_div_method_zero(self):
        self.assertRaises(ZeroDivisionError, c.calculate, "5/0")

    def test_many_math_simbols_in_a_row(self):
        self.assertEqual(c.calculate("5+++5"), 10)


class MainLoopTest(unittest.TestCase):

    @patch("builtins.input", return_value="exit")
    def test_input(self, input):
        self.assertRaises(SystemExit, main)


if __name__ == '__main__':
    unittest.main()
