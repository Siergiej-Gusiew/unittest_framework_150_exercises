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


    def test_valid_input(self):
        inp = [50, 50, 50]
        self.assertAlmostEqual(calculate_grade(inp), 50)
        # inp = [-50, 0, 50]
        # self.assertAlmostEqual(calculate_grade(inp), 0)
        # inp = [-50, -50, -50]
        # self.assertAlmostEqual(calculate_grade(inp), -50)
        inp = [90, 0, 0]
        self.assertAlmostEqual(calculate_grade(inp), 30)
        inp = [0]
        self.assertAlmostEqual(calculate_grade(inp), 0)
        inp = [1.5, 2.5, 5.0]
        self.assertAlmostEqual(calculate_grade(inp), 3)


if __name__ == "__main__":
    unittest.main()
