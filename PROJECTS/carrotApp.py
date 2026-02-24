"""Carrot in a Box
A silly bluffing game between two human players. Based on the game from the show, 8 Out of 10 Cats

Level: Beginner
What I learned:
    ASCII art is hard and time consuming
    This code is super basic, not even worth the time to convert it to a class
"""

from carrot import Carrot
import random

def main():
    carrot = Carrot()
    carrot.set_names()

    print('''HERE ARE TWO BOXES:
    __________     __________
    /         /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/''')

    print()
    print(carrot.playerNames)
    print()
    print(carrot.p1Name + ', you have a RED box in front of you.')
    print(carrot.p2Name + ', you have a GOLD box in front of you.')
    print()
    print(carrot.p1Name + ', you will get to look into your box.')
    print(carrot.p2Name.upper() + ', close your eyes and don\'t look!!!')
    input('When ' + carrot.p2Name + ' has closed their eyes, press Enter...')
    print()

    print(carrot.p1Name + ' here is the inside of your box:')

    # Assign carrot
    if random.randint(1, 2) == 1:
        carrotInFirstBox = True
    else:
        carrotInFirstBox = False

    if carrotInFirstBox:
        print('''
    ___VV____
    |   VV    |
    |   VV    |
    |___||____|    __________
    /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
    (carrot!)''')
        print(carrot.playerNames)
    else:
        print('''
    _________
    |         |
    |         |
    |_________|    __________
    /         /|   /         /|
    +---------+ |  +---------+ |
    |   RED   | |  |   GOLD  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/
    (no carrot!)''')
        print(carrot.playerNames)

    input('Press Enter to continue...')

    print('\n' * 100)                       # Clear screen by printing several newlines
    print(carrot.p1Name + ', tell ' + carrot.p2Name + ' to open their eyes.')
    input('Press Enter to continue...')

    print()
    print(carrot.p1Name + ', say one of the following sentences to ' + carrot.p2Name + '.')
    print('  1) There is a carrot in my box.')
    print('  2) There is not a carrot in my box.')
    print()
    input('Then press Enter to continue...')

    print()
    print(carrot.p2Name + ', do you want to swap boxes with ' + carrot.p1Name + '? YES/NO')
    while True:
        response = input('> ').upper()
        if not (response.startswith('Y') or response.startswith('N')):
            print(carrot.p2Name + ', please enter "YES" or "NO".')
        else:
            break

    firstBox = 'RED '                                   # Note the space after the "D"
    secondBox = 'GOLD'

    if response.startswith('Y'):
        carrotInFirstBox = not carrotInFirstBox
        firstBox, secondBox = secondBox, firstBox

    print('''HERE ARE THE TWO BOXES:
    __________     __________
    /         /|   /         /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/'''.format(firstBox, secondBox))
    print(carrot.playerNames)

    input('Press Enter to reveal the winner...')
    print()

    if carrotInFirstBox:
        print('''
    ___VV____      _________
    |   VV    |    |         |
    |   VV    |    |         |
    |___||____|    |_________|
    /    ||   /|   /         /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/'''.format(firstBox, secondBox))

    else:
        print('''
    _________      ___VV____
    |         |    |   VV    |
    |         |    |   VV    |
    |_________|    |___||____|
    /         /|   /    ||   /|
    +---------+ |  +---------+ |
    |   {}  | |  |   {}  | |
    |   BOX   | /  |   BOX   | /
    +---------+/   +---------+/'''.format(firstBox, secondBox))

    print(carrot.playerNames)

    # This modification made possible through the 'carrotInFirstBox variable
    if carrotInFirstBox:
        print(carrot.p1Name + ' is the winner!')
    else:
        print(carrot.p2Name + ' is the winner!')

    print('Thanks for playing!')

if __name__ == "__main__":
    main()