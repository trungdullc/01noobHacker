"""
Sudoku Puzzle

The classic 9x9 number placement puzzle

Level: Intermediate
What I learned:
    TODO later
"""

import random, sys
from sudokugrid import SudokuGrid

def main():
    # Load the sudokupuzzles.txt file
    with open('data/sudokupuzzles.txt') as puzzleFile:
        puzzles = puzzleFile.readlines()

    # Remove the newlines at the end of each puzzle
    for i, puzzle in enumerate(puzzles):
        puzzles[i] = puzzle.strip()

    grid = SudokuGrid(random.choice(puzzles))

    while True:                             # Main game loop
        grid.display()

        # Check if the puzzle is solved
        if grid.isSolved():
            print('Congratulations! You solved the puzzle!')
            print('Thanks for playing!')
            sys.exit()

        # Get the player's action
        while True:                     # Keep asking until the player enters a valid action
            print()
            print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
            print('(For example, a move looks like "B4 9".)')

            action = input('> ').upper().strip()

            if len(action) > 0 and action[0] in ('R', 'N', 'U', 'O', 'Q'):
                # Player entered a valid action
                break

            if len(action.split()) == 2:
                space, number = action.split()
                if len(space) != 2:
                    continue

                column, row = space
                if column not in list('ABCDEFGHI'):
                    print('There is no column', column)
                    continue
                if not row.isdecimal() or not (1 <= int(row) <= 9):
                    print('There is no row', row)
                    continue
                if not (1 <= int(number) <= 9):
                    print('Select a number from 1 to 9, not ', number)
                    continue
                break               # Player entered a valid move

        print()

        if action.startswith('R'):
            # Reset the grid
            grid.resetGrid()
            continue

        if action.startswith('N'):
            # Get a new puzzle:
            grid = SudokuGrid(random.choice(puzzles))
            continue

        if action.startswith('U'):
            # Undo the last move
            grid.undo()
            continue

        if action.startswith('O'):
            # View the original numbers
            originalGrid = SudokuGrid(grid.originalSetup)
            print('The original grid looked like this:')
            originalGrid.display()
            input('Press Enter to continue...')

        if action.startswith('Q'):
            # Quit the game
            print('Thanks for playing!')
            sys.exit()

        # Handle the move the player selected
        if grid.makeMove(column, row, number) == False:
            print('You cannot overwrite the original grid\'s numbers.')
            print('Enter ORIGINAL to view the original grid.')
            input('Press Enter to continue...')

if __name__ == "__main__":
    main()