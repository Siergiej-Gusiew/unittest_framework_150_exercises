import unittest


class StringReverser:
    def reverse(self, string):
        return string[::-1]


class TestStringReverser(unittest.TestCase):
    
    def test_reverse(self):
        reverse_inst = StringReverser()
        test_case_input = ["hello", "12345", ""]
        test_case_output = ["olleh", "54321", ""]
        for inp, out in zip(test_case_input, test_case_output):
            self.assertEqual(reverse_inst.reverse(inp), out)
            
if __name__ == "__main__":
    unittest.main()
