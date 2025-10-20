# Level 15

## Previous Flag
```
http://www.pythonchallenge.com/pc/return/uzi.html
```

## Goal
Given picture of calender of year 1??6 and month of Jan with 26 circled on a monday

## What I learned
```
A leap year is a year in which an extra day is added to keep the calendar year synchronized with the astronomical year (the time it takes Earth to orbit the Sun).

Normally, a year has 365 days.
A leap year has 366 days (an extra day in February, making it 29 days instead of 28).

How to determine a leap year

Step 1: Divisible by 4?
  If yes, go to step 2.
  If no, it’s not a leap year.

Step 2: Divisible by 100?
  If yes, go to step 3.
  If no, it is a leap year.

Step 3: Divisible by 400?
  If yes, it is a leap year.
  If no, it is not a leap year.

Why it exists
Earth takes roughly 365.2422 days to orbit the Sun. Without leap years, our calendar would slowly drift out of sync with the seasons. Leap years fix this drift.
```

## Solution
```
Browser: http://www.pythonchallenge.com/pc/return/uzi.html

View Page Source

<html>
<head>
  <title>whom?</title>
  <link rel="stylesheet" type="text/css" href="../style.css">
</head>
<body>
<br><center>
<!-- he ain't the youngest, he is the second --> 👀
<img src="screen15.jpg"><br>
</body>
</html>

<!-- todo: buy flowers for tomorrow --> 👀

AsianHacker-picoctf@webshell:~$ python3 -q ⌨️
>>> import datetime, calendar
>>> dir(datetime) ⌨️
['MAXYEAR', 'MINYEAR', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
>>> dir(calendar) ⌨️
['Calendar', 'EPOCH', 'FRIDAY', 'February', 'HTMLCalendar', 'IllegalMonthError', 'IllegalWeekdayError', 'January', 'LocaleHTMLCalendar', 'LocaleTextCalendar', 'MONDAY', 'SATURDAY', 'SUNDAY', 'THURSDAY', 'TUESDAY', 'TextCalendar', 'WEDNESDAY', '_EPOCH_ORD', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_colwidth', '_locale', '_localized_day', '_localized_month', '_monthlen', '_nextmonth', '_prevmonth', '_spacing', 'c', 'calendar', 'datetime', 'day_abbr', 'day_name', 'different_locale', 'error', 'firstweekday', 'format', 'formatstring', 'isleap', 'leapdays', 'main', 'mdays', 'month', 'month_abbr', 'month_name', 'monthcalendar', 'monthrange', 'prcal', 'prmonth', 'prweek', 'repeat', 'setfirstweekday', 'sys', 'timegm', 'week', 'weekday', 'weekheader']
>>> help(datetime) ⌨️
>>> help(calendar) ⌨️

External Documentation:
  https://docs.python.org/3/library/datetime.html ❤️
  https://docs.python.org/3/library/calendar.html ❤️

AsianHacker-picoctf@webshell:~$ vi pythonScript.py ⌨️
AsianHacker-picoctf@webshell:~$ cat pythonScript.py ⌨️
#!/usr/bin/python3
import datetime, calendar

monday = 0
sunday = 6

for year in range(1006, 2016, 10):
  if datetime.datetime(year, 1, 26).weekday() == monday:
    if (calendar.isleap(year)):
      print("isLeap: ", year)

AsianHacker-picoctf@webshell:~$ chmod u+x pythonScript.py 
AsianHacker-picoctf@webshell:~$ ./pythonScript.py 
isLeap:  1176
isLeap:  1356
isLeap:  1576
isLeap:  1756
isLeap:  1976

# Think buy flowers for tommorow looking at 26 + 1
# Think he aint the youngest but second closer to current year
Google: Jan 27 1756 who was born ⌨️
Wolfgang Amadeus Mozart 👀

Browser: http://www.pythonchallenge.com/pc/return/mozart.html 🔐
```

## Flag
http://www.pythonchallenge.com/pc/return/mozart.html

## Continue
[Continue](./Level16.md)