import unittest


class Calculator:

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y
    

class TestCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.calc = Calculator()
    
    def tearDown(self) -> None:
        del self.calc
    
    def test_add(self):
        self.assertEqual(self.calc.add(2 ,2) ,4)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 2), 0)


if __name__ == "__main__":
    unittest.main()
