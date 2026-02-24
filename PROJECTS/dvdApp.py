"""
Bouncing DVD Logo
A bouncing DVD logo animation. You have to be "of a certain age" to appreciate this
Press Ctrl-C to stop

NOTE: Do not resize the terminal window while this program is running.

Level: Intermediate
What I learned:
    Use try when importing external modules
    Bext module like turtle but for terminal
"""

import sys, random, time

try:
    import bext                             # ❤️ pip3 install Bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

from dvd import DVD, NUMBER_OF_LOGOS, PAUSE_AMOUNT, COLORS, UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT, DIRECTIONS, COLOR, X, Y, DIR

def main():
    bext.clear()                        # Go to Definition uses colorama and other modules ❤️

    dvd = DVD()

    # Generate some logos
    logos = []

    for _ in range(NUMBER_OF_LOGOS):
        # Note: Data Structure of logos is list[dict[str, str | int]]
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, dvd.WIDTH - 4),
                      Y: random.randint(1, dvd.HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            logos[-1][X] -= 1       # Make sure X is even so it can hit the corner

    corner_bounces = 0              # Count how many times a logo hits a corner

    while True:                     # Main program loop
        for logo in logos:          # Handle each logo in the logos list
            # Erase the logo's current location
            bext.goto(logo[X], logo[Y])
            print('   ', end='')    # (!) Try commenting this line out

            originalDirection = logo[DIR]

            # See if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == dvd.HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif logo[X] == dvd.WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif logo[X] == dvd.WIDTH - 3 and logo[Y] == dvd.HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounces += 1

            # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge
            # (WIDTH - 3 because 'DVD' has 3 letters)
            elif logo[X] == dvd.WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == dvd.WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge
            elif logo[Y] == dvd.HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == dvd.HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != originalDirection:
                logo[COLOR] = random.choice(COLORS)     # Change color when the logo bounces

            # Move the logo (X moves by 2 because the terminal characters are twice as tall as wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        # Display number of corner bounces
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', corner_bounces, end='')

        for logo in logos:
            # Draw the logos at their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()                                  # Required for bext-using programs
        time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:                               # ❤️ When Ctrl-C is pressed, end the program
        print()
        print('Bouncing DVD Logo')
        sys.exit()