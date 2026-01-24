import smtplib          # For sending emails in Python
import datetime         # For changing date format

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
Note: Have to use this link to see App passwords: https://myaccount.google.com/u/1/apppasswords
"""

SENDER_EMAIL = "duprogramllc@gmail.com"
PASSWORD = "PLACEHOLDER"                                        # Password got from sender gmail
RECEIVER_EMAIL = "trungminhdu@gmail.com"

if __name__ == "__main__":
    # connection = smtplib.SMTP(host="smtp.gmail.com")          # smtp is from Sender (You)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()                                   # Transport Layer Security (Secure Connection)
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg="Subject:Hello\n\nTesting Message")
        # connection.close()