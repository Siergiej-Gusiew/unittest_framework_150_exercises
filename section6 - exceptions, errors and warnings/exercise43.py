import unittest


def find_longest_word(words):
    if not isinstance(words, list):
        raise TypeError("Input must be a list")
    if not all(isinstance(word, str) for word in words):
        raise TypeError("List must contain only strings")
    if not words:
        raise ValueError("List cannot be empty")
    return max(words, key=len)


class TestFindLongestWord(unittest.TestCase):

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            find_longest_word(list())

    def test_non_string_elements(self):
        with self.assertRaises(TypeError):
            find_longest_word([dict()])
        with self.assertRaises(TypeError):
            find_longest_word([1, 3, 5.5])
        with self.assertRaises(TypeError):
            find_longest_word([[], [], []])


if __name__ == "__main__":
    unittest.main()
