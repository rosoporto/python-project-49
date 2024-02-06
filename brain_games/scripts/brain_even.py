#!/usr/bin/env python3
import random
import prompt
from .cli import welcome_user


MAX_ROUNDS = 3
MIN_NUMBER = 1
MAX_NUMBER = 99


def parity_check(number):
    return "yes" if number % 2 == 0 else "no"


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    for i in range(MAX_ROUNDS):
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        print(f"Question: {random_number}")
        answer_user = prompt.string(prompt="Your answer: ")
        verified_number = parity_check(random_number)
        if answer_user == verified_number:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(. \
                Correct answer was '{verified_number}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
