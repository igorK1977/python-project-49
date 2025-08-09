from random import randint

from brain_games.games.common import game_start


def game_play():
    data = []
    data.append('What is the result of the expression?')
    questions = []
    for question_number in range(3):
        number_1 = randint(1, 10)
        number_2 = randint(1, 10)
        question = []
        match question_number:
            case 0:
                question.append(f'Question: {number_1} + {number_2}')
                question.append(str(number_1 + number_2))
            case 1:
                question.append(f'Question: {number_1} - {number_2}')
                question.append(str(number_1 - number_2))
            case 2:
                question.append(f'Question: {number_1} * {number_2}')
                question.append(str(number_1 * number_2))                
        questions.append(question)
    data.append(questions)
    game_start(data)