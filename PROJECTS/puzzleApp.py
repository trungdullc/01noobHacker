"""
Sliding Tile Puzzle

Slide the numbered tiles into the correct order.

Level: Intermediate
What I learned:
    TODO later
"""

import sys
from puzzle import Puzzle

def main():
    puzzle = Puzzle()
    gameBoard = puzzle.getNewPuzzle()

    while True:
        puzzle.displayBoard(gameBoard)
        playerMove = puzzle.askForPlayerMove(gameBoard)
        puzzle.makeMove(gameBoard, playerMove)

        if gameBoard == puzzle.getNewBoard():
            print('You won!')
            sys.exit()

if __name__ == '__main__':
    main()