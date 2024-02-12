#!/usr/bin/env python3
from random import randint
from brain_games.engine import launch_game
from brain_games.const import MIN_NUM, MAX_NUM
from brain_games.const import INSTRUCTION_FOR_PRIME_GAME


def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_num_and_prime_ans():
    random_num = randint(MIN_NUM, MAX_NUM)
    check_num = "yes" if is_prime(random_num) else "no"
    return random_num, check_num


def run_even_game():
    launch_game(get_num_and_prime_ans, INSTRUCTION_FOR_PRIME_GAME)
