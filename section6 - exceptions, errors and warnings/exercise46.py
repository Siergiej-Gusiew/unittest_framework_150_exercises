import unittest


def calculate_grade(scores):
    if not isinstance(scores, list):
        raise TypeError("Input must be a list")
    if not scores:
        raise ValueError("List cannot be empty")
    if not all(isinstance(score, (int, float)) for score in scores):
        raise TypeError("Elements of list must be numbers")
    if not all(0 <= score <= 100 for score in scores):
        raise ValueError("Elements of list must be between 0 and 100")
    return sum(scores) / len(scores)


class TestCalculateGrade(unittest.TestCase):

    def test_non_list_input(self):
        with self.assertRaisesRegex(TypeError, "Input must be a list"):
            calculate_grade(123)

    def test_empty_list_input(self):
        with self.assertRaisesRegex(ValueError, "List cannot be empty"):
            calculate_grade(list())

    def test_non_numeric_element(self):
        with self.assertRaisesRegex(TypeError, "Elements of list must be numbers"):
            calculate_grade(["1", 2, 3])

    def test_out_of_range_element(self):
        with self.assertRaisesRegex(ValueError, "Elements of list must be between 0 and 100"):
            calculate_grade([-100])


if __name__ == "__main__":
    unittest.main()
