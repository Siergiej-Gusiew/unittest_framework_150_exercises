import unittest


class StringListOnly(list):

    def append(self, string: str) -> None:
        if not isinstance(string, str):
            raise TypeError(
                'Only object of type str can be added to the list.'
            )
        super().append(string)


class TestStringListOnly(unittest.TestCase):

    def test_slo_is_instance(self):
        slo = StringListOnly()
        self.assertIsInstance(slo, StringListOnly)
        self.assertIsInstance(slo, list)

if __name__ == "__main__":
    unittest.main()
