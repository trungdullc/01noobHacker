"""
Conway's Game of Life
The classic cellular automata simulation. Press Ctrl-C to stop.

Level: Beginner
What I learned:
    copy.deepcopy() there a deep and shallow copy (new object) like in C++
"""

import copy, random, sys, time

CELL_WIDTH = 79
CELL_HEIGHT = 20

# (!) Try changing ALIVE to '|' and DEAD to '-'
ALIVE = 'O'         # Character representing a living cell
DEAD = ' '          # Character representing a dead cell

# The cells and nextCells are dictionaries for the state of the game
# Their keys are (x, y) tuples and their values are one of the ALIVE or DEAD values
nextCells = {}

def main():
    # Fill random dead and alive cells into nextCells
    for x in range(CELL_WIDTH):                 # Loop over every possible column
        for y in range(CELL_HEIGHT):            # Loop over every possible row
            # 50/50 chance for starting cells being alive or dead
            if random.randint(0, 1) == 0:
                nextCells[(x, y)] = ALIVE       # Add a living cell
            else:
                nextCells[(x, y)] = DEAD        # Add a dead cell

    while True:                                 # Main program loop
        print('\n' * 50)                        # Separate each step with newlines
        cells = copy.deepcopy(nextCells)        # ❤️

        # Print cells on the screen:
        for y in range(CELL_HEIGHT):
            for x in range(CELL_WIDTH):
                print(cells[(x, y)], end='')    # Print the # or space
            print()                             # Print a newline at the end of the row
        print('Press Ctrl-C to quit.')

        # Calculate the next step's cells based on current step's cells:
        for x in range(CELL_WIDTH):
            for y in range(CELL_HEIGHT):
                # Get the neighboring coordinates of (x, y), even if they wrap around the edge ❤️❤️❤️❤️❤️
                left  = (x - 1) % CELL_WIDTH
                right = (x + 1) % CELL_WIDTH
                above = (y - 1) % CELL_HEIGHT
                below = (y + 1) % CELL_HEIGHT

                # Count the number of living neighbors:
                numNeighbors = 0

                if cells[(left, above)] == ALIVE:
                    numNeighbors += 1               # Top-left neighbor is alive
                if cells[(x, above)] == ALIVE:
                    numNeighbors += 1               # Top neighbor is alive
                if cells[(right, above)] == ALIVE:
                    numNeighbors += 1               # Top-right neighbor is alive
                if cells[(left, y)] == ALIVE:
                    numNeighbors += 1               # Left neighbor is alive
                if cells[(right, y)] == ALIVE:
                    numNeighbors += 1               # Right neighbor is alive
                if cells[(left, below)] == ALIVE:
                    numNeighbors += 1               # Bottom-left neighbor is alive
                if cells[(x, below)] == ALIVE:
                    numNeighbors += 1               # Bottom neighbor is alive
                if cells[(right, below)] == ALIVE:
                    numNeighbors += 1               # Bottom-right neighbor is alive

                # Set cell based on Conway's Game of Life rules
                if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors == 3):
                        # Living cells with 2 or 3 neighbors stay alive:
                        nextCells[(x, y)] = ALIVE
                elif cells[(x, y)] == DEAD and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    nextCells[(x, y)] = ALIVE
                else:
                    # Everything else dies or stays dead:
                    nextCells[(x, y)] = DEAD

        try:
            time.sleep(1)                           # Add a 1 second pause to reduce flickering
        except KeyboardInterrupt:
            print("Conway's Game of Life")
            sys.exit()

if __name__ == "__main__":
    main()