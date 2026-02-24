"""
Calendar Maker
Create monthly calendars, saved to a text file and fit for printing

Level: Intermediate
What I learned:
    Hardest part of the code is getCalendarFor() method
"""

from calendarMaker import CalendarMaker

def main():
    calendarmaker = CalendarMaker()
    calendarmaker.set_year()
    calendarmaker.set_month()

    calText: str = calendarmaker.getCalendarFor(calendarmaker.year, calendarmaker.month)
    calendarmaker.display_calendar(calText)

    calendarmaker.save_to_file(calText)

if __name__ == "__main__":
    main()