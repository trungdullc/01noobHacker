"""
Sound Mimic

A pattern-matching game with sounds. Try to memorize an increasingly
longer and longer pattern of letters. Inspired by the electronic game,
Simon.

Level: Beginner
What I learned:
    compatibility issue of playsound with playsound (the old package) fails to build on Python 3.11+
    Need to use: pip3 install playsound==1.2.2 ❤️
    TODO later
"""

import random, sys, time, os

try:
    import playsound
except ImportError:
    print("The 'playsound' module is not installed.")
    print('The playsound module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip3 install playsound')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install playsound')
    choice = input("Install it now using pip3? (y/n): ").strip().lower()

    if not choice.startswith('y'):
        print("Exiting program.")
        sys.exit()

    # attempt installation
    os.system("pip3 install install playsound==1.2.2")
    print("Please rerun python program")

def main():
    print('''Sound Mimic
    Try to memorize a pattern of A S D F letters (each with its own sound)
    as it gets longer and longer.''')

    input('Press Enter to begin...')

    pattern = ''

    while True:
        print('\n' * 60)                                    # Clear the screen by printing several newlines

        # Add a random letter to the pattern
        pattern = pattern + random.choice('ASDF')

        # Display the pattern (and play their sounds)
        print('Pattern: ', end='')
        for letter in pattern:
            print(letter, end=' ', flush=True)
            playsound.playsound('sounds/' + 'sound' + letter + '.wav')

        time.sleep(1)                               # Add a slight pause at the end
        print('\n' * 60)                            # Clear the screen by printing several newlines

        # Let the player enter the pattern
        print('Enter the pattern:')
        response = input('> ').upper()

        if response != pattern:
            print('Incorrect!')
            print('The pattern was', pattern)
        else:
            print('Correct!')

        for letter in pattern:
            playsound.playsound('sounds/' + 'sound' + letter + '.wav')

        if response != pattern:
            print('You scored', len(pattern) - 1, 'points.')
            print('Thanks for playing!')
            break

        time.sleep(1)

if __name__ == "__main__":
    main()