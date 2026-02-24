"""
Bagel: A deductive logic game where you must guess a number based on clues
CLI game similar to mastermind and wordle but with 3 numbers or more

Level: Beginner
What I Learned:
    Different style to python programming more easier to read but need to remember functions
    In if __name__ == "__main__" call main() only so imported can't run file
    Can convert everything to classes to be more organized but remember to use self parameter
    Don't import * just add the class and variables manually
    Rename variables using _ method instead of pascal or camel case
    while loop can be exited using break
    f strings can be replaced with .format() but I prefer f strings

    Placed ❤️ to different style of doing things
"""

import sys
from bagelGame import Game, guess_counter, MAX_GUESSES

def main():
    # TODO 1: Create a Game class to introduce game via def __init__(self) then call it
    game = Game()

    # TODO 2: Create a main game while loop and break it when player inputs no
    while True:                                 # Main game loop, use break to exit or use not game_over flag
        # TODO 3: Create global variable inside bagelGame.py to be used
        global guess_counter                    # Note: Get globals from bagelGame.py best place to put I think
        global MAX_GUESSES

        # TODO 3: Create a method to get secret number in Game class an assign it as secret_number
        secret_number = game.get_secret_number()

        # TODO 4: Create a inner loop to play game until lives/counter reaches destination and break when guess correct
        # remember to reset guess_counter to 1
        while guess_counter <= MAX_GUESSES:     # Note: Another while loop inside mainloop to not reset secret_number ❤️
            # TODO 5: Create a validate_guess method in Game class to check if answer is correct
            guess = ''                          # RESET if asked to continue to play game

            guess = game.validate_guess(guess)              # Validiate if input correct format

            # TODO 6: Create a get_clues method to give clues if answer not correct
            clues = game.get_clues(guess, secret_number)
            print(clues)
            guess_counter += 1

            if guess == secret_number:
                break                                       # Note: breaks from inner while loop if correct
            if guess_counter > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secret_number))

        guess_counter = 1                                   # RESET

        # Continue: Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):         # instead of input('> ').lower()[0] == 'y' ❤️
            break                                           # Note: breaks from outer while loop

    print('Thanks for playing!')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:               # ❤️ When Ctrl-C is pressed, end the program
        print()
        print('Thanks for running my app')
        sys.exit()