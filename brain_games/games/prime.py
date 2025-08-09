from random import randint

from brain_games.games.common import game_start


def is_prime(number):
    if number < 2:
        return False
    divider = 2
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
    return True


def game_play():
    data = []
    data.append('Answer "yes" if given number is prime. Otherwise answer "no".')
    questions = []
    for _ in range(3):
        number = randint(1, 20)
        question = []
        question.append(f'Question: {number}')
        if is_prime(number):
            question.append('yes')     
        else:
            question.append('no')          
        questions.append(question)
    data.append(questions)
    game_start(data)
