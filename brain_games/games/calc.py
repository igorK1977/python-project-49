from random import randint

from brain_games.games.common import NUMBER_OF_QUESTIONS, game_start


def game_play():
    """
    Defining game_task and questions for game

    Launching the game engine with parameters:
        str : game_task
        list: elements consist of the text question and the correct answer.
    """    
    MIN_NUMBER = 1
    MAX_NUMBER = 50

    # Defining game parameters
    game_task = 'What is the result of the expression?'
    questions = []
    for question_number in range(NUMBER_OF_QUESTIONS):
        number_1 = randint(MIN_NUMBER, MAX_NUMBER)
        number_2 = randint(MIN_NUMBER, MAX_NUMBER)
        match question_number:
            case 0:
                question_text = f'Question: {number_1} + {number_2}'
                correct_answer = str(number_1 + number_2)
            case 1:
                question_text = f'Question: {number_1} - {number_2}'
                correct_answer = str(number_1 - number_2)
            case 2:
                question_text = f'Question: {number_1} * {number_2}'
                correct_answer = str(number_1 * number_2)
        question = [question_text, correct_answer]       
        questions.append(question)

    # Launching the game engine    
    game_start(game_task, questions)