#!/usr/bin/env python3
import random
import prompt
from .cli import welcome_user


MAX_ROUNDS = 3
MIN_NUM = 2
MAX_NUM = 1000


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "no"
    return "yes"


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    for i in range(MAX_ROUNDS):
        random_num = random.randint(MIN_NUM, MAX_NUM)
        print(f"Question: {random_num}")
        check_num = is_prime(random_num)
        answer_user = prompt.string(prompt="Your answer: ")
        if answer_user == check_num:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(. \
                Correct answer was '{check_num}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
