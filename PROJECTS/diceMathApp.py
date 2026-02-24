"""
Dice Math
A flash card addition game where you sum the total on random dice rolls

Level: Beginner
What I learned:
    assert method
    Different type of data structures
"""

import random, time

DICE_WIDTH = 9
DICE_HEIGHT = 5
CANVAS_WIDTH = 79
CANVAS_HEIGHT = 24 - 3          # -3 for room to enter the sum at the bottom

# The duration is in seconds
QUIZ_DURATION = 30              # (!) Try changing this to 10 or 60
MIN_DICE = 2                    # (!) Try changing this to 1 or 5
MAX_DICE = 6                    # (!) Try changing this to 14

REWARD = 4                      # (!) Points awarded for correct answers
PENALTY = 1                     # (!) Points removed for incorrect answers

# The program hangs if all of the dice can't fit on the screen
assert MAX_DICE <= 14           # ❤️

# Data Structure is tuple[list[str], int]
D1 = (['+-------+',
       '|       |',
       '|   O   |',
       '|       |',
       '+-------+'], 1)

D2a = (['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'], 2)

D2b = (['+-------+',
        '|     O |',
        '|       |',
        '| O     |',
        '+-------+'], 2)

D3a = (['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'], 3)

D3b = (['+-------+',
        '|     O |',
        '|   O   |',
        '| O     |',
        '+-------+'], 3)

D4 = (['+-------+',
       '| O   O |',
       '|       |',
       '| O   O |',
       '+-------+'], 4)

D5 = (['+-------+',
       '| O   O |',
       '|   O   |',
       '| O   O |',
       '+-------+'], 5)

D6a = (['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+'], 6)

D6b = (['+-------+',
        '| O O O |',
        '|       |',
        '| O O O |',
        '+-------+'], 6)

ALL_DICE = [D1, D2a, D2b, D3a, D3b, D4, D5, D6a, D6b]   # list[objects]

def main():
    print('''Dice Math

    Add up the sides of all the dice displayed on the screen. You have
    {} seconds to answer as many as possible. You get {} points for each
    correct answer and lose {} point for each incorrect answer.
    '''.format(QUIZ_DURATION, REWARD, PENALTY))

    input('Press Enter to begin...')

    # Keep track of how many answers were correct and incorrect
    correct_answers = 0
    incorrect_answers = 0

    start_time = time.time()                                    # current time without using datetime module

    while time.time() < start_time + QUIZ_DURATION:             # Main game loop
        # Come up with the dice to display
        sum_answer = 0
        dice_faces = []                                         # Contains total dice objects

        for i in range(random.randint(MIN_DICE, MAX_DICE)):
            die = random.choice(ALL_DICE)
            dice_faces.append(die[0])                           # die[0] is the list[str] that show dice
            sum_answer += die[1]                                # die[1] is the value of the dice

        # Contains (x, y) tuples of the top-left corner of each die
        top_left_dice_corners = []                              # Coordinates of top left corner of dices

        # Figure out where dice should go
        for i in range(len(dice_faces)):
            while True:
                # Find a random place on the canvas to put the die:
                left = random.randint(0, CANVAS_WIDTH  - 1 - DICE_WIDTH)
                top  = random.randint(0, CANVAS_HEIGHT - 1 - DICE_HEIGHT)

                # Get the x, y coordinates for all four corners
                #      left
                #      v
                #top > +-------+ ^
                #      | O     | |
                #      |   O   | DICE_HEIGHT (5)
                #      |     O | |
                #      +-------+ v
                #      <------->
                #      DICE_WIDTH (9)
                topLeftX = left
                topLeftY = top
                topRightX = left + DICE_WIDTH
                topRightY = top
                bottomLeftX = left
                bottomLeftY = top + DICE_HEIGHT
                bottomRightX = left + DICE_WIDTH
                bottomRightY = top + DICE_HEIGHT

                # Check if this die overlaps with previous dice
                overlaps = False

                for prevDieLeft, prevDieTop in top_left_dice_corners:
                    prevDieRight = prevDieLeft + DICE_WIDTH
                    prevDieBottom = prevDieTop + DICE_HEIGHT
                    # Check each corner of this die to see if it is inside of area the previous die
                    for cornerX, cornerY in ((topLeftX, topLeftY),
                                            (topRightX, topRightY),
                                            (bottomLeftX, bottomLeftY),
                                            (bottomRightX, bottomRightY)):
                        if (prevDieLeft <= cornerX < prevDieRight and prevDieTop <= cornerY < prevDieBottom):
                                overlaps = True
                if not overlaps:
                    # It doesn't overlap, so we can put it here
                    top_left_dice_corners.append((left, top))
                    break

        # Draw the dice on the canvas
        # Keys are (x, y) tuples of ints, values the character at that position on the canvas
        canvas = {}
        
        # Loop over each die:
        for i, (dieLeft, dieTop) in enumerate(top_left_dice_corners):
            # Loop over each character in the die's face
            dieFace = dice_faces[i]
            
            for dx in range(DICE_WIDTH):
                for dy in range(DICE_HEIGHT):
                    # Copy this character to the correct place on the canvas
                    canvasX = dieLeft + dx
                    canvasY = dieTop + dy
                    # Note that in dieFace, a list of strings, the x and y are swapped
                    canvas[(canvasX, canvasY)] = dieFace[dy][dx]

        # Display the canvas on the screen
        for cy in range(CANVAS_HEIGHT):
            for cx in range(CANVAS_WIDTH):
                print(canvas.get((cx, cy), ' '), end='')
            print()

        # Let the player enter their answer
        response = input('Enter the sum: ').strip()
        if response.isdecimal() and int(response) == sum_answer:
            correct_answers += 1
        else:
            print('Incorrect, the answer is', sum_answer)
            time.sleep(2)
            incorrect_answers += 1

    # Display the final score
    score = (correct_answers * REWARD) - (incorrect_answers * PENALTY)
    print('Correct:  ', correct_answers)
    print('Incorrect:', incorrect_answers)
    print('Score:    ', score)

if __name__ == "__main__":
    main()