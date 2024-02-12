import prompt
from brain_games.cli import welcome_user
from brain_games.const import MAX_ROUNDS


def launch_game(get_guestion_and_answer, instruction):
    name = welcome_user()
    print(instruction)
    for _ in range(MAX_ROUNDS):
        guestion, correct_answer = get_guestion_and_answer()
        print(f"Question: {guestion}")
        user_reply = prompt.string(prompt="Your answer: ")
        if user_reply == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_reply}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
