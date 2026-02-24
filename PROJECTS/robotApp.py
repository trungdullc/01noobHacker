"""
Hungry Robots
Escape the hungry robots by making them crash into each other

Level: Advance
What I learned:
    TODO later
"""

import sys
from robot import Robot

def main():
    robot = Robot()

    # Set up a new game
    board = robot.getNewBoard()
    robots = robot.addRobots(board)
    playerPosition = robot.getRandomEmptySpace(board, robots)

    while True:                         # Main game loop
        robot.displayBoard(board, robots, playerPosition)

        if len(robots) == 0:            # Check if the player has won
            print('All the robots have crashed into each other and you')
            print('lived to tell the tale! Good job!')
            sys.exit()

        # Move the player and robots
        playerPosition = robot.askForPlayerMove(board, robots, playerPosition)
        robots = robot.moveRobots(board, robots, playerPosition)

        for x, y in robots:             # Check if the player has lost
            if (x, y) == playerPosition:
                robot.displayBoard(board, robots, playerPosition)
                print('You have been caught by a robot!')
                sys.exit()

if __name__ == '__main__':
    main()