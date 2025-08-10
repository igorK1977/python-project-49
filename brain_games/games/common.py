import prompt


def game_start(game_task, questions):
    # Welcome user
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    # Game
    print(game_task)

    for question in questions:
        question_text, correct_answer = question
        print(question_text)

        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')

    print(f'Congratulations, {name}!')


NUMBER_OF_QUESTIONS = 3
