import unittest


def calculate_daily_return(
    open_price: float,
    close_price: float,
) -> float:
    return round(((close_price / open_price) - 1) * 100, 2)


class TestCalculateDailyReturn(unittest.TestCase):
    
    def test_positive_return(self):
        self.assertEqual(calculate_daily_return(349.0, 360.0), 3.15)

    def test_negative_return(self):
        self.assertEqual(calculate_daily_return(349.0, 340.0), -2.58)

    def test_zero_return(self):
        self.assertAlmostEqual(calculate_daily_return(349.0, 349.0), 0)


if __name__ == "__main__":
    unittest.main()
