"""Flooder
A colorful game where you try to fill the board with a single color. Has
a mode for colorblind players.
Inspired by the "Flood It!" game.

Level: Advanced
What I learned:
    TODO Later very interesting CLI game using bext
"""

from flooder import Flooder, SHAPE_MODE, COLOR_MODE, MOVES_PER_GAME
import sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    flooder = Flooder()
    print('''Flooder

Set the upper left color/shape, which fills in all the
adjacent squares of that color/shape. Try to make the
entire board the same colo
r/shape.''')

    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = flooder.getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:                                 # Main game loop
        flooder.displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = flooder.askForPlayerMove(displayMode)
        flooder.changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if flooder.hasWon(gameBoard):
            flooder.displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            flooder.displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break

if __name__ == '__main__':
    main()