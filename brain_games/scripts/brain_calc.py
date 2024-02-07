#!/usr/bin/env python3
import random
import prompt
from .cli import welcome_user


MAX_ROUNDS = 3
MIN_NUM = 1
MAX_NUM = 9


def calculation(math_operation):
    first_num = random.randint(MAX_NUM, MAX_NUM * 2)
    second_num = random.randint(MIN_NUM, MAX_NUM)
    result = None
    match math_operation:
        case "+":
            print(f"Question: {first_num} + {second_num}")
            result = first_num + second_num
        case "-":
            print(f"Question: {first_num} - {second_num}")
            result = first_num - second_num
        case "*":
            print(f"Question: {first_num} * {second_num}")
            result = first_num * second_num
        case _:
            print("Other")
    return result


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What is the result of the expression?")
    math_operations = ["+", "-", "*"]
    for i in range(MAX_ROUNDS):
        math_operation = random.choice(math_operations)
        result_math_operation = calculation(math_operation)
        answer_user = prompt.integer(prompt="Your answer: ")
        if result_math_operation == answer_user:
            print("Correct!")
        else:
            print(f"'{answer_user}' is wrong answer ;(.\
                Correct answer was '{result_math_operation}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()