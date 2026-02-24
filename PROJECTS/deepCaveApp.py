"""
Deep Cave
An animation of a deep cave that goes forever into the earth

Level: Beginner
What I learned:
    Nothing
"""

import random, sys, time

WIDTH = 70                      # (!) Try changing this to 10 or 30.
PAUSE_AMOUNT = 0.05             # (!) Try changing this to 0 or 1.0.

left_width = 20
gap_width = 10

def main():
    global left_width
    global gap_width

    print('Press Ctrl-C to stop')
    time.sleep(2)

    while True:
        # Display the tunnel segment:
        right_width = WIDTH - gap_width - left_width
        print(('#' * left_width) + (' ' * gap_width) + ('#' * right_width))

        # Check for Ctrl-C press during the brief pause
        try:
            time.sleep(PAUSE_AMOUNT)
        except KeyboardInterrupt:
            sys.exit()

        # Adjust the left side width (Main way to change left_width)
        diceRoll = random.randint(1, 6)
        if diceRoll == 1 and left_width > 1:
            left_width = left_width - 1           # Decrease left side width by 1
        elif diceRoll == 2 and left_width + gap_width < WIDTH - 1:
            left_width = left_width + 1           # Increase left side widthby 1
        else:
            pass                                # Do nothing; no change in left side width

if __name__ == "__main__":
    main()