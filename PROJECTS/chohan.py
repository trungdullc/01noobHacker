import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}
STARTING_MONEY = 5000

class ChoHan:
    def __init__(self):
        self.pot = ""
        self.purse = STARTING_MONEY
        self.dice1 = 0
        self.dice2 = 0
        self.bet = ""
        print('''Cho-Han

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.
''')

    def set_bet(self):
        print('You have', self.purse, 'How much do you bet? (or QUIT)')

        while True:
            self.pot = input('> ')

            if self.pot.upper().startswith("Q"):
                print('Thanks for playing!')
                sys.exit()
            elif not self.pot.isdecimal():
                print('Please enter a number!')
            elif int(self.pot) > self.purse:
                print('You do not have enough to make that bet')
            else:
                self.pot = int(self.pot)            # Note: dynamic typing
                break

    def roll_dices(self):
        self.dice1 = random.randint(1, 6)
        self.dice2 = random.randint(1, 6)

    def place_bet(self):
        print('The dealer swirls the cup and you hear the rattle of dice.')
        print('The dealer slams the cup on the floor, still covering the')
        print('dice and asks for your bet.')
        print()
        print('    CHO (even) or HAN (odd)?')

        # Let the player bet cho or han:
        while True:
            self.bet = input('> ').upper()[0]

            if self.bet == "C" or self.bet =="H":
                break
            else:
                print('Please enter either "CHO" or "HAN".')
                continue

    def reveal_dice(self):
        print('The dealer lifts the cup to reveal:')
        print('  ', JAPANESE_NUMBERS[self.dice1], '-', JAPANESE_NUMBERS[self.dice2])
        print('    ', self.dice1, '-', self.dice2)