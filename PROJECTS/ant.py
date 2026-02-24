import sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

WIDTH, HEIGHT = bext.size()
# We can't print to the last column on Windows without it adding a newline automatically, so reduce the width by one
WIDTH -= 1
HEIGHT -= 1                         # Adjustment for the quit message at the bottom

NUMBER_OF_ANTS = 10                 # (!) Try changing this to 1 or 50
PAUSE_AMOUNT = 0.1                  # (!) Try changing this to 1.0 or 0.0

# (!) Try changing these to make the ants look different
ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'

# (!) Try changing these colors to one of 'black', 'red', 'green',
# 'yellow', 'blue', 'purple', 'cyan', or 'white'. (These are the only
# colors that the bext module supports.)
ANT_COLOR = 'red'
BLACK_TILE = 'black'
WHITE_TILE = 'white'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

class Ant:
    def displayBoard(self, board, ants, changedTiles):
        """Displays the board and ants on the screen. The changedTiles
        argument is a list of (x, y) tuples for tiles on the screen that
        have changed and need to be redrawn"""

        # Draw the board data structure
        for x, y in changedTiles:
            bext.goto(x, y)
            if board.get((x, y), False):
                bext.bg(BLACK_TILE)
            else:
                bext.bg(WHITE_TILE)

            antIsHere = False

            for ant in ants:
                if (x, y) == (ant['x'], ant['y']):
                    antIsHere = True

                    if ant['direction'] == NORTH:
                        print(ANT_UP, end='')
                    elif ant['direction'] == SOUTH:
                        print(ANT_DOWN, end='')
                    elif ant['direction'] == EAST:
                        print(ANT_LEFT, end='')
                    elif ant['direction'] == WEST:
                        print(ANT_RIGHT, end='')
                    break

            if not antIsHere:
                print(' ', end='')

        # Display the quit message at the bottom of the screen
        bext.goto(0, HEIGHT)
        bext.bg(WHITE_TILE)
        print('Press Ctrl-C to quit.', end='')

        sys.stdout.flush()              # (Required for bext-using programs)
        time.sleep(PAUSE_AMOUNT)