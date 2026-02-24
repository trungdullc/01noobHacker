import sys

try:
    import bext                             # ❤️ pip3 install Bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

NUMBER_OF_LOGOS = 5  # (!) Try changing this to 1 or 100
PAUSE_AMOUNT = 0.2  # (!) Try changing this to 1.0 or 0.0
# (!) Try changing this list to fewer colors:
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT   = 'ur'
UP_LEFT    = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT  = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

# Key names for logo dictionaries, did this so look nicer
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

class DVD:
    def __init__(self):        
        # Set up the constants
        self.WIDTH, self.HEIGHT = bext.size()
        # Can't print to last column on Windows without it adding a newline automatically, so reduce width by one
        self.WIDTH -= 1