"""
Guess the Number
Try to guess the secret number based on hints

Level: Beginner
What I learned:
    Nothing
"""

import random

NUMBER_OF_GUESSES = 10

def askForGuess():
    while True:
        guess = input('> ')

        if guess.isdecimal():
            return int(guess)                                   # return escapes while loop if inside a fx vs break, continue, sys.exit()
        print('Please enter a number between 1 and 100.')

def main():
    print('Guess the Number\n')
    secretNumber = random.randint(1, 100)
    print('I am thinking of a number between 1 and 100.')

    for i in range(NUMBER_OF_GUESSES):
        print('You have {} guesses left. Take a guess.'.format(NUMBER_OF_GUESSES - i))

        guess = askForGuess()

        if guess == secretNumber:
            break                               # Break out of the for loop if the guess is correct.

        # Offer a hint
        if guess < secretNumber:
            print('Your guess is too low.')
        elif guess > secretNumber:
            print('Your guess is too high.')

    # Reveal the results
    if guess == secretNumber:
        print('Yay! You guessed my number!')
    else:
        print('Game over. The number I was thinking of was', secretNumber)

if __name__ == "__main__":
    main()