#!/usr/bin/python3

import unittest
from mycalculator import addition, subtraction, division, multiplication, grade_calculator


class TestCalculator(unittest.TestCase):
    def test_addtion(self):
        self.assertEqual(addition(2, 3), 5, "Wrong expected value")

    def test_subtraction(self):
        self.assertEqual(subtraction(3, 3), 0)

    def test_multiplication(self):
        self.assertEqual(multiplication(10, 10), 100)

    def test_division(self):
        self.assertEqual(division(10, 2), 5)


class TestGradeCalculator(unittest.TestCase):
    def test_grade_calculator_a(self):
        scores = [95, 95, 95, 95, 95]
        self.assertEqual(grade_calculator(scores), 'A')

    def test_grade_calculator_b(self):
        scores = [85, 85, 85, 85, 85]
        self.assertEqual(grade_calculator(scores), 'B')

    def test_grade_calculator_c(self):
        scores = [75, 75, 75, 75, 75]
        self.assertEqual(grade_calculator(scores), 'C')

    def test_grade_calculator_d(self):
        scores = [65, 65, 65, 65, 65]
        self.assertEqual(grade_calculator(scores), 'D')

    def test_grade_calculator_f(self):
        scores = [55, 55, 55, 55, 55]
        self.assertEqual(grade_calculator(scores), 'F')


def main():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestCalculator)
    runner = unittest.TextTestRunner()
    runner.run(suite)

    suite = loader.loadTestsFromTestCase(TestGradeCalculator)
    runner.run(suite)


if __name__ == "__main__":
    main()
