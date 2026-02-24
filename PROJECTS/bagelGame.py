import random

NUM_DIGITS = 3                          # 1 to 10
MAX_GUESSES = 10                        # 1 to 100

guess_counter = 1

class Game:
    def __init__(self):                                         # Note: No need for def __str__()
        print('''Bagels, a deductive logic game.

I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:    That means:
  Pico         One digit is correct but in the wrong position
  Fermi        One digit is correct and in the right position
  Bagels       No digit is correct

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    def get_secret_number(self):
        """Returns a string made up of NUM_DIGITS unique random digits."""
        global NUM_DIGITS
        global MAX_GUESSES
        
        secret_number = ''

        numbers:list[str] = list('0123456789')
        random.shuffle(numbers)                     # ['3', '6', '1', '2', '4', '9', '0', '5', '8', '7']

        # Note: This logic makes it so that the secret_number is unique numbers only
        for i in range(NUM_DIGITS):                 # Note: Dynamic Coding so can pick more than 3 digits but limits to 10
            secret_number += str(numbers[i])
        
        print(f"DEBUG: Secret Number: {secret_number}")

        print('I have thought up a number.')
        print(' You have {} guesses to get it.'.format(MAX_GUESSES))
        return secret_number

    def get_clues(self, guess, secret_number):
        """Returns a string with the pico, fermi, bagels clues for a guess
        and secret number pair."""
        if guess == secret_number:
            return 'You got it!'

        clues = []

        for i in range(len(guess)):
            if guess[i] == secret_number[i]:        # A correct digit is in the correct place use == secret_number[i]
                clues.append('Fermi')
            elif guess[i] in secret_number:         # A correct digit is in the incorrect place use in
                clues.append('Pico')

        if len(clues) == 0:
            return 'Bagels'                         # There are no correct digits at all, do seperate or else many output
        else:
            # Sort the clues so doesn't give info away unless programming Wordle or Mastermind
            clues.sort()
            return ' '.join(clues)                  # typecast to string from list

    def validate_guess(self, guess):
        global guess_counter

        while len(guess) != NUM_DIGITS or not guess.isdecimal():    # Note: How python validiates input ❤️
            print('Guess #{}: '.format(guess_counter))
            guess = input('> ')
        return guess