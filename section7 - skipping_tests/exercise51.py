from datetime import date
import unittest


class Container:

    def __init__(self):
        if date.today().day % 2 == 0:
            self.code = 'XC-0'
        else:
            self.code = 'XC-1'


class TestContainer(unittest.TestCase):

    @unittest.skipIf(date.today().day % 2 == 1, "Skipping odd days.")
    def test_code_ends_with_0_on_even_days(self):
        c = Container()
        self.assertTrue(
            c.code.endswith('0'), 'Expected code to end with 0.'
        )

    @unittest.skipIf(date.today().day % 2 == 0, "Skipping even days.")
    def test_code_ends_with_1_on_odd_days(self):
        c = Container()
        self.assertTrue(
            c.code.endswith('1'), 'Expected code to end with 1.'
        )


if __name__ == "__main__":
    unittest.main()
