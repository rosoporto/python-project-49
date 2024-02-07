#!/usr/bin/env python3
import random
import prompt
from .cli import welcome_user


MAX_ROUNDS = 3
MIN_NUM = 1
MAX_NUM = 99


def parity_check(num):
    return "yes" if num % 2 == 0 else "no"


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(MAX_ROUNDS):
        random_num = random.randint(MIN_NUM, MAX_NUM)
        print(f"Question: {random_num}")
        answer_user = prompt.string(prompt="Your answer: ")
        verified_num = parity_check(random_num)
        if answer_user == verified_num:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(. \
                Correct answer was '{verified_num}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
