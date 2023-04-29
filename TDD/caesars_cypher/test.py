#!/usr/bin/python3
import unittest
from main import encrypt


class TestEncryption(unittest.TestCase):
    def setUp(self):
        self.message = "banana"

    def test_input_has_value(self):
        self.assertIsNotNone(self.message)

    def test_message_is_string(self):
        self.assertIsInstance(self.message, str)

    def test_output_is_string(self):
        self.assertIsInstance(encrypt(self.message), str)

    def test_function_returns_something(self):
        self.assertIsNotNone(encrypt(self.message))

    def test_length_of_input_equals_length_of_output(self):
        self.assertEqual(len(self.message), len(encrypt(self.message)))

    def test_input_is_differnt_from_output(self):
        self.assertNotEqual(self.message, encrypt(self.message))

    def test_shifted_cipher_one(self):
        self.assertEqual(encrypt(self.message), 'cbobob')

    def test_shifted_cipher_with_shifted_value_more_than_one(self):
        self.assertEqual(encrypt(self.message, 4), 'ferere')
        self.assertEqual(encrypt(self.message, 8), 'jivivi')

    def test_shifted_cipher_with_negative_shifted_value(self):
        self.assertEqual(encrypt(self.message, -8), '43f3f3')


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestEncryption)
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    main()
