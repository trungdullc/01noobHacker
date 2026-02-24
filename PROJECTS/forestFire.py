import random, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

WIDTH = 79
HEIGHT = 22

TREE = 'A'
FIRE = 'W'
EMPTY = ' '

# (!) Try changing these settings to anything between 0.0 and 1.0
INITIAL_TREE_DENSITY = 0.20         # Amount of forest that starts with trees
GROW_CHANCE = 0.01                  # Chance a blank space turns into a tree
FIRE_CHANCE = 0.01                  # Chance a tree is hit by lightning & burns

# (!) Try setting the pause length to 1.0 or 0.0
PAUSE_LENGTH = 0.5

class ForestFire:
    def createNewForest(self):
        """Returns a dictionary for a new forest data structure."""
        forest = {'width': WIDTH, 'height': HEIGHT}

        for x in range(WIDTH):
            for y in range(HEIGHT):
                if (random.random() * 100) <= INITIAL_TREE_DENSITY:
                    forest[(x, y)] = TREE  # Start as a tree.
                else:
                    forest[(x, y)] = EMPTY  # Start as an empty space.
        return forest

    def displayForest(self, forest):
        """Display the forest data structure on the screen."""
        bext.goto(0, 0)
        for y in range(forest['height']):
            for x in range(forest['width']):
                if forest[(x, y)] == TREE:
                    bext.fg('green')
                    print(TREE, end='')
                elif forest[(x, y)] == FIRE:
                    bext.fg('red')
                    print(FIRE, end='')
                elif forest[(x, y)] == EMPTY:
                    print(EMPTY, end='')
            print()
        bext.fg('reset')  # Use the default font color.
        print('Grow chance: {}%  '.format(GROW_CHANCE * 100), end='')
        print('Lightning chance: {}%  '.format(FIRE_CHANCE * 100), end='')
        print('Press Ctrl-C to quit.')