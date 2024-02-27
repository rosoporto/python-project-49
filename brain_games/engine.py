import prompt
from brain_games.cli import welcome_user


MAX_ROUNDS = 3


def launch_game(game_module):
    name = welcome_user()
    print(game_module.RULE)
    for _ in range(MAX_ROUNDS):
        guestion, correct_answer = game_module.prepare_question_answer()
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
