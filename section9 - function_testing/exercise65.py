import unittest
import math


def circle_area(radius):
    """Calculate the area of a circle given its radius."""

    if not isinstance(radius, (int, float)):
        raise TypeError('Radius must be of type int or float.')

    if not radius > 0:
        raise ValueError('Radius must be positive.')

    return math.pi * radius ** 2


class TestCircleArea(unittest.TestCase):

    def test_area_with_radius_one(self):
        self.assertEqual(circle_area(1), math.pi * 1 ** 2)

    def test_area_with_radius_three(self):
        self.assertEqual(circle_area(3), math.pi * 3 ** 2)

    def test_incorrect_type(self):
        with self.assertRaises(TypeError):
            circle_area("4")
        with self.assertRaises(TypeError):
            circle_area(None)

    def test_incorrect_value(self):
        with self.assertRaises(ValueError):
            circle_area(0)
        with self.assertRaises(ValueError):
            circle_area(-3)

    
if __name__ == "__main__":
    unittest.main()
