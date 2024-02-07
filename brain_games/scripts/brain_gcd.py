#!/usr/bin/env python3
import random
import prompt
from .cli import welcome_user


MAX_ROUNDS = 3
MIN_NUM = 1
MAX_NUM = 100


def find_gcd(first_num, second_num):
    while second_num:
        first_num, second_num = second_num, first_num % second_num
    return first_num


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    for i in range(MAX_ROUNDS):
        first_num = random.randint(MIN_NUM, MAX_NUM)
        second_num = random.randint(MIN_NUM, MAX_NUM)
        print(f"Question: {first_num} {second_num}")
        answer_user = prompt.integer(prompt="Your answer: ")
        gcd_num = find_gcd(first_num, second_num)
        if answer_user == gcd_num:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(. \
                Correct answer was '{gcd_num}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
