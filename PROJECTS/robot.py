import random, sys

WIDTH = 40                      # (!) Try changing this to 70 or 10
HEIGHT = 20                     # (!) Try changing this to 10
NUM_ROBOTS = 10                 # (!) Try changing this to 1 or 30
NUM_TELEPORTS = 2               # (!) Try changing this to 0 or 9999
NUM_DEAD_ROBOTS = 2             # (!) Try changing this to 0 or 20
NUM_WALLS = 100                 # (!) Try changing this to 0 or 300

EMPTY_SPACE = ' '               # (!) Try changing this to '.'
PLAYER = '@'                    # (!) Try changing this to 'R'
ROBOT = 'R'                     # (!) Try changing this to '@'
DEAD_ROBOT = 'X'                # (!) Try changing this to 'R'

# (!) Try changing this to '#' or 'O' or ' ':
WALL = chr(9617)                # Character 9617 is '░'

class Robot:
    def __init__(self):
        print('''Hungry Robots

You are trapped in a maze with hungry robots! You don't know why robots
need to eat, but you don't want to find out. The robots are badly
programmed and will move directly toward you, even if blocked by walls.
You must trick the robots into crashing into each other (or dead robots)
without being caught. You have a personal teleporter device, but it only
has enough battery for {} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
'''.format(NUM_TELEPORTS))

        input('Press Enter to begin...')

    def getNewBoard(self):
        """Returns a dictionary that represents the board. The keys are
        (x, y) tuples of integer indexes for board positions, the values are
        WALL, EMPTY_SPACE, or DEAD_ROBOT. The dictionary also has the key
        'teleports' for the number of teleports the player has left.
        The living robots are stored separately from the board dictionary."""
        board = {'teleports': NUM_TELEPORTS}

        # Create an empty board:
        for x in range(WIDTH):
            for y in range(HEIGHT):
                board[(x, y)] = EMPTY_SPACE

        # Add walls on the edges of the board:
        for x in range(WIDTH):
            board[(x, 0)] = WALL  # Make top wall.
            board[(x, HEIGHT - 1)] = WALL  # Make bottom wall.
        for y in range(HEIGHT):
            board[(0, y)] = WALL  # Make left wall.
            board[(WIDTH - 1, y)] = WALL  # Make right wall.

        # Add the random walls:
        for i in range(NUM_WALLS):
            x, y = self.getRandomEmptySpace(board, [])
            board[(x, y)] = WALL

        # Add the starting dead robots:
        for i in range(NUM_DEAD_ROBOTS):
            x, y = self.getRandomEmptySpace(board, [])
            board[(x, y)] = DEAD_ROBOT
        return board

    def getRandomEmptySpace(self, board, robots):
        """Return a (x, y) integer tuple of an empty space on the board."""
        while True:
            randomX = random.randint(1, WIDTH - 2)
            randomY = random.randint(1, HEIGHT - 2)
            if self.isEmpty(randomX, randomY, board, robots):
                break
        return (randomX, randomY)

    def isEmpty(self, x, y, board, robots):
        """Return True if the (x, y) is empty on the board and there's also
        no robot there."""
        return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots

    def addRobots(self, board):
        """Add NUM_ROBOTS number of robots to empty spaces on the board and
        return a list of these (x, y) spaces where robots are now located."""
        robots = []
        for i in range(NUM_ROBOTS):
            x, y = self.getRandomEmptySpace(board, robots)
            robots.append((x, y))
        return robots

    def displayBoard(self, board, robots, playerPosition):
        """Display the board, robots, and player on the screen."""
        # Loop over every space on the board:
        for y in range(HEIGHT):
            for x in range(WIDTH):
                # Draw the appropriate character:
                if board[(x, y)] == WALL:
                    print(WALL, end='')
                elif board[(x, y)] == DEAD_ROBOT:
                    print(DEAD_ROBOT, end='')
                elif (x, y) == playerPosition:
                    print(PLAYER, end='')
                elif (x, y) in robots:
                    print(ROBOT, end='')
                else:
                    print(EMPTY_SPACE, end='')
            print()  # Print a newline.

    def askForPlayerMove(self, board, robots, playerPosition):
        """Returns the (x, y) integer tuple of the place the player moves
        next, given their current location and the walls of the board."""
        playerX, playerY = playerPosition

        # Find which directions aren't blocked by a wall:
        q = 'Q' if self.isEmpty(playerX - 1, playerY - 1, board, robots) else ' '
        w = 'W' if self.isEmpty(playerX + 0, playerY - 1, board, robots) else ' '
        e = 'E' if self.isEmpty(playerX + 1, playerY - 1, board, robots) else ' '
        d = 'D' if self.isEmpty(playerX + 1, playerY + 0, board, robots) else ' '
        c = 'C' if self.isEmpty(playerX + 1, playerY + 1, board, robots) else ' '
        x = 'X' if self.isEmpty(playerX + 0, playerY + 1, board, robots) else ' '
        z = 'Z' if self.isEmpty(playerX - 1, playerY + 1, board, robots) else ' '
        a = 'A' if self.isEmpty(playerX - 1, playerY + 0, board, robots) else ' '
        allMoves = (q + w + e + d + c + x + a + z + 'S')

        while True:
            # Get player's move
            print('(T)eleports remaining: {}'.format(board["teleports"]))
            print('                    ({}) ({}) ({})'.format(q, w, e))
            print('                    ({}) (S) ({})'.format(a, d))
            print('Enter move or QUIT: ({}) ({}) ({})'.format(z, x, c))

            move = input('> ').upper()
            if move == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            elif move == 'T' and board['teleports'] > 0:
                # Teleport the player to a random empty space
                board['teleports'] -= 1
                return self.getRandomEmptySpace(board, robots)
            elif move != '' and move in allMoves:
                # Return the new player position based on their move
                return {'Q': (playerX - 1, playerY - 1),
                        'W': (playerX + 0, playerY - 1),
                        'E': (playerX + 1, playerY - 1),
                        'D': (playerX + 1, playerY + 0),
                        'C': (playerX + 1, playerY + 1),
                        'X': (playerX + 0, playerY + 1),
                        'Z': (playerX - 1, playerY + 1),
                        'A': (playerX - 1, playerY + 0),
                        'S': (playerX, playerY)}[move]

    def moveRobots(self, board, robotPositions, playerPosition):
        """Return a list of (x, y) tuples of new robot positions after they
        have tried to move toward the player."""
        playerx, playery = playerPosition
        nextRobotPositions = []

        while len(robotPositions) > 0:
            robotx, roboty = robotPositions[0]

            # Determine the direction the robot moves
            if robotx < playerx:
                movex = 1                   # Move right
            elif robotx > playerx:
                movex = -1                  # Move left
            elif robotx == playerx:
                movex = 0                   # Don't move horizontally

            if roboty < playery:
                movey = 1                   # Move up
            elif roboty > playery:
                movey = -1                  # Move down
            elif roboty == playery:
                movey = 0                   # Don't move vertically

            # Check if the robot would run into a wall, and adjust course
            if board[(robotx + movex, roboty + movey)] == WALL:
                # Robot would run into a wall, so come up with a new move
                if board[(robotx + movex, roboty)] == EMPTY_SPACE:
                    movey = 0               # Robot can't move horizontally
                elif board[(robotx, roboty + movey)] == EMPTY_SPACE:
                    movex = 0               # Robot can't move vertically
                else:
                    # Robot can't move
                    movex = 0
                    movey = 0
            newRobotx = robotx + movex
            newRoboty = roboty + movey

            if (board[(robotx, roboty)] == DEAD_ROBOT
                or board[(newRobotx, newRoboty)] == DEAD_ROBOT):
                # Robot is at a crash site, remove it
                del robotPositions[0]
                continue

            # Check if it moves into a robot, then destroy both robots
            if (newRobotx, newRoboty) in nextRobotPositions:
                board[(newRobotx, newRoboty)] = DEAD_ROBOT
                nextRobotPositions.remove((newRobotx, newRoboty))
            else:
                nextRobotPositions.append((newRobotx, newRoboty))

            # Remove robots from robotPositions as they move
            del robotPositions[0]
        return nextRobotPositions