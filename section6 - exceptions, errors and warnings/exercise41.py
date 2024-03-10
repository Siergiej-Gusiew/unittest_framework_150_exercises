import unittest


def calculate_discount(price, discount_rate):
    if not isinstance(price, (int, float)):
        raise TypeError("Price must be a number")
    if not isinstance(discount_rate, (int, float)):
        raise TypeError("Discount rate must be a number")
    if price < 0 or discount_rate < 0:
        raise ValueError(
            "Price and discount rate must be non-negative"
        )
    discount = price * discount_rate
    return price - discount


class TestCalculateDiscount(unittest.TestCase):

    def test_non_number_price(self):
        with self.assertRaises(TypeError):
            calculate_discount("25000", 0.25)

    def test_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discount(-1000, 0.25)


if __name__ == "__main__":
    unittest.main()
