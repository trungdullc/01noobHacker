"""
Forest Fire Sim
A simulation of wildfires spreading in a forest. Press Ctrl-C to stop.

Level: Advance
What I learned:
    TODO Later
"""

from forestFire import ForestFire, EMPTY, GROW_CHANCE, FIRE, FIRE_CHANCE, TREE, PAUSE_LENGTH
import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

def main():
    ff = ForestFire()
    forest = ff.createNewForest()
    bext.clear()

    while True:                             # Main program loop
        ff.displayForest(forest)

        # Run a single simulation step
        nextForest = {'width': forest['width'],
                      'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in nextForest:
                    # If we've already set nextForest[(x, y)] on a
                    # previous iteration, just do nothing here
                    continue

                if ((forest[(x, y)] == EMPTY)
                    and (random.random() <= GROW_CHANCE)):
                    # Grow a tree in this empty space
                    nextForest[(x, y)] = TREE
                elif ((forest[(x, y)] == TREE)
                    and (random.random() <= FIRE_CHANCE)):
                    # Lightning sets this tree on fire
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    # This tree is currently burning
                    # Loop through all the neighboring spaces
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            # Fire spreads to neighboring trees
                            if forest.get((x + ix, y + iy)) == TREE:
                                nextForest[(x + ix, y + iy)] = FIRE
                    # The tree has burned down now, so erase it
                    nextForest[(x, y)] = EMPTY
                else:
                    # Just copy the existing object
                    nextForest[(x, y)] = forest[(x, y)]
        forest = nextForest

        time.sleep(PAUSE_LENGTH)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()