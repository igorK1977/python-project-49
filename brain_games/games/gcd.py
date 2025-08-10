from random import randint

from brain_games.games.common import NUMBER_OF_QUESTIONS, game_start


def gcd(number_1, number_2):
    while number_2 != 0:
        (number_1, number_2) = (number_2, number_1 % number_2)
    return number_1


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
    game_task = 'Find the greatest common divisor of given numbers.'
    questions = []
    for _ in range(NUMBER_OF_QUESTIONS):
        number_1 = randint(MIN_NUMBER, MAX_NUMBER)
        number_2 = randint(MIN_NUMBER, MAX_NUMBER)
        question_text = f'Question: {number_1} {number_2}'
        correct_answer = str(gcd(number_1, number_2)) 
        question = [question_text, correct_answer]                
        questions.append(question)

    # Launching the game engine    
    game_start(game_task, questions)
