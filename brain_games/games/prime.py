#!/usr/bin/env python3
from random import randint


GAME_RULE = "Answer \"yes\" if given number is prime. "\
            "Otherwise answer \"no\"."
MIN_NUM = 1
MAX_NUM = 100


def is_prime(n):
    if n <= 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def check_num_on_prime(num):
    return "yes" if is_prime(num) else "no"


def run_even_game():
    random_num = randint(MIN_NUM, MAX_NUM)
    check_num = check_num_on_prime(random_num)
    return random_num, check_num
