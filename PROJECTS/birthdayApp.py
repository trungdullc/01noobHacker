"""
Birthday Paradox Simulation
Explore the surprising probabilities of the "Birthday Paradox".

Level: Beginner
What I Learned:
    Basics of datetime module
    A nested for enumerate type loop that compares everything after (useful for leetcode brute force manual searches)
"""

import sys
from birthday import Birthday, MONTHS

def main():
    mybirthdays = Birthday()
    number_of_BDays = mybirthdays.validiate_input()
    print()

    # Generate and display the birthdays:
    print('Here are', number_of_BDays, 'birthdays:')
    birthdays = mybirthdays.getBirthdays(number_of_BDays)

    for i, birthday in enumerate(birthdays):
        if i != 0:
            print(', ', end='')     # Display a comma for each birthday after first birthday

        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end='')
    print()
    print()

    # Determine if there are two birthdays that match.
    match = mybirthdays.getMatch(birthdays)

    # Display the results:
    print('In this simulation, ', end='')

    if match != None:
        monthName = MONTHS[match.month - 1]
        dateText = '{} {}'.format(monthName, match.day)
        print('multiple people have a birthday on', dateText)
    else:
        print('there are no matching birthdays.')
    print()

    # Run through 100,000 simulations:
    print('Generating', number_of_BDays, 'random birthdays 100,000 times...')
    input('Press Enter to begin...')

    print('Let\'s run another 100,000 simulations.')
    simMatch = 0  # How many simulations had matching birthdays in them.
    for i in range(100000):
        # Report on the progress every 10,000 simulations:
        if i % 10000 == 0:
            print(i, 'simulations run...')
        birthdays = mybirthdays.getBirthdays(number_of_BDays)
        if mybirthdays.getMatch(birthdays) != None:
            simMatch = simMatch + 1
    print('100,000 simulations run.')

    # Display simulation results:
    probability = round(simMatch / 100000 * 100, 2)
    print('Out of 100,000 simulations of', number_of_BDays, 'people, there was a')
    print('matching birthday in that group', simMatch, 'times. This means')
    print('that', number_of_BDays, 'people have a', probability, '% chance of')
    print('having a matching birthday in their group.')
    print('That\'s probably more than you would think!')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:               # ❤️ When Ctrl-C is pressed, end the program
        print()
        print('Thanks for running my app')
        sys.exit()