from random import randint

from brain_games.games.common import game_start


def game_play():
    data = []
    data.append('Answer "yes" if the number is even, otherwise answer "no".')
    questions = []
    for _ in range(3):
        number = randint(1, 100)
        question = []
        question.append(f'Question: {number}')
        if number % 2 == 0:
            question.append('yes')
        else:
            question.append('no')
        questions.append(question)
    data.append(questions)
    game_start(data)
