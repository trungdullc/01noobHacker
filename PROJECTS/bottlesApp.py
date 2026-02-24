"""
Ninety-Nine Bottles of Milk on the Wall

Print the full lyrics to one of the longest songs ever! Press
Ctrl-C to stop.

Level: Beginner
What I learned:
    When moving local variable out to global need use global keyword
"""

import sys, time

bottles = 99                                # This is the starting number of bottles
PAUSE = 2                                   # (!) Try changing this to 0 to see the full song at once

def main():
    global bottles, PAUSE
    print('Ninety-Nine Bottles\nPress Ctrl-C to quit.)')

    time.sleep(2)

    try:
        while bottles > 1:                  # Keep looping and display the lyrics
            print(bottles, 'bottles of milk on the wall,')
            time.sleep(PAUSE)               # Pause for PAUSE number of seconds
            print(bottles, 'bottles of milk,')
            time.sleep(PAUSE)
            print('Take one down, pass it around,')
            time.sleep(PAUSE)
            bottles = bottles - 1           # Decrease the number of bottles by one
            print(bottles, 'bottles of milk on the wall!')
            time.sleep(PAUSE)
            print()

        # Display the last stanza
        print('1 bottle of milk on the wall,')
        time.sleep(PAUSE)
        print('1 bottle of milk,')
        time.sleep(PAUSE)
        print('Take it down, pass it around,')
        time.sleep(PAUSE)
        print('No more bottles of milk on the wall!')
    except KeyboardInterrupt:
        sys.exit()

if __name__ == "__main__":
    main()