#!/usr/bin/python3

def addition(a, b):
    return a+b


def subtraction(a, b):
    return a-b


def division(a, b):
    return a/b


def multiplication(a, b):
    return a*b


def grade_calculator(scores):
    avg_score = sum(scores)/len(scores)
    if avg_score >= 90:
        return 'A'
    elif avg_score >= 80:
        return 'B'
    elif avg_score >= 70:
        return 'C'
    elif avg_score >= 60:
        return 'D'
    else:
        return 'F'
