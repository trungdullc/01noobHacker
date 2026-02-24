"""
Dice Roller
Simulates dice rolls using the Dungeons & Dragons dice roll notation

Level: Beginner
What I learned:
    raise Exception()
    except Exception as exc:
"""

import random, sys

def main():
    print('''Dice Roller

Enter what kind and how many dice to roll. The format is the number of
dice, followed by "d", followed by the number of sides the dice have.
You can also add a plus or minus adjustment.

Examples:
3d6 rolls three 6-sided dice
1d10+2 rolls one 10-sided die, and adds 2
2d38-1 rolls two 38-sided die, and subtracts 1
QUIT quits the program
    ''')

    while True:                                 # Main program loop
        try:
            dice_input = input('> ')
            if dice_input.upper()[0] == 'Q':
                print('Thanks for playing!')
                sys.exit()

            # Clean up the dice string
            dice_input = dice_input.lower().replace(' ', '')

            # Find the "d" in the dice string input
            d_index = dice_input.find('d')

            if d_index == -1:
                raise Exception('Missing the "d" character')        # ❤️

            # Get the number of dice. (The "3" in "3d6+1"):
            number_of_dice = dice_input[:d_index]

            if not number_of_dice.isdecimal():
                raise Exception('Missing the number of dice')       # ❤️
            number_of_dice = int(number_of_dice)

            # Find if there is a plus or minus sign for a modifier
            mod_index = dice_input.find('+')

            if mod_index == -1:
                mod_index = dice_input.find('-')

            # Find the number of sides. (The "6" in "3d6+1"):
            if mod_index == -1:
                number_of_sides = dice_input[d_index + 1 :]
            else:
                number_of_sides = dice_input[d_index + 1 : mod_index]
            
            if not number_of_sides.isdecimal():
                raise Exception('Missing the number of sides')
            number_of_sides = int(number_of_sides)

            # Find the modifier amount. (The "1" in "3d6+1"):
            if mod_index == -1:
                mod_amount = 0
            else:
                mod_amount = int(dice_input[mod_index + 1 :])
                if dice_input[mod_index] == '-':
                    # Change the modification amount to negative
                    mod_amount = -mod_amount

            # Simulate the dice rolls
            rolls = []

            for i in range(number_of_dice):
                rollResult = random.randint(1, number_of_sides)
                rolls.append(rollResult)

            # Display the total:
            print('Total:', sum(rolls) + mod_amount, '(Each die: ', end='')

            # Display the individual rolls
            for i, roll in enumerate(rolls):
                rolls[i] = str(roll)
            print(', '.join(rolls), end='')

            # Display the modifier amount
            if mod_amount != 0:
                modSign = dice_input[mod_index]
                print(', {}{}'.format(modSign, abs(mod_amount)), end='')
            print(')')

        except Exception as exc:
            # Catch any exceptions and display the message to the user:
            print('Invalid input. Enter something like "3d6" or "1d10+2".')
            print('Input was invalid because: ' + str(exc))
            continue

if __name__ == "__main__":
    main()