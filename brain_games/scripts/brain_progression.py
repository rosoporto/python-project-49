#!/usr/bin/env python3
import random
import prompt
from .cli import welcome_user


MAX_ROUNDS = 3
MIN_NUM = 1
MAX_NUM = 10


def generate_progression():
    start = random.randint(MIN_NUM, MAX_NUM)
    diff = random.randint(MIN_NUM, MAX_NUM / 2)
    progression = [start + diff * i for i in range(MAX_NUM)]
    hidden_index = random.randint(2, 7)
    hidden_num = progression[hidden_index]
    progression[hidden_index] = ".."
    str_progression = " ".join(list(map(str, progression)))
    return str_progression, hidden_num


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")
    for i in range(MAX_ROUNDS):
        progression, missing_num = generate_progression()
        print(f"Question: {progression}")
        answer_user = prompt.integer(prompt="Your answer: ")
        if answer_user == missing_num:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(. \
                Correct answer was '{missing_num}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
