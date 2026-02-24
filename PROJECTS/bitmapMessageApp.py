"""
Bitmap Message
Displays a text message according to the provided bitmap image

Level: Beginner
What I learned:
    sys module for sys.exit() vs return(0) in C/C++
    builtins.str.splitlines() to convert your long ass str into list[str]
"""

import sys

def main():
    try:
        with open("data/worldmap.txt", mode="r") as file:
            bitmap = file.read()                # Instead of bitmap = """ """, need learn external files and read() vs readlines()
    except FileNotFoundError:
        print("worldmap.txt not exist, create it and use * only or program not work correctly")
    else:
        print('Bitmap Message')
        print('Enter the message to display with the bitmap')
        message = input('> ')

        if message == '':                                           # if message is empty exit program
            sys.exit()                                              # ❤️

        # Main logic to program
        for line in bitmap.splitlines(keepends=False):              # Loop over each line in the bitmap using .splitlines() -> list[str] ❤️❤️❤️❤️❤️
            for index, char in enumerate(line):                     # Loop over each character in the line
                if char == ' ':
                    print(' ', end='')                              # Print an empty space since there's a space in the bitmap
                else:
                    print(message[index % len(message)], end='')    # Print a character from the message ❤️❤️❤️❤️❤️
            print()
    finally:
        print("Program reach end")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:               # ❤️ When Ctrl-C is pressed, end the program
        print()
        print('Thanks for running my app')
        sys.exit()