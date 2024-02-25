#!/usr/bin/env python3
from random import randint


GAME_RULE = "Find the greatest common divisor of given numbers."
MIN_NUM = 1
MAX_NUM = 100


def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def run_even_game():
    num1, num2 = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
    random_nums = f"{num1} {num2}"
    gcd_num = find_gcd(num1, num2)
    return random_nums, str(gcd_num)
