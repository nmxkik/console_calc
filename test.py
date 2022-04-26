import unittest
from calc import Calc

c = Calc()


class CalculateTests(unittest.TestCase):

    def test_add_method(self):
        result = c.calculate("(2+3)-(4*5)")
        self.assertEqual(result, -15)

    def test_add_method_wrong_value(self):
        result = c.calculate("2+2")
        self.assertNotEqual(result, 5)

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


if __name__ == '__main__':
    unittest.main()
