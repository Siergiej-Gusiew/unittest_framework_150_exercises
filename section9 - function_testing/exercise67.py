import unittest
from tax import calculate_tax


class TestCalculateTax(unittest.TestCase):

    def test_tax_with_eighteen_age(self):
        self.assertEqual(calculate_tax(60_000, 18), 6_000)

    def test_tax_with_nineteen_age(self):
        self.assertEqual(calculate_tax(60_000, 19), 10_200)

    def test_tax_with_sixty_five_age(self):
        self.assertEqual(calculate_tax(60_000, 65), 10_200)

    def test_tax_with_sixty_six_age(self):
        self.assertEqual(calculate_tax(66_000, 66), 9_000)


if __name__ == "__main__":
    unittest.main()
