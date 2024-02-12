#!/usr/bin/env python3
from random import randint, choice
from brain_games.engine import launch_game
from brain_games.const import MATH_SIGNS, MIN_NUM, MAX_NUM
from brain_games.const import INSTRUCTION_FOR_CALC_GAME


def get_result_by_math_sign():
    num1, num2 = randint(MAX_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM / 2)
    math_sign = choice(MATH_SIGNS)
    expression = f"{num1} {math_sign} {num2}"
    math_result = eval(expression)
    return expression, str(math_result)


def run_even_game():
    launch_game(get_result_by_math_sign, INSTRUCTION_FOR_CALC_GAME)
