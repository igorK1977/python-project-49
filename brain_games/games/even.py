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
    game_task = 'Answer "yes" if the number is even, otherwise answer "no".'
    questions = []
    for _ in range(NUMBER_OF_QUESTIONS):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        question_text = f'Question: {number}'
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        question = [question_text, correct_answer]   
        questions.append(question)

    # Launching the game engine    
    game_start(game_task, questions)
