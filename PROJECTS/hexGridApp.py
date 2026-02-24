"""Hex Grid
Displays a simple tessellation of a hexagon grid.

Level: Beginner
What I learned:
    Nothing, more of a learning row, column in a nested for loop
"""

X_REPEAT = 19               # How many times to tessellate horizontally
Y_REPEAT = 12               # How many times to tessellate vertically

def main():
    for column in range(Y_REPEAT):
        # Display the top half of the hexagon
        for row in range(X_REPEAT):
            print(r'/ \_', end='')
        print()

        # Display the bottom half of the hexagon
        for row in range(X_REPEAT):
            print(r'\_/ ', end='')
        print()
    
if __name__ == "__main__":
    main()