"""
Numeral System Counters
Shows equivalent numbers in decimal, hexadecimal, and binary.

Level: Beginner
What I learned:
    int type casting to hex or binary
    hex()
    bin()
"""

def main():
    print('''Numeral System Counters

    This program shows you equivalent numbers in decimal (base 10),
    hexadecimal (base 16), and binary (base 2) numeral systems.

    (Ctrl-C to quit.)
    ''')

    # Validate response
    while True:
        response = input('Enter the starting number (e.g. 0) > ')

        if response == '':
            response = '0'                          # Start at 0 by default
            break
        if response.isdecimal():
            break
        print('Please enter a number greater than or equal to 0')
    start = int(response)

    while True:
        response = input('Enter how many numbers to display (e.g. 1000) > ')

        if response == '':
            response = '1000'                       # Display 1000 numbers by default
            break
        if response.isdecimal():
            break
        print('Please enter a number.')
    amount = int(response)

    for number in range(start, start + amount):     # Main program loop
        # Convert to hexadecimal/binary and remove the prefix
        hexNumber = hex(number)[2:].upper()         # hex type cast ❤️
        binNumber = bin(number)[2:]                 # binary type cast ❤️

        print('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber)

if __name__ == "__main__":
    main()