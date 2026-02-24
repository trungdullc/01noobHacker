import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
MONTHS = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

class CalendarMaker:
    def __init__(self):
        self.year = 0
        self.month = 0
        print('Calendar Maker')

    def set_year(self):
        while True:
            print('Enter the year for the calendar:')
            response = input('> ')

            if response.isdecimal() and int(response) > 0:
                self.year = int(response)
                break
            else:
                print('Please enter a numeric year, like 2023')
                continue
        
    def set_month(self):
        while True:
            print('Enter the month for the calendar, 1-12:')
            response = input('> ')

            if not response.isdecimal():
                print('Please enter a numeric month, like 3 for March')
                continue
            else:
                self.month = int(response)
                if 1 <= self.month <= 12:
                    break

            print('Please enter a number from 1 to 12')

    def getCalendarFor(self, year, month):
        calText = '' 
        calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'  # 34 spaces concat with MONTH folow by YEAR

        # Add days of week labels to calendar
        calText += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'

        weekSeparator = ('+----------' * 7) + '+\n'     # Add horizontal line string that separate weeks
        blankRow = ('|          ' * 7) + '|\n'          # The blank rows have ten spaces in between the | day separators:

        # Get date in the month (datetime module handles all the complicated calendar stuff)
        currentDate = datetime.date(year, self.month, 1)

        # Roll back currentDate until it is Sunday (weekday() returns 6 for Sunday, not 0)
        while currentDate.weekday() != 6:
            currentDate -= datetime.timedelta(days=1)

        while True:                                     # Loop over each week in the month
            calText += weekSeparator
            dayNumberRow = ''                           # dayNumberRow is row with the day number labels

            for i in range(7):
                dayNumberLabel = str(currentDate.day).rjust(2)
                dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
                currentDate += datetime.timedelta(days=1)   # Go to next day
            dayNumberRow += '|\n'                           # Add the vertical line after Saturday

            # Add the day number row and 3 blank rows to the calendar text
            calText += dayNumberRow
            for i in range(3):                              # (!) Try changing the 4 to a 5 or 10
                calText += blankRow

            # Check if we're done with the month
            if currentDate.month != month:
                break

        # Add the horizontal line at the very bottom of the calendar.
        calText += weekSeparator
        return calText

    def display_calendar(self,calText):
        print(calText)

    def save_to_file(self, calText):
        calendarFilename = 'calendar_{}_{}.txt'.format(self.year, self.month)

        with open(calendarFilename, 'w') as file:
            file.write(calText)

        print('Saved to ' + calendarFilename)