import unittest


class Rectangle:

    def __init__(self, width: float, height: float) -> None:
        self._validate_params(width, height)
        self.width = width
        self.height = height

    def _validate_params(self, width: float, height: float) -> None:
        if not isinstance(width, (int, float)) or width < 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(height, (int, float)) or height < 0:
            raise ValueError("Height must be a positive number")

    def area(self) -> float:
        return self.width * self.height

class TestRectangle(unittest.TestCase):

    def test_area_with_nonzero_dimensions(self):
        width, height = 2, 5.5
        rect = Rectangle(width, height)
        self.assertEqual(rect.area(), width * height, f"RESULT: {rect.area} != {width * height}")

    def test_area_with_zero_dimensions(self):
        width, height = 0, 5.5
        rect = Rectangle(width, height)
        self.assertEqual(rect.area(), width * height, f"RESULT: {rect.area} != {width * height}")

    def test_area_with_negative_width(self):
        width, height = -3.0, 5.5
        with self.assertRaises(ValueError):
            rect = Rectangle(width, height)
            rect.area()

    def test_area_with_negative_height(self):
        width, height = 3.0, -5.5
        with self.assertRaises(ValueError):
            rect = Rectangle(width, height)
            rect.area()

    def test_area_with_float_dimensions(self):
        width, height = 3.0, 5.5
        rect = Rectangle(width, height)
        self.assertEqual(rect.area(), width * height, f"RESULT: {rect.area} != {width * height}")

    def test_area_with_large_dimensions(self):
        width, height = 300000.0, 550000.0
        rect = Rectangle(width, height)
        self.assertEqual(rect.area(), width * height, f"RESULT: {rect.area} != {width * height}")
            

if __name__ == "__main__":
    unittest.main()
