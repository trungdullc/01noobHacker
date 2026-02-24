"""Blackjack CLI
The classic card game also known as 21. (This version doesn't have splitting or insurance)

Level: Beginner
What I learned:
    When converting to class remember self parameter in Python3
    When a method uses another method use self.
    When a static method used as a function use the instance.method() since python not have static methods like C++
    builtins.list.pop() removes last element from list and [] saves it as a list
    Accessing set similar to list with [0]
"""

from blackjack import Blackjack

def main():
    blackjack = Blackjack()

    while True:                                     # Main game loop, exit with break or sys.exit()
        blackjack.is_broke()                        # Exit game or not when broke

        # Let the player enter their bet for this round:
        print('Money:', blackjack.money)
        bet = blackjack.getBet(blackjack.money)     # Note: acts as a static method

        # Give the dealer and player two cards from the deck each:
        deck = blackjack.getDeck()
        dealerHand = [deck.pop(), deck.pop()]       # Pops last data type from array
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions:
        print('Bet:', bet)
        while True:                                 # Keep looping until player stands or busts.
            blackjack.displayHands(playerHand, dealerHand, showDealerHand=False)
            print()

            # Check if the player has bust
            if blackjack.getHandValue(playerHand) > 21:
                break

            # Get the player's move, either H, S, or D
            move = blackjack.getMove(playerHand, blackjack.money - bet)

            # Handle the player actions
            if move == 'D':
                # Player is doubling down, they can increase their bet
                additionalBet = blackjack.getBet(min(bet, (blackjack.money - bet)))
                bet += additionalBet
                print('Bet increased to {}.'.format(bet))
                print('Bet:', bet)

            if move in ('H', 'D'):
                # Hit/doubling down takes another card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank, suit))
                playerHand.append(newCard)

                if blackjack.getHandValue(playerHand) > 21:
                    # The player has busted
                    continue

            if move in ('S', 'D'):
                # Stand/doubling down stops the player's turn
                break

        # Handle the dealer's actions:
        if blackjack.getHandValue(playerHand) <= 21:
            while blackjack.getHandValue(dealerHand) < 17:
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                blackjack.displayHands(playerHand, dealerHand, False)

                if blackjack.getHandValue(dealerHand) > 21:
                    break                               # The dealer has busted

                input('Press Enter to continue...')
                print('\n\n')

        # Show the final hands
        blackjack.displayHands(playerHand, dealerHand, True)

        playerValue = blackjack.getHandValue(playerHand)
        dealerValue = blackjack.getHandValue(dealerHand)
        
        # Handle whether the player won, lost, or tied:
        if dealerValue > 21:
            print('Dealer busts! You win ${}!'.format(bet))
            blackjack.money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('You lost!')
            blackjack.money -= bet
        elif playerValue > dealerValue:
            print('You won ${}!'.format(bet))
            blackjack.money += bet
        elif playerValue == dealerValue:
            print('It\'s a tie, the bet is returned to you.')

        input('Press Enter to continue...')
        print('\n\n')

if __name__ == '__main__':
    main()