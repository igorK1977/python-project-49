from random import randint

from brain_games.games.common import game_start


def create_progression():
    result = []
    progression_length = randint(5, 10)
    progression_step = randint(2, 10)
    progression_start = randint(1, 7)
    for index in range(progression_length):
        result.append(str(progression_start + index * progression_step))
    return result


def game_play():
    data = []
    data.append('What number is missing in the progression?')
    questions = []
    for _ in range(3):
        progression = create_progression()
        task = ' '.join(progression)
        hidden_item = randint(1, len(progression)) - 1
        task = task.replace(progression[hidden_item], '..')
        question = []
        question.append(f'Question: {task}')
        question.append(progression[hidden_item])               
        questions.append(question)
    data.append(questions)
    game_start(data)
