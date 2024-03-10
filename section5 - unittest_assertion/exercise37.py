import unittest


class Calculator:

    def divide(self, dividend: float, divisor: float) -> float:
        if divisor == 0:
            raise ValueError("Cannot divide by zero")
        return dividend / divisor


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def tearDown(self):
        del self.calc

    def test_divide_positive_numbers(self):
        self.assertAlmostEqual(self.calc.divide(15, 5), 3)

    def test_divide_zero_by_positive_number(self):
        self.assertAlmostEqual(self.calc.divide(0, 5), 0)

    def test_divide_negative_by_positive_number(self):
        self.assertAlmostEqual(self.calc.divide(-15, 5), -3)

    def test_divide_by_zero_should_raise_error(self):
        self.assertRaises(ValueError, self.calc.divide, -15, 0)


if __name__ == "__main__":
    unittest.main()
