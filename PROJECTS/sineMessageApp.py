"""
Sine Message

Create a sine-wavy message.

Level: Beginner
What I learned:
    Using sin with padding
    shutil module used to get terminal size
"""

import math, shutil, sys, time

WIDTH, HEIGHT = shutil.get_terminal_size()
# We can't print to the last column on Windows without it adding a newline automatically, so reduce the width by one
WIDTH -= 1

def main():
    print('Sine Message')
    print('(Press Ctrl-C to quit.\n)')
    print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')

    while True:
        message = input('> ')
        if 1 <= len(message) <= (WIDTH // 2):
            break
        print('Message must be 1 to', WIDTH // 2, 'characters long.')


    step = 0.0                          # "step" determines how far into the sine wave we are
    # Sine goes from -1.0 to 1.0, so we need to change it by a multiplier
    multiplier = (WIDTH - len(message)) / 2

    try:
        while True:                                             # Main program loop
            sinOfStep = math.sin(step)
            padding = ' ' * int((sinOfStep + 1) * multiplier)   # ❤️
            print(padding + message)
            time.sleep(0.1)
            step += 0.25                                        # (!) Try changing this to 0.1 or 0.5 ❤️
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()