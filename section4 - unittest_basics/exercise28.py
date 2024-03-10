import unittest


def find_largest(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise TypeError("All elements in the list must be numbers")
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


class TestFindLargest(unittest.TestCase):

    def test_find_largest_valid_input(self):
        inputs = [[1, 1, 1], [-10, 0, 10], [500, 100, 5]]
        outputs = [1, 10, 500]
        for inp, out in zip(inputs, outputs):
            self.assertEqual(find_largest(inp), out)

    def test_find_largest_empty_input(self):
        self.assertIsNone(find_largest([]))

    def test_find_largest_invalid_input(self):
        inputs = [[1, 1, "1"], [-10, [0], 10], 5.50]
        for inp in inputs:
            self.assertRaises(TypeError, find_largest, inp)

if __name__ == "__main__":
    unittest.main()
