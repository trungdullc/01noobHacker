# Day 032
```python
# Email SMTP
# datetime module
```

# Side Quest: Send message in python
```python
import smtplib          # For sending emails in Python
# import datetime         # For changing date format

"""
Gmail:      smtp.gmail.com
Hotmail:    smtp.live.com
Outlook:    outlook.office365.com
Yahoo:      smtp.mail.yahoo.com

# Sending emails from gmail account
https://myaccount.google.com/
# Enable 2-Step Verification
Profile Picture (Top Right) > Manage your Google Account > Security > 2-Step Verification (Enable)> Turn On
                                                                    > App Passwords (Enable)(Hidden) > Select App > Other
                                                                    > bithday_wisher
    You don't have any app passwords
    To create a new app-specific password, type a name for it below
    App name: Python Mail > Create
    # Copy App password to use in python code (1 time) ⭐
    # Note: Default smtplib.SMTP uses port 25 not 587 or 465
    # smtplib.SMTP("smtp.gmail.com", port=587)

smtplib Documentation: https://docs.python.org/3/library/smtplib.html
Note: Have to use this link to see App passwords: https://myaccount.google.com/u/1/apppasswords ❤️
Important: To delete use same link above and click trash can ❤️❤️❤️❤️❤️
Note: Many things not in Documentation have to brute force code
"""

def open_secret():
    global PASSWORD
    with open("passwords/README.md") as file:
        PASSWORD = file.readline()                              # Similar to .env.local
                                                                # TODO: Improvement is to create encode/decode pass

SENDER_EMAIL = "duprogramllc@gmail.com"
PASSWORD = "PLACEHOLDER"                                        # Password got from sender gmail
RECEIVER_EMAIL = "trungminhdu@gmail.com"

if __name__ == "__main__":
    open_secret()                                               # TODO: Learn better way later

    # connection = smtplib.SMTP(host="smtp.gmail.com")          # smtp is from Sender (You)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()                                   # Transport Layer Security (Secure Connection)
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg="Subject:Hello\n\nTesting Message")
        # connection.close()
```

# Side Quest: datetime module
```python
# Documentation: https://docs.python.org/3/library/datetime.html
import datetime as dt

if __name__ == "__main__":
    current_time = dt.datetime.now()                # 2026-01-23 20:45:14.274074
    print(current_time)
    print(type(current_time))                       # <class 'datetime.datetime'>   datetime.py class datetime

    current_year = current_time.year                # Property
    print(current_year)

    print(dir(current_time))
    """
    ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
    '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', 
    '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', 
    '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 
    'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 
    'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 
    'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 
    'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 
    'utcoffset', 'utctimetuple', 'weekday', 'year']
    """

    day_of_week = current_time.weekday()
    print(day_of_week)                              # 4 where Monday = 0

    # Create a datetime object
    date_of_birth = dt.datetime(year=1337, month=12, day=25)    # ... means default arg not required
    print(date_of_birth)                            # 1337-12-25 00:00:00
```

# Side Quest: Quote Emailer
```python
import datetime as dt
import smtplib
import random

def open_secret():
    global PASSWORD
    with open("passwords/README.md") as file:       # Note: Will need to redo (due to my safety)
        PASSWORD = file.readline()
                                                               
SENDER_EMAIL = "duprogramllc@gmail.com"
PASSWORD = "PLACEHOLDER"
RECEIVER_EMAIL = "trungminhdu@gmail.com"

if __name__ == "__main__":
    open_secret()
    
    current_date = dt.datetime.now()
    day_of_week = current_date.weekday()        # Monday = 0, Sunday = 6

    if day_of_week == 4:
        with open("data/quotes.txt") as file:
            all_quotes = file.readlines()
            random_quote = random.choice(all_quotes)

        # Send message
        with smtplib.SMTP(host="smtp.gmail.com") as server:
            server.starttls()
            server.login(user=SENDER_EMAIL, password=PASSWORD)
            server.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg=f"Subject:Friday Motivation\n\n{random_quote}")
```

# Side Quest: Automate Happy Birthday Wisher
```python
"""
Given:
    birthdays.csv
    letter_1.txt
    letter_2.txt
    letter_3.txt

Goal: Randomly pick one of the template letters and replace [NAME] with name on birthdays.csv
"""
import datetime as dt
import smtplib
import random
import pandas                                       # read csv file easier without using with open()

def open_secret():
    global PASSWORD
    with open("passwords/README.md") as file:       # Note: Will need to redo (due to my safety)
        PASSWORD = file.readline()
CSV_SOURCE = "data/birthdays.csv"                                                               
SENDER_EMAIL = "duprogramllc@gmail.com"
PASSWORD = "PLACEHOLDER"

if __name__ == "__main__":
    open_secret()
    
    # TODO 1: Update birthdays.csv name, email, month, day

    # TODO 2: Import datetime to get current date and set as tuple
    current_date = dt.datetime.now()
    today_tuple = (current_date.month, current_date.day)

    # TODO 3: Import pandas to read birthdays.csv DataFrame as dict
    data_DF = pandas.read_csv(CSV_SOURCE)
    
    # TODO 4: Dict Comprehension the DataFrame
    birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data_DF.iterrows()}
    # print(type(new_dict))     # <class 'dict'> but it a dict[set, panda.DataFrame]

    # TODO 5: if logic to see if there date matches
    if today_tuple in birthdays_dict:
        # print("Happy Birthday")
        birthday_person = birthdays_dict[today_tuple]
        # print(type(birthday_person))                    # <class 'pandas.core.series.Series'>

        # TODO 6: Pick random letter using import random
        pick_number = random.randint(1,3)
        with open(f"data/letter_templates/letter_{pick_number}.txt") as file:
            contents = file.read()
            # TODO 7: Use str.replace() [name] with name
            replaced_contents = contents.replace("[NAME]", birthday_person["name"])
        # print(replaced_contents)

        # Note: Used Chatgpt to fix header not just Subject: only
        msg = (
            f"From: {SENDER_EMAIL}\n"
            f"To: {birthday_person['email']}\n"
            f"Subject: Happy Birthday\n"
            f"\n"  # <-- REQUIRED blank line separating headers from body
            f"{replaced_contents}"
        )
        
        # TODO 8: Send letter using import smtplib
        with smtplib.SMTP(host="smtp.gmail.com") as server:
            server.starttls()
            server.login(user=SENDER_EMAIL, password=PASSWORD)
            server.sendmail(from_addr=SENDER_EMAIL, to_addrs=birthday_person["email"], msg=msg)
    
    print("Message Sent")
```

# Tool to run python code on cloud ⭐⭐⭐❤️❤️❤️❤️❤️
```python
""" 3 Methods to run python code
Linux:
    crontab -e
    0 2 * * * /usr/local/bin/backup.sh
Windows (Task Scheduler):
    schtasks /create /tn "Backup" /tr "C:\backup.bat" /sc daily /st 02:00
Python (must keep program on):
import schedule
import time
import subprocess

def job():
    subprocess.run(["python3", "app.py"])

schedule.every().day.at("07:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
"""

Source: https://www.pythonanywhere.com/
Files > (Upload Files)
Console > Start a new console: Bash
    $ python3 app.py
    # Note: email provider blocking so copy https://support.google.com/mail/answer/[NUMBER]
    # I can't sign in to my email client
    # Click: https://www.google.com/accounts/DisplayUnlockCaptcha > Continue
    # Account access enabled
    $ python3 app.py
Tasks > Scheduled tasks:
    Daily, at 4:38 UTC, run python3 app.py > Create
    # Note: Since you free tier user has Expiry date
```