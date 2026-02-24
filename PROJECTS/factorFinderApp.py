"""
Factor Finder
Finds all the factors of a number
Note: If factor is 1 and the number it is called a prime number ⭐

Level: Beginner
What I learned:
    math module
    Brute Force finding prime is get range of 1 to square root + 1
"""

import math, sys

def main():
    print('''

    A number's factors are two numbers that, when multiplied with each
    other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
    factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
    say that 26 has four factors: 1, 2, 13, and 26.

    If a number only has two factors (1 and itself), we call that a prime
    number. Otherwise, we call it a composite number.

    Can you discover some prime numbers?
    ''')

    while True:                                 # Main program loop
        print('Enter a positive whole number to factor (or QUIT):')
        response = input('> ')

        if response.upper().startswith("Q"):
            sys.exit()

        if not (response.isdecimal() and int(response) > 0):
            continue
        number = int(response)

        factors = []

        # Find the factors of number
        # Note: going from range 1 to number takes to long can half it by going to square root + 1 is range excludes it ❤️
        # Example: 81
        # 1, 3, 9, 27, 81
        for i in range(1, int(math.sqrt(number)) + 1):          # Brute Force Method
            if number % i == 0:                                 # If there's no remainder, it is a factor
                factors.append(i)
                factors.append(number // i)                     # 1, 81 3, 27, 9, 9

        # Convert to a set to get rid of duplicate factors
        factors = list(set(factors))                            # Reason to convert to set to remove duplicates
        factors.sort()                                          # Sort so goes in right order

        # Display the results
        for i, factor in enumerate(factors):
            factors[i] = str(factor)
        print(', '.join(factors))

if __name__ == "__main__":
    main()