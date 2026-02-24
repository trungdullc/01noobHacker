"""
Soroban Japanese Abacus

A simulation of a Japanese abacus calculator tool

Level: Intermediate
What I learned:
    TODO later, got to understand what program is doing
"""

from soroban import Abacus

def main():
    abacus = Abacus()

    abacusNumber = 0                        # This is the number represented on the abacus

    while True:                             # Main program loop
        abacus.displayAbacus(abacusNumber)
        abacus.displayControls()

        commands = input('> ').lower()

        if commands.startswith("q"):
            # Quit the program
            break
        elif commands.isdecimal():
            # Set the abacus number
            abacusNumber = int(commands)
        else:
            # Handle increment/decrement commands
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        # The abacus can't show negative numbers
        if abacusNumber < 0:
            abacusNumber = 0                    # Change any negative numbers to 0
        # The abacus can't show numbers larger than 9999999999
        if abacusNumber > 9999999999:
            abacusNumber = 9999999999

if __name__ == '__main__':
    main()