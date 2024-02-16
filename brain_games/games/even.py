#!/usr/bin/env python3
from random import randint


GAME_RULE = "Answer \"yes\" if the number is even, "\
            "otherwise answer \"no\"."
MIN_NUM = 1
MAX_NUM = 100


def is_even(num):
    return num % 2 == 0


def run_even_game():
    random_num = randint(MIN_NUM, MAX_NUM)
    verified_random_num = "yes" if is_even(random_num) else "no"
    return random_num, verified_random_num
