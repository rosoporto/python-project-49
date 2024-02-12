#!/usr/bin/env python3
from random import randint
from brain_games.engine import launch_game
from brain_games.const import MIN_NUM, MAX_NUM
from brain_games.const import INSTRUCTION_FOR_EVEN_GAME


def is_even(num):
    return num % 2 == 0


def get_num_and_check_even():
    random_num = randint(MIN_NUM, MAX_NUM)
    verified_random_num = "yes" if is_even(random_num) else "no"
    return random_num, verified_random_num


def run_even_game():
    launch_game(get_num_and_check_even, INSTRUCTION_FOR_EVEN_GAME)
