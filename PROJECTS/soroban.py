NUMBER_OF_DIGITS = 10

class Abacus:
    def __init__(self):
        print('Soroban - The Japanese Abacus\n')

    def displayAbacus(self, number):
        numberList = list(str(number).zfill(NUMBER_OF_DIGITS))

        hasBead = []                                # Contains a True or False for each bead position

        # Top heaven row has a bead for digits 0, 1, 2, 3, and 4
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '01234')

        # Bottom heaven row has a bead for digits 5, 6, 7, 8, and 9
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '56789')

        # 1st (topmost) earth row has a bead for all digits except 0
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '12346789')

        # 2nd earth row has a bead for digits 2, 3, 4, 7, 8, and 9
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '234789')

        # 3rd earth row has a bead for digits 0, 3, 4, 5, 8, and 9
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '034589')

        # 4th earth row has a bead for digits 0, 1, 2, 4, 5, 6, and 9
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '014569')

        # 5th earth row has a bead for digits 0, 1, 2, 5, 6, and 7
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '012567')

        # 6th earth row has a bead for digits 0, 1, 2, 3, 5, 6, 7, and 8
        for i in range(NUMBER_OF_DIGITS):
            hasBead.append(numberList[i] in '01235678')

        # Convert these True or False values into O or | characters
        abacusChar = []

        for i, beadPresent in enumerate(hasBead):
            if beadPresent:
                abacusChar.append('O')
            else:
                abacusChar.append('|')

        # Draw the abacus with the O/| characters
        chars = abacusChar + numberList
        print("""
    +================================+
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  |  |  |  |  |  |  |  |  |  |  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    +================================+
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    +=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))

    def displayControls(self):
        print('  +q  w  e  r  t  y  u  i  o  p')
        print('  -a  s  d  f  g  h  j  k  l  ;')
        print('(Enter a number, "quit", or a stream of up/down letters.)')