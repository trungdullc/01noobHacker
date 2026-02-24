"""
The Tower of Hanoi

A stack-moving puzzle game

Level: Intermediate
What I learned:
    TODO later
"""

import copy, sys
from hanoi import Hanoi, COMPLETE_TOWER

def main():
    hanoi = Hanoi()

    # Set up the towers. The end of the list is the top of the tower
    towers = {'A': copy.copy(COMPLETE_TOWER), 'B': [], 'C': []}

    while True:                         # Run a single turn
        # Display the towers and disks
        hanoi.displayTowers(towers)

        # Ask the user for a move
        fromTower, toTower = hanoi.askForPlayerMove(towers)

        # Move the top disk from fromTower to toTower
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # Check if the user has solved the puzzle
        if COMPLETE_TOWER in (towers['B'], towers['C']):
            hanoi.displayTowers(towers)       # Display the towers one last time
            print('You have solved the puzzle! Well done!')
            sys.exit()

if __name__ == '__main__':
    main()