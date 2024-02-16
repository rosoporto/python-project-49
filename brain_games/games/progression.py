#!/usr/bin/env python3
from random import randint, choice


GAME_RULE = "What number is missing in the progression?"
MIN_NUM = 1
MAX_NUM_PROGRESSION = 10


def generate_progression():
    start = randint(MIN_NUM, MAX_NUM_PROGRESSION)
    diff = randint(MIN_NUM, MAX_NUM_PROGRESSION / 2)
    progression = [start + diff * i for i in range(MAX_NUM_PROGRESSION)]
    return progression


def hide_num_and_generate_question(progression, missing_num):
    missing_index = progression.index(missing_num)
    progression[missing_index] = ".."
    return ' '.join(list(map(str, progression)))


def run_even_game():
    progression = generate_progression()
    missing_num = choice(progression)
    str_progression = hide_num_and_generate_question(progression, missing_num)
    return str_progression, str(missing_num)
