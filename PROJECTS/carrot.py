class Carrot:
    def __init__(self):
        self.p1Name = ""
        self.p2Name = ""
        self.playerNames = ""
        print('''Carrot in a Box

This is a bluffing game for two human players. Each player has a box.
One box has a carrot in it. To win, you must have the box with the
carrot in it.

This is a very simple and silly game.

The first player looks into their box (the second player must close
their eyes during this.) The first player then says "There is a carrot
in my box" or "There is not a carrot in my box". The second player then
gets to decide if they want to swap boxes or not.
''')
        input('Press Enter to begin...')

    def set_names(self):
        self.p1Name = input('Human player 1, enter your name: ')
        self.p2Name = input('Human player 2, enter your name: ')
        self.playerNames = self.p1Name[:11].center(11) + '    ' + self.p2Name[:11].center(11)