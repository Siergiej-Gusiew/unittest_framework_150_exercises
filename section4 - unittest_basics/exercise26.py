import unittest
 
 
class TemperatureConverter:

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        return (celsius * 9 / 5) + 32

class TestTemperatureConverter(unittest.TestCase):
    
    def test_celsius_to_fahrenheit(self):
        converter = TemperatureConverter()
        inputs = [-10, 0, 25]
        outputs = [(celsius * 9 / 5) + 32 for celsius in inputs]
        for inp, out in zip(inputs, outputs):
            self.assertEqual(converter.celsius_to_fahrenheit(inp), out)

if __name__ == "__main__":
    unittest.main()
