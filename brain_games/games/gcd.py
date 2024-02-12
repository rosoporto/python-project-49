#!/usr/bin/env python3
from random import randint
from brain_games.engine import launch_game
from brain_games.const import MIN_NUM, MAX_NUM
from brain_games.const import INSTRUCTION_FOR_GCD_GAME


def find_gcd():
    num1, num2 = randint(MIN_NUM, MAX_NUM), randint(MIN_NUM, MAX_NUM)
    random_nums = f"{num1} {num2}"
    while num2:
        num1, num2 = num2, num1 % num2
    return random_nums, str(num1)


def run_even_game():
    launch_game(find_gcd, INSTRUCTION_FOR_GCD_GAME)
