import unittest


def calculate(numbers, operation):
    if not isinstance(numbers, list):
        raise TypeError("First argument must be a list of numbers")
    if not isinstance(operation, str) or operation not in [
        "+",
        "-",
        "*",
        "/",
    ]:
        raise ValueError(
            "Second argument must be a string representing"
            "a valid operation (+, -, *, /)"
        )
    if operation == "+":
        return sum(numbers)
    elif operation == "-":
        return numbers[0] - sum(numbers[1:])
    elif operation == "*":
        result = 1
        for num in numbers:
            result *= num
        return result
    elif operation == "/":
        if 0 in numbers:
            raise ZeroDivisionError("Cannot divide by zero")
        result = numbers[0]
        for num in numbers[1:]:
            result /= num
        return result


class TestCalculate(unittest.TestCase):

    def setUp(self) -> None:
        self.input = [1, 2, 3]
    
    def tearDown(self) -> None:
        del self.input

    def test_raises_type_error_if_first_arg_not_list(self):
        with self.assertRaises(TypeError):
            calculate(1, "+")

    def test_raises_value_error_if_second_arg_not_valid_operation(self):
        with self.assertRaises(ValueError):
            calculate(self.input, "!")

    def test_performs_addition_correctly(self):
        self.assertEqual(calculate(self.input, "+"), 6)

    def test_performs_subtraction_correctly(self):
        self.assertEqual(calculate(self.input, "-"), -4)

    def test_performs_multiplication_correctly(self):
        self.assertEqual(calculate(self.input, "*"), 6)

    def test_performs_division_correctly(self):
        self.assertAlmostEqual(calculate(self.input, "/"), 1 / 2 / 3)

    def test_raises_zero_division_error_if_dividing_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calculate([1, 0, 3], "/")

        
if __name__ == "__main__":
    unittest.main()
