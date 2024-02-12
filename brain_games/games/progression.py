#!/usr/bin/env python3
from random import randint
from brain_games.engine import launch_game
from brain_games.const import MIN_NUM, MAX_NUM_PROGRESSION
from brain_games.const import INSTRUCTION_FOR_PROGRESSION_GAME


def generate_progression():
    start = randint(MIN_NUM, MAX_NUM_PROGRESSION)
    diff = randint(MIN_NUM, MAX_NUM_PROGRESSION / 2)
    progression = [start + diff * i for i in range(MAX_NUM_PROGRESSION)]
    hidden_index = randint(2, 7)
    missing_num = progression[hidden_index]
    progression[hidden_index] = ".."
    str_progression = " ".join(list(map(str, progression)))
    return str_progression, str(missing_num)


def run_even_game():
    launch_game(generate_progression, INSTRUCTION_FOR_PROGRESSION_GAME)
