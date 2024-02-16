#!/usr/bin/env python3
from random import randint, choice


GAME_RULE = "What is the result of the expression?"
MATH_SIGNS = ("+", "-", "*")
MIN_NUM = 1
MAX_NUM = 100


def run_even_game():
    num1, num2 = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM / 2)
    math_sign = choice(MATH_SIGNS)
    expression = f"{num1} {math_sign} {num2}"
    math_result = eval(expression)
    return expression, str(math_result)
