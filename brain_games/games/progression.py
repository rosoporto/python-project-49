#!/usr/bin/env python3
from random import randint, choice


RULE = "What number is missing in the progression?"
MIN_NUM = 1
MAX_NUM_PROGRESSION = 10


def generate_progression(start, diff, max_num):
    progression = [start + diff * i for i in range(max_num)]
    return progression


def set_hidden_num(progression, index_hide_num):
    progression[index_hide_num] = ".."
    return progression


def get_hidden_num(progression, index_hide_num):
    return progression[index_hide_num]


def generate_quest(progression):
    return ' '.join(list(map(str, progression)))


def prepare_question_answer():
    start = randint(MIN_NUM, MAX_NUM_PROGRESSION)
    diff = randint(MIN_NUM, MAX_NUM_PROGRESSION / 2)
    progression = generate_progression(start, diff, MAX_NUM_PROGRESSION)
    index_missing_num = choice(range(len(progression)))
    hide_num = get_hidden_num(progression, index_missing_num)
    progression_hide_num = set_hidden_num(progression, index_missing_num)
    str_progression = generate_quest(progression_hide_num)
    return str_progression, str(hide_num)
