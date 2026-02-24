"""
Tic-Tac-Toe

The classic board game.

Level: Beginner
What I learned:
    TODO later
"""

from tictactoe import TicTacToe, X, O

def main():
    game = TicTacToe()
    gameBoard = game.getBlankBoard()             # Create a TTT board dictionary
    currentPlayer, nextPlayer = X, O        # X goes first, O goes next

    while True:                             # Main game loop
        # Display the board on the screen
        print(game.getBoardStr(gameBoard))

        # Keep asking the player until they enter a number 1-9
        move = None
        while not game.isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input('> ')
        game.updateBoard(gameBoard, move, currentPlayer)     # Make the move

        # Check if the game is over
        if game.isWinner(gameBoard, currentPlayer):          # Check for a winner
            print(game.getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif game.isBoardFull(gameBoard):                    # Check for a tie
            print(game.getBoardStr(gameBoard))
            print('The game is a tie!')
            break
        # Switch turns to the next player
        currentPlayer, nextPlayer = nextPlayer, currentPlayer
    print('Thanks for playing!')

if __name__ == '__main__':
    main()