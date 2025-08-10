from random import randint

from brain_games.games.common import NUMBER_OF_QUESTIONS, game_start


def is_prime(number):
    MIN_PRIME_NUMBER = 2
    if number < MIN_PRIME_NUMBER:
        return False
    divider = MIN_PRIME_NUMBER
    while divider < number:
        if number % divider == 0:
            return False
        divider += 1
    return True


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
    game_task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    questions = []
    for _ in range(NUMBER_OF_QUESTIONS):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        question_text = f'Question: {number}'
        if is_prime(number):
            correct_answer = 'yes'   
        else:
            correct_answer = 'no'  
        question = [question_text, correct_answer]   
        questions.append(question)

    # Launching the game engine    
    game_start(game_task, questions)
