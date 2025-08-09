from random import randint

from brain_games.games.common import game_start


def gcd(number_1, number_2):
    while number_2 != 0:
        (number_1, number_2) = (number_2, number_1 % number_2)
    return number_1


def game_play():
    data = []
    data.append('Find the greatest common divisor of given numbers.')
    questions = []
    for question_number in range(3):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        question = []
        question.append(f'Question: {number_1} {number_2}')
        question.append(str(gcd(number_1, number_2)))               
        questions.append(question)
    data.append(questions)
    game_start(data)
