import sys
import unittest


class Container:

    def __init__(self):
        if sys.platform.startswith('win'):
            self.code = 'XC-win'
        else:
            self.code = f'XC-{sys.platform}'


class TestContainer(unittest.TestCase):
    
    @unittest.skipUnless(sys.platform.startswith('win'), "Requires Windows.")
    def test_code_is_XC_win_on_Windows(self):
        c = Container()
        self.assertEqual(c.code, 'XC-win', 'Expected code to be XC-win.')

    @unittest.skipUnless(sys.platform.startswith('linux'), "Requires Linux.")
    def test_code_starts_with_XC_on_Linux(self):
        c = Container()
        self.assertEqual(
            c.code, 'XC-linux', 'Expected code to be XC-linux.'
        )


if __name__ == "__main__":
    unittest.main()
