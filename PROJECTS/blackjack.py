import random, sys

# Set up the constants:
HEARTS   = chr(9829)                # Character 9829 is '♥'.
DIAMONDS = chr(9830)                # Character 9830 is '♦'.
SPADES   = chr(9824)                # Character 9824 is '♠'.
CLUBS    = chr(9827)                # Character 9827 is '♣'.
BACKSIDE = 'backside'

STARTING_MONEY = 5000

class Blackjack:
    def __init__(self):
        self.money = STARTING_MONEY
        print('''Blackjack, by Al Sweigart al@inventwithpython.com

    Rules:
      Try to get as close to 21 without going over
      Kings, Queens, and Jacks are worth 10 points
      Aces are worth 1 or 11 points
      Cards 2 through 10 are worth their face value
      (H)it to take another card
      (S)tand to stop taking cards
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing
      In case of a tie, the bet is returned to the player
      The dealer stops hitting at 17''')

    def is_broke(self):
        """
        Check if the player has run out of money
        """
        if self.money <= 0:
            print("You're broke!")
            print("Good thing you weren't playing with real money.")
            print('Thanks for playing!')
            sys.exit()

    def getBet(self, maxBet):
        """static method: Ask player how much they want to bet for this round."""

        while True:                         # Keep asking until they enter a valid amount
            print('How much do you bet? (1-{}, or QUIT)'.format(maxBet))
            bet = input('> ').strip()

            if bet.lower().startswith('q'):
                print('Thanks for playing!')
                sys.exit()
            elif bet.isdecimal():           # Note: Checks if string is decimal
                bet = int(bet)              # typecast input since always return str
                if 1 <= bet <= maxBet:
                    return bet              # return valid bet
            else:
                continue

    def getDeck(self):
        """Return a list of (rank, suit) tuples for all 52 cards."""
        deck = []
        
        # Builds the 52 deck cards and append it
        for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
            for rank in range(2, 11):
                deck.append((str(rank), suit))              # Data Type list[set(str, str)] ❤️
            for rank in ('J', 'Q', 'K', 'A'):               # Note: First card 2-10, Second card J-A but appends all
                deck.append((rank, suit))

        random.shuffle(deck)                                # Shuffles
        return deck

    def displayHands(self, playerHand, dealerHand, showDealerHand):
        """Show the player's and dealer's cards. Hide the dealer's first card if showDealerHand is False."""
        print()

        if showDealerHand:
            print('DEALER:', self.getHandValue(dealerHand))
            self.displayCards(dealerHand)
        else:
            print('DEALER: ???')
            self.displayCards([BACKSIDE] + dealerHand[1:])      # Hide the dealer's first card ❤️

        # Show the player's cards:
        print('PLAYER:', self.getHandValue(playerHand))
        self.displayCards(playerHand)

    def getMove(self, playerHand, money):
        """Asks the player for their move, and returns 'H' for hit, 'S' for
        stand, and 'D' for double down."""
        while True:
            moves = ['(H)it', '(S)tand']                        # Determine what moves the player can make

            # The player can double down on their first move, which we can tell because they'll have exactly two cards
            if len(playerHand) == 2 and money > 0:
                moves.append('(D)ouble down')

            movePrompt = ', '.join(moves) + '> '                # Get the player's move

            move = input(movePrompt).upper()

            # Note: We assume player gives correct input
            if move in ('H', 'S'):                              # ❤️
                return move
            if move == 'D' and '(D)ouble down' in moves:
                return move

    def getHandValue(self, cards):
        """static method: Returns the value of the cards. Face cards are worth 10, aces are
        worth 11 or 1 (this function picks the most suitable ace value)."""
        value = 0
        numberOfAces = 0

        # Add the value for the non-ace cards:
        for card in cards:
            rank = card[0]                              # card is a tuple like (rank, suit)
            if rank == 'A':
                numberOfAces += 1
            elif rank in ('K', 'Q', 'J'):               # Face cards are worth 10 points.
                value += 10
            else:
                value += int(rank)                      # Numbered cards are worth their number

        # Main logic ❤️❤️❤️❤️❤️
        # Add the value for the aces ❤️ Different than set ace to 11 and see if bust or convert to 1
        value += numberOfAces                           # Add 1 per ace

        for i in range(numberOfAces):
            if value + 10 <= 21:                        # If another 10 can be added without busting, do so:
                value += 10

        return value

    def displayCards(self, cards):
        """Display all the cards in the cards list."""
        rows = ['', '', '', '', '']                     # The text to display on each row

        for card in cards:
            rows[0] += ' ___  '                         # Print the top line of the card
            if card == BACKSIDE:                        # Print a card's back:
                rows[1] += '|## | '
                rows[2] += '|###| '
                rows[3] += '|_##| '
            else:                                       # Print the card's front:
                rank, suit = card                       # The card is a tuple data structure ❤️ Can do in JS
                rows[1] += '|{} | '.format(rank.ljust(2))   # .format() can justify align vs f string ❤️❤️❤️
                rows[2] += '| {} | '.format(suit)
                rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

        for row in rows:                                # Print each row on the screen ❤️
            print(row)