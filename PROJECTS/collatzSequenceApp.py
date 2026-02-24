"""
Collatz Sequence
Generates numbers for the Collatz sequence, given a starting number
# Note: Lots of leetcode have sequences like fibonacci sequence and others

Level: Beginner
What I learned:
    time.sleep(0.1) is like bash way to do sleep() to pause before next output
"""

import sys, time

def main():
    print('''Collatz Sequence, or, the 3n + 1 Problem

    The Collatz sequence is a sequence of numbers produced from a starting
    number n, following three rules:

    1) If n is even, the next number n is n / 2
    2) If n is odd, the next number n is n * 3 + 1
    3) If n is 1, stop. Otherwise, repeat

    It is generally thought, but so far not mathematically proven, that
    every starting number eventually terminates at 1.
    ''')

    # Get input and assign as response
    response = input('Enter a starting number (greater than 0) or QUIT:\n> ')

    # Checks if response is valid, not done in while loop just exit game if wront input
    if not response.isdecimal() or response == '0':
        print('You must enter an integer greater than 0.')
        sys.exit()

    my_number = int(response)
    print(my_number, end='', flush=True)

    while my_number != 1:                       # Because end is 1
        if my_number % 2 == 0:                  # If even divide by 2
            my_number = my_number // 2
        else:                                   # Otherwise multiply by 3 and add 1
            my_number = 3 * my_number + 1

        print(', ' + str(my_number), end='', flush=True)
        time.sleep(0.1)                         # ❤️
    print()

if __name__ == "__main__":
    main()