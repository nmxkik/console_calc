from turtle import clear
import unittest
from unittest.mock import patch, Mock

from defer import return_value
from calc import Calc
from calculator import main

c = Calc()


class CalculateTests(unittest.TestCase):

    def test_many_signs(self):
        result = c.calculate("(2+3)-(4*5)")
        self.assertEqual(result, -15)

    def test_many_signs_wrong_value(self):
        result = c.calculate("2+2")
        self.assertNotEqual(result, 5)

    def test_no_ints(self):
        result = c.calculate("2.0 + 5.0")
        self.assertEqual(result, 7.0)

    def test_add_method_invalid_value(self):
        self.assertRaises(
            NameError, c.calculate, "four + five")

    def test_multiply_method(self):
        result = c.calculate("5*3*1")
        self.assertEqual(result, 15)

    def test_sub_method(self):
        result = c.calculate("6-2")
        self.assertEqual(result, 4)

    def test_div_method_zero(self):
        self.assertRaises(ZeroDivisionError, c.calculate, "5/0")


class MainLoopTest(unittest.TestCase):

    @patch("builtins.input", return_value="exit")
    def test_input(self, input):
        self.assertRaises(SystemExit, main)


if __name__ == '__main__':
    unittest.main()
