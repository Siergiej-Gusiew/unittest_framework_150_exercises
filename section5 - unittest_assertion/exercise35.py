import unittest


class StringListOnly(list):

    def append(self, string: str) -> None:
        if not isinstance(string, str):
            raise TypeError(
                'Only object of type str can be added to the list.'
            )
        super().append(string)


class TestStringListOnly(unittest.TestCase):


    def test_append_string(self):
        inst = StringListOnly()
        string = "hello"
        inst.append(string)
        self.assertIn(string, inst)
        

    def test_append_not_string_should_raise_error(self):
        inst = StringListOnly()
        self.assertRaises(TypeError, inst.append, list())
        self.assertRaises(TypeError, inst.append, True)


if __name__ == "__main__":
    unittest.main()
