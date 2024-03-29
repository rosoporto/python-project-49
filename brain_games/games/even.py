#!/usr/bin/env python3
from random import randint


RULE = "Answer \"yes\" if the number is even, "\
       "otherwise answer \"no\"."
MIN_NUM = 1
MAX_NUM = 100


def is_even(num):
    return num % 2 == 0


def check_num_on_even(num):
    return "yes" if is_even(num) else "no"


def prepare_question_answer():
    random_num = randint(MIN_NUM, MAX_NUM)
    verified_random_num = check_num_on_even(random_num)
    return random_num, verified_random_num
