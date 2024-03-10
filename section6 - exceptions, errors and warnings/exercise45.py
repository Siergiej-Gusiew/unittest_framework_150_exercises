import unittest


def calculate_shipping_cost(weight, destination):
    if not isinstance(weight, (int, float)):
        raise TypeError("Weight must be a number")
    if weight <= 0:
        raise ValueError("Weight must be greater than zero")
    if not isinstance(destination, str):
        raise TypeError("Destination must be a string")
    if not destination:
        raise ValueError("Destination cannot be empty")
    if destination.lower() == "usa":
        return 0
    if destination.lower() == "canada":
        return weight * 1.5
    if destination.lower() == "mexico":
        return weight * 2.0
    return weight * 5.0


class TestCalculateShippingCost(unittest.TestCase):

    def test_non_numeric_weight(self):
        with self.assertRaisesRegex(TypeError, "Weight must be a number"):
            calculate_shipping_cost("123", "ksjdhf")

    def test_non_positive_weight(self):
        with self.assertRaisesRegex(ValueError, "Weight must be greater than zero"):
            calculate_shipping_cost(-123, "lksjf")

    def test_non_string_destination(self):
        with self.assertRaisesRegex(TypeError, "Destination must be a string"):
            calculate_shipping_cost(123, 87236)

    def test_empty_destination(self):
        with self.assertRaisesRegex(ValueError, "Destination cannot be empty"):
            calculate_shipping_cost(123, "")


if __name__ == "__main__":
    unittest.main()
