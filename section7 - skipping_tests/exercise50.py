import unittest


class Container:
    code = 'ABCD1234'


class TestContainer(unittest.TestCase):
    def test_container_is_instance_of_type(self) -> None:
        self.assertIsInstance(Container, type)

    @unittest.skip('The Container class requires implementation.')
    def test_container_has_code_attribute(self) -> None:
        msg = 'The Container class does not have a code attribute.'
        self.assertTrue(hasattr(Container, 'code'), msg)


if __name__ == "__main__":
    unittest.main()
