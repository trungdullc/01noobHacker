import datetime, random

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

class Birthday:
    def __init__(self):
        print('''Birthday Paradox

        The birthday paradox shows us that in a group of N people, the odds
        that two of them have matching birthdays is surprisingly large.
        This program does a Monte Carlo simulation (that is, repeated random
        simulations) to explore this concept.

        (It's not actually a paradox, it's just a surprising result.)\n
        ''')
    
    def validiate_input(self):
        while True:
            print('How many birthdays shall I generate? (Max 100)')
            response = input('> ')

            if response.isdecimal() and (0 < int(response) <= 100):
                number_of_BDays = int(response)
                break                           # User has entered a valid amount
            else:
                print("Please enter a digit between 0 and 100")
                response = input('> ')
                
        return number_of_BDays

    def getBirthdays(self, numberOfBirthdays):
        """Returns a list of number random date objects for birthdays."""
        birthdays = []

        for i in range(numberOfBirthdays):
            # The year is unimportant for our simulation, as long as all birthdays have the same year.
            startOfYear = datetime.date(2001, 1, 1)                             # Learn create datetime instance ❤️, 2001-01-01

            # Get a random day into the year:
            randomNumberOfDays = datetime.timedelta(random.randint(0, 364))     # Learn timedelta() ❤️, 1 days, 0:00:00
            birthday = startOfYear + randomNumberOfDays                         # 2001, 1, 2
            birthdays.append(birthday)
        return birthdays

    def getMatch(self, birthdays):
        """Returns the date object of a birthday that occurs more than once in the birthdays list."""
        if len(birthdays) == len(set(birthdays)):
            return None                                                         # All birthdays are unique, so return None.

        # Compare each birthday to every other birthday:
        for a, birthdayA in enumerate(birthdays):
            for b, birthdayB in enumerate(birthdays[a + 1 :]):                  # Note: Acts like a pointer to check everything else after ❤️❤️❤️❤️❤️
                if birthdayA == birthdayB:
                    return birthdayA                                            # Return the matching birthday.