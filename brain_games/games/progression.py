#!/usr/bin/env python3
from random import randint, choice


GAME_RULE = "What number is missing in the progression?"
MIN_NUM = 1
MAX_NUM_PROGRESSION = 10


def generate_progression(start, diff, max_num):
    progression = [start + diff * i for i in range(max_num)]
    return progression


def hide_num_and_generate_quest(progression, index_hide_num):
    hide_num = progression[index_hide_num]
    progression[index_hide_num] = ".."
    return ' '.join(list(map(str, progression))), hide_num


def run_even_game():
    start = randint(MIN_NUM, MAX_NUM_PROGRESSION)
    diff = randint(MIN_NUM, MAX_NUM_PROGRESSION / 2)
    progression = generate_progression(start, diff, MAX_NUM_PROGRESSION)
    index_missing_num = choice(range(len(progression)))
    str_progression, hide_num = hide_num_and_generate_quest(progression,
                                                            index_missing_num)
    return str_progression, str(hide_num)
