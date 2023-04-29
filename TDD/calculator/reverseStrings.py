#!/usr/bin/python3

import unittest


def reverse_string(string):
    if isinstance(string, int):
        string = str(string)
    return (string[::-1])


class TestReverseString(unittest.TestCase):
    def test_reverse_string_with_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_string_with_special_chars(self):
        self.assertEqual(reverse_string("\n\\\b"), "\b\\\n")

    def test_reverse_string_with_banana(self):
        self.assertEqual(reverse_string("banana"), "ananab")

    def test_reverse_string_with_number(self):
        self.assertEqual(reverse_string(1234), "4321")


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
