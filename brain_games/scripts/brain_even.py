from random import randint

import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for question in range(3):
        number = randint(1, 100)
        if number % 2 == 0:
            correct_answer = 'yes'
            incorrect_answer = 'no'
        else:
            correct_answer = 'no'
            incorrect_answer = 'yes'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
    return


if __name__ == "__main__":
    main()

