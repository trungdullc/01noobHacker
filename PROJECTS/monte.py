import random

NUM_SWAPS = 16                  # (!) Try changing this to 30 or 100.
DELAY     = 0.8                 # (!) Try changing this 2.0 or 0.0.

# The card suit characters
HEARTS   = chr(9829)            # Character 9829 is '♥'
DIAMONDS = chr(9830)            # Character 9830 is '♦'
SPADES   = chr(9824)            # Character 9824 is '♠'
CLUBS    = chr(9827)            # Character 9827 is '♣'

# The indexes of a 3-card list
LEFT   = 0
MIDDLE = 1
RIGHT  = 2

class Monte:
    def __init__(self):
        print('Three-Card Monte')
        print()
        print('Find the red lady (the Queen of Hearts)! Keep an eye on how')
        print('the cards move.')
        print()

    def displayCards(self, cards):
        """Display the cards in "cards", which is a list of (rank, suit)
        tuples."""
        rows = ['', '', '', '', '']  # Stores the text to display.

        for i, card in enumerate(cards):
            rank, suit = card  # The card is a tuple data structure.
            rows[0] += ' ___  '  # Print the top line of the card.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        # Print each row on the screen:
        for i in range(5):
            print(rows[i])

    def getRandomCard(self):
        """Returns a random card that is NOT the Queen of Hearts."""
        while True:  # Make cards until you get a non-Queen of hearts.
            rank = random.choice(list('23456789JQKA') + ['10'])
            suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])

            # Return the card as long as it's not the Queen of Hearts:
            if rank != 'Q' and suit != HEARTS:
                return (rank, suit)