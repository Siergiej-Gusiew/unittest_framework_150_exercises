import unittest
from typing import Optional


def calculate_average(numbers: list) -> Optional[float]:
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


class TestCalculateAverage(unittest.TestCase):

    def test_calculate_average_valid_input(self):
        inputs = [[1, 1, 1], [5, 10, 15], [-100, 0, 100]]
        outputs = [1, 10, 0]
        for inp, out in zip(inputs, outputs):
            self.assertAlmostEqual(calculate_average(inp), out)

    def test_calculate_average_empty_input(self):
        self.assertIsNone(calculate_average([]))

    def test_calculate_average_invalid_input(self):
        inputs = [1, [1, 2, "3"], [1, 2, []]]
        for inp in inputs:
            self.assertRaises(TypeError, calculate_average, inp)


if __name__ == "__main__":
    unittest.main()
