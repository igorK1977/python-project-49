import prompt


def game_start(data):
    game_task, questions = data
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_task)
    for question in questions:
        question_text, correct_answer = question
        print(question_text)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
