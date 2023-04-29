#!/usr/bin/python3

import unittest


def sort_words(word):
    if not isinstance(word, str):
        word = str(word)
    list_word = list(word)
    sorted_word = sorted(list_word, key=str.lower)
    return "".join(sorted_word)


class TestSortWords(unittest.TestCase):

    def test_sort_words_on_empty_string(self):
        self.assertEqual(sort_words(""), "")

    def test_sort_words_on_one_letter_string(self):
        self.assertEqual(sort_words("e"), "e")

    def test_sort_words_repeated_strings(self):
        self.assertEqual(sort_words("abaaaaabaa"), "aaaaaaaabb")

    def test_sort_words_normal_string(self):
        self.assertEqual(sort_words("helloworld"), "dehllloorw")

    def test_sort_words_integer(self):
        self.assertEqual(sort_words(242891507), "012245789")


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSortWords)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
