"""
Three-Card Monte

Find the Queen of Hearts after cards have been swapped around.
(In the real-life version, the scammer palms the Queen of Hearts so you always lose.)
"""

import random, time
from monte import Monte, HEARTS, LEFT, MIDDLE, RIGHT, NUM_SWAPS, DELAY

def main():
    monte = Monte()
    # Show the original arrangement
    cards = [('Q', HEARTS), monte.getRandomCard(), monte.getRandomCard()]
    random.shuffle(cards)                       # Put the Queen of Hearts in a random place
    print('Here are the cards:')
    monte.displayCards(cards)
    input('Press Enter when you are ready to begin...')

    # Print the swaps
    for i in range(NUM_SWAPS):
        swap = random.choice(['l-m', 'm-r', 'l-r', 'm-l', 'r-m', 'r-l'])

        if swap == 'l-m':
            print('swapping left and middle...')
            cards[LEFT], cards[MIDDLE] = cards[MIDDLE], cards[LEFT]
        elif swap == 'm-r':
            print('swapping middle and right...')
            cards[MIDDLE], cards[RIGHT] = cards[RIGHT], cards[MIDDLE]
        elif swap == 'l-r':
            print('swapping left and right...')
            cards[LEFT], cards[RIGHT] = cards[RIGHT], cards[LEFT]
        elif swap == 'm-l':
            print('swapping middle and left...')
            cards[MIDDLE], cards[LEFT] = cards[LEFT], cards[MIDDLE]
        elif swap == 'r-m':
            print('swapping right and middle...')
            cards[RIGHT], cards[MIDDLE] = cards[MIDDLE], cards[RIGHT]
        elif swap == 'r-l':
            print('swapping right and left...')
            cards[RIGHT], cards[LEFT] = cards[LEFT], cards[RIGHT]

        time.sleep(DELAY)

    # Print several new lines to hide the swaps
    print('\n' * 60)

    # Ask the user to find the red lady
    while True:             # Keep asking until LEFT, MIDDLE, or RIGHT is entered
        print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
        guess = input('> ').upper()

        # Get the index in cards for the position that the player entered
        if guess in ['LEFT', 'MIDDLE', 'RIGHT']:
            if guess == 'LEFT':
                guessIndex = 0
            elif guess == 'MIDDLE':
                guessIndex = 1
            elif guess == 'RIGHT':
                guessIndex = 2
            break

    # (!) Uncomment this code to make the player always lose
    #if cards[guessIndex] == ('Q', HEARTS):
    #    # Player has won, so let's move the queen.
    #    possibleNewIndexes = [0, 1, 2]
    #    possibleNewIndexes.remove(guessIndex)  # Remove the queen's index.
    #    newInd = random.choice(possibleNewIndexes)  # Choose a new index.
    #    # Place the queen at the new index:
    #    cards[guessIndex], cards[newInd] = cards[newInd], cards[guessIndex]

    monte.displayCards(cards)               # Show all the cards

    # Check if the player won
    if cards[guessIndex] == ('Q', HEARTS):
        print('You won!')
        print('Thanks for playing!')
    else:
        print('You lost!')
        print('Thanks for playing, sucker!')

if __name__ == "__main__":
    main()