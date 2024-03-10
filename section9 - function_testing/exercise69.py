import unittest
from tax import income_tax


class TestIncomeTax(unittest.TestCase):

    def test_tax_below_threshold(self):
        self.assertAlmostEqual(income_tax(60_000), 10_200)

    def test_tax_equal_threshold(self):
        self.assertAlmostEqual(income_tax(85_528), 14_539.76)

    def test_tax_above_threshold(self):
        self.assertAlmostEqual(income_tax(100_000), 19_170.8)


if __name__ == "__main__":
    unittest.main()
