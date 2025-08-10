from random import randint

from brain_games.games.common import NUMBER_OF_QUESTIONS, game_start


def create_progression():
    """
    Creates an arithmetic progression based on progression constants.

    Returns:
        list: progression elements in str format.
    """
    # Progression constants
    MIN_LENGTH = 5
    MAX_LENGTH = 10
    MIN_STEP = 1
    MAX_STEP = 10
    MIN_START = 1
    MAX_START = 10
    
    # Defining progression parameters
    progression_length = randint(MIN_LENGTH, MAX_LENGTH)
    progression_step = randint(MIN_STEP, MAX_STEP)
    progression_start = randint(MIN_START, MAX_START)

    # Make result
    result = []
    for index in range(progression_length):
        result.append(str(progression_start + index * progression_step))
    return result


def game_play():
    """
    Defining game_task and questions for game

    Launching the game engine with parameters:
        str : game_task
        list: elements consist of the text question and the correct answer.
    """
    # Defining game parameters
    game_task = 'What number is missing in the progression?'
    questions = []
    for _ in range(NUMBER_OF_QUESTIONS):
        progression = create_progression()
        hidden_item_number = randint(1, len(progression)) - 1
        correct_answer = progression[hidden_item_number]
        progression[hidden_item_number] = '..'
        question_text = f'Question: {' '.join(progression)}'
        question = [question_text, correct_answer]            
        questions.append(question)

    # Launching the game engine
    game_start(game_task, questions)
