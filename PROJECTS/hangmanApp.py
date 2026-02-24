"""
Hangman
Guess the letters to a secret word before the hangman is drawn.

Level: Beginner
What I learned:
    [r]aw string instead of [f]ormatted string
    WORD_LIST = "dog cat duck".split()
"""

import random, sys
from hangman import Hangman, WORDS, HANGMAN_PICS

def main():
    hangman = Hangman()

    missedLetters = []                          # List of incorrect letter guesses
    correctLetters = []                         # List of correct letter guesses
    secretWord = random.choice(WORDS)           # The word the player must guess

    while True:
        hangman.drawHangman(missedLetters, correctLetters, secretWord)

        # Let the player enter their letter guess
        guess = hangman.getPlayerGuess(missedLetters + correctLetters)

        if guess in secretWord:
            # Add the correct guess to correctLetters
            correctLetters.append(guess)

            # Check if the player has won
            foundAllLetters = True              # Start off assuming they've won
            for secretWordLetter in secretWord:
                if secretWordLetter not in correctLetters:
                    # There's a letter in secret word that isn't yet in correctLetters, so player hasn't won
                    foundAllLetters = False
                    break

            if foundAllLetters:
                print('Yes! The secret word is:', secretWord)
                print('You have won!')
                break                           # Break out of the main game loop
        else:
            # The player has guessed incorrectly
            missedLetters.append(guess)

            # Check if player has guessed too many times and lost. (The
            # "- 1" is because we don't count the empty gallows in HANGMAN_PICS)
            if len(missedLetters) == len(HANGMAN_PICS) - 1:
                hangman.drawHangman(missedLetters, correctLetters, secretWord)
                print('You have run out of guesses!')
                print('The word was "{}"'.format(secretWord))
                break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()