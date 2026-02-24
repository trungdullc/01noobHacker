"""
Twenty Forty-Eight

A sliding tile game to combine exponentially-increasing numbers.
Inspired by Gabriele Cirulli's 2048, which is a clone of Veewo Studios'
1024, which in turn is a clone of the Threes! game.

Level: Intermediate
What I learned:
    TODO later
"""

import sys
from game2048 import Game2048

def main():
    game = Game2048()
    gameBoard = game.getNewBoard()

    while True:                             # Main game loop
        game.drawBoard(gameBoard)
        print('Score:', game.getScore(gameBoard))
        playerMove = game.askForPlayerMove()
        gameBoard = game.makeMove(gameBoard, playerMove)
        game.addTwoToBoard(gameBoard)

        if game.isFull(gameBoard):
            game.drawBoard(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()