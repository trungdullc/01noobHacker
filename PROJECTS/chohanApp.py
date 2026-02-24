"""
Cho-Han
The traditional Japanese dice game of even-odd

Level: Beginner
What I learned:
    How to determine if odd/even (Leetcode)
"""

import sys
from chohan import ChoHan

def main():
    chohan = ChoHan()

    while True:                             # Main game loop
        chohan.set_bet()
        chohan.roll_dices()
        chohan.place_bet()
        chohan.reveal_dice()

        # Note: Was lazy to convert the rest into class just needed to understand main logic of how to determine even/odd

        # Determine if the player won using mod 2 instead of bitwise &
        rollIsEven = (chohan.dice1 + chohan.dice2) % 2 == 0
        
        if rollIsEven:
            correctBet = 'CHO'
        else:
            correctBet = 'HAN'

        playerWon = chohan.bet == correctBet

        # Display the bet results:
        if playerWon:
            print('You won! You take', chohan.pot, 'mon.')
            chohan.purse = chohan.purse + chohan.pot                        # Add pot from player's purse
            print('The house collects a', chohan.pot // 10, 'mon fee.')
            chohan.purse = chohan.purse - (chohan.pot // 10)                # The house fee is 10%
        else:
            chohan.purse = chohan.purse - chohan.pot                        # Subtract the pot from player's purse
            print('You lost!')

        # Check if the player has run out of money
        if chohan.purse == 0:
            print('You have run out of money!')
            print('Thanks for playing!')
            sys.exit()

if __name__ == "__main__":
    main()