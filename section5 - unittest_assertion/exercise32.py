import unittest


class Doc:
    def __init__(self, string: str) -> None:
        self.string = string

    def __repr__(self) -> str:
        return f"Doc(string='{self.string}')"

    def __eq__(self, other) -> bool:
        return len(self.string) == len(other.string)

    def __ne__(self, other) -> bool:
        return len(self.string) != len(other.string)


class Inputs:

    DOC1 = Doc('Online')
    DOC2 = Doc('Nature')
    DOC3 = Doc('Technology')


class TestDoc(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(Inputs.DOC1, Inputs.DOC2)

    def test_not_equal(self):
        self.assertNotEqual(Inputs.DOC3, Inputs.DOC1)
        self.assertNotEqual(Inputs.DOC3, Inputs.DOC2)


if __name__ == "__main__":
    unittest.main()
