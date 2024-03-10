import unittest


class Doc:
    def __init__(self, string: str) -> None:
        self.string = string
        
    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"

    def __lt__(self, other) -> bool:
        return len(self.string) < len(other.string)

    def __gt__(self, other) -> bool:
        return len(self.string) > len(other.string)


class Inputs:

    DOC1 = Doc('Technology')
    DOC2 = Doc('Online')
    DOC3 = Doc('Nature')


class TestDoc(unittest.TestCase):

    def test_less_than(self):
        self.assertLess(Inputs.DOC2, Inputs.DOC1)
        self.assertLess(Inputs.DOC3, Inputs.DOC1)

    def test_greater_than(self):
        self.assertGreater(Inputs.DOC1, Inputs.DOC2)
        self.assertGreater(Inputs.DOC1, Inputs.DOC3)

if __name__ == "__main__":
    unittest.main()
