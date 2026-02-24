# 100 Days of Code™: The Complete Python Pro Bootcamp
```
ASCII Art Generator: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type+Something+&x=none&v=4&h=4&w=80&we=false

FREE APIs:
    https://apilist.fun/ 
    https://publicapis.io/github-api
    https://free-apis.github.io/#/
    https://github.com/public-api-lists/public-api-lists

Folders
    data
    images
```

# CheatSheet: Used alot
```python
# Name stuff lowercase with _ like my_game unless class use Pascal case vs camel case (C/C++)
# docstring classes and methods and functions and write TODO 1:

# Rules: classes always use self but not external functions ! ❤️❤️❤️❤️❤️
# Rules: input always returns str ! ❤️❤️❤️❤️❤️
# Rules: / is float division in Python
# Rules: True/False is uppercase in Python
# Rules: No switch case in Python
# Scope Rules: After function done everything deleted !
# Score Rules: Must use global to access global variable ! ❤️❤️❤️❤️❤️

# LeetCode
# BruteForce first in Python
# Hash Map everything and bitwise operation

from builtins import print, len 
from typing import List
import string
import random
import tkinter as tk

python -m http.server 8000              # Module execution mode, http.server ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
python -m venv venv                     # Module execution mode, virtual environment ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
venv\Scripts\activate (for Windows)     source venv/bin/activate (for Linux/macOS)
(myenv) $ pip install requests
(myenv) $ deactivate
python -c "print(help())"               # Command-line execution mode ❤️❤️❤️❤️❤️
python -c "print(dir(print))"           # Command-line execution mode ❤️❤️❤️❤️❤️
python -q

import os

os.system("whoami")
os.system("pip3 install --user turtle")

# string
# letters = list(string.ascii_letters)                  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# numbers = list(string.digits)                         # '0123456789'
# symbols = list(string.punctuation)                    # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# builtins.str.strip()                                  # Used to remove \n when using .readlines()
# builtins.str.replace()                                # Used alot in templates
# "123".isdecimal()                                     # .isalpha(), .isalnum()

PLACEHOLDER = "[NAME]"
letter_contents = "Hey [NAME], your cool"
new_letter = letter_contents.replace(PLACEHOLDER, "Hacker")

my_string = "a,b,c"
my_string_list = my_string.split(",")                   # ['a', 'b', 'c']
my_string2 = ",".join(my_string_list)                   # "a,b,c"
my_string3 = "abc"
my_string_list2 = [char for char in my_string3]         # List comprehension ['a', 'b', 'c']

my_dict = {
    "Pikachu": "electric",
    "Bulbasaur": "water",
    "Charmander": "fire"
}

my_list = [key for (key,value) in my_dict.items()]              # ['Pikachu', 'Bulbasaur', 'Charmander']

# Dictionary Comprehension from a str
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"   
result = {word:len(word) for word in sentence.split(" ")}
# {'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}

# Dictionary Comprehension from a dict
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {key:(value * 9/5) + 32 for key,value in weather_c.items()}

# input
print(len(input("What is your name? ")))
is_extra: str = input("Do you want supersize it for $2 more. [Y]es or [N]o : ")[0].upper()

# random
friends: list[str] = ["HackerDu", "Bob", "Alice", "Charlie", "David"]

random_float_0to099: float = random.random() 
random_dice: int = random.randint(a=1, b=6)
random_buddy: str = random.choice(friends)              # random_buddy = friends[random.randint(0, len(friends) - 1)]

# for
fruits: list[str] = ["Apple", "Pear", "Peach"]

for index in range(len(fruits)):
    print(fruits[index], end=" ")
print()

for fruit in fruits:
    print(fruit, end=" ")
print()

for index, value in enumerate(fruits):
    print(f"{index}: {value}")                                      # print("{}: {}".format(index,value)) like C ❤️❤️❤️❤️❤️

# Multiple return
def name_title(f_name, l_name) -> tuple[str, str]:
    return f_name.title(), l_name.title()                           # ❤️❤️❤️❤️❤️

if __name__ == "__main__":
    first_name, last_name = name_title("hacker", "DU")              # ❤️❤️❤️❤️❤️
    print(f"Hi {first_name} {last_name}")

# **kwargs and *args
def print_me(num: int, *arg, **kwargs):
    print(num, arg, kwargs)

if __name__ == "__main__":
    print_me(1337, 69, 42, 777, 666, x=0, y=67)     # 1337 (69, 42, 777, 666) {'x': 0, 'y': 67} ❤️❤️❤️❤️❤️

# **kwargs and *args
def calculator(**kwargs):                               # **kwargs: Returns dict ❤️❤️❤️❤️❤️
    if "add" in kwargs:
        return add(*kwargs["add"])
    elif "subtract" in kwargs:
        return subtract(*kwargs["subtract"])
    return None

def add(*args):                                         # *arg: Returns tuple ❤️❤️❤️❤️❤️
    total = 0
    
    for num in args:
        total += num
    return total

def subtract(*args):
    if not args:
        return 0
    
    total = args[0]
    for num in args[1:]:
        total -= num
    return total

if __name__ == "__main__":
    print(calculator(add=(20, 40)))
    print(calculator(subtract=(100, 50)))

# class w/ **kwargs
class Car:
    def __init__(self, **kwargs):                               # ❤️❤️❤️❤️❤️
        self.make = kwargs["make"]                              # Important: If make attribute not exist would crash
        self.model = kwargs["model"]                            # kwargs.get("model")       Always use get() returns None
    
    def __str__(self):
        return f"Driving my {self.make} {self.model}"

if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Rav4")                   # Only see **kwargs not all the attributes
    print(my_car)

class Calculator:
    """ calculator program """                                  # __doc__: class docstring
    def __init__ (self, number: float):                         # python dunder method ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
        self.number = number

    def __str__ (self) -> str:                                  # python dunder method ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
        return f"Calculator(number={self.number})"

if __name__ == "__main__":
    my_calculator = Calculator(3)
    print(my_calculator)
    print(type(my_calculator))                                  # print(my_calculator.__class__)    <class '__main__.Calculator'>
    print(Calculator.__doc__)

# Inheritance alot with turtle module
class Animal:
    def __init__(self) -> None:
        print("Created an Animal")

    def breathe(self) -> None:
        print("breathing")

class Fish(Animal):                         # Inheritance w/ () instead of : like C++ ❤️❤️❤️❤️❤️
    def breathe(self) -> None:
        super().breathe()                   # super() from parent ❤️❤️❤️❤️❤️⭐⭐⭐⭐⭐
        print("underwater")

if __name__ == "__main__":                  # Note: if create __init__ for Fish it will override parent
    nemo = Fish()                           # Created an Animal
    nemo.breathe()                          # breathing

# global
global_counter = 0

def counter() -> bool:
    global global_counter                   # Note: Need global in python ❤️❤️❤️❤️❤️ Used alot in tkinter apps

    if global_counter != 3:
        global_counter += 1
        return False
    return True

while counter() != True:                    # while not counter()
    print("Hi")

# Open Files
def read_file(text: str):                               # Preferred,not need close()
    file = open(text)                                   # with open(text) as file
    contents = file.read()                              # .readlines()
    file.close()
    return contents

# Note: mode="w" will write new file if not exist (use try, except, else, finally with append or read)
# Note: mode="a" will get error if file not exist and trying to append
def write_file(text: str):
    with open(text, mode="a") as file:                      # ❤️❤️❤️❤️❤️
        file.write("New text has appeared!")

if __name__ == "__main__":
    read_file("my_file.txt")
    print(read_file)
    write_file("my_file.txt")

import json                                     # Module needed to use json functions

website: str = website_entry.get()              # New

new_data = {                                    # New dict
    website: {
        "email": email_entry.get(),
        "password": password_entry.get(),
    }
}

with open("data/data_password.json", mode="r") as file:             # Read mode
    data = json.load(file)                                          # New json() to read data from json file ⭐

    data.update(new_data)                                           # Note: Update json takes more steps ❤️❤️❤️❤️❤️
    with open("data/data_password.json", mode="w") as file:
        json.dump(data, file, indent=4)                             # Need overwrite/dump as well ⭐

# weather_data.csv
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny

import pandas               # pip3 install pandas
import csv                  # rarely used because have to do str manipulation

data = []

def read_data(file_location):
    with open(file_location, mode="r") as file:
        file_list = file.readlines()
    for line in file_list:
        data.append(line.strip())

def read_data_csv(file_location):
    """
    Manually modifying csv data painful, pandas library better for Data Anaylsis
    """
    temperatures_extracted = []

    with open(file_location, mode="r") as file:
        file_list = csv.reader(file)                # ❤️❤️
        # print(file_list)                          # <_csv.reader object at 0x0000020566FB7280>
        # print(list(file_list))                    # Note: need comment this out since list() does perm changes     

        for row in file_list:
            if row[1] != "temp":
                temperatures_extracted.append(int(row[1]))
        
        print(temperatures_extracted)               # [12, 14, 15, 14, 21, 22, 24]

def read_data_panda(file_location):
    file_data = pandas.read_csv(file_location)      # Note: No need 2 step with and readlines() ❤️❤️❤️❤️❤️
    print(file_data)                                # <class 'pandas.core.frame.DataFrame'>
    print(file_data["temp"])                        # <class 'pandas.core.series.Series'> is a column like a list

    data_dict = file_data.to_dict()                 # Serialize all columns w/ .to_dict() ❤️❤️❤️❤️❤️
    print(data_dict)
    """
    {
        'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 
        'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 
        'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
    }
    """

    print(data_dict["temp"])                            # {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}

    temp_list = file_data["temp"].to_list()             # .to_list() ❤️❤️❤️❤️❤️
    print(temp_list)                                    # [12, 14, 15, 14, 21, 22, 24]

    # built-in method from pandas.core.series.Series
    print(file_data["temp"].mean())
    print(file_data["temp"].max())

    # Get row data (2 syntax)
    print(file_data[file_data.day == "Monday"])         # print(file_data[file_data["day"]  == "Monday"])

if __name__ == "__main__":
    read_data("data/weather_data.csv")
    print(data)                                         # Note: painful to work with string like this
    # ['day,temp,condition', 'Monday,12,Sunny', 'Tuesday,14,Rain', 'Wednesday,15,Rain', 'Thursday,14,Cloudy', 'Friday,21,Sunny', 'Saturday,22,Sunny', 'Sunday,24,Sunny']
    read_data_csv("data/weather_data.csv")   
    read_data_panda("data/weather_data.csv")

    # Create a DataFrame from scratch instead of from csv (rarely done)
    data_dict = {
        "students": ["HackerDu", "Bob", "Chris"],
        "scores": [1337, 56, 12]
    }

    new_data = pandas.DataFrame(data_dict)              # ❤️❤️❤️

    # Convert pandas.DataFrame into csv
    new_data.to_csv("new_data.csv")                     # .to_csv() ❤️❤️❤️❤️❤️

    # Iterate thru panda DataFrame w/ .iterrows()
    student_dict = {
        "student": ["Hackerdu", "Bob", "Cici"],
        "score": [1337, 39, 69]
    }

    pandas_DF = pandas.DataFrame(student_dict)

    for (index, row) in pandas_DF.iterrows():           # .iterrows() not .items() like in regular dict for (key, value)
        print(row["student"], row["score"])

# Basics of tkinter: Label, Button, Entry
import tkinter as tk

def button_clicked():
    # print("I got clicked")
    user_input = input.get()                                # get() ❤️❤️❤️❤️❤️
    my_label["text"] = user_input
    print(user_input)

window = tk.Tk()                                            # Create window (Screen in turtle)

window.title("Title goes here")                             # Set the title of the window
window.geometry("500x300")                                  # Set the size of the window
# window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="top")                                   # .pack(side=), .place(), .grid(row=,column=)
my_label["text"] = "New Text"                               # Reassign since dict
my_label.config(text="New Text")                            # Same as above (used more bc can access more keywords)

# Button
my_button = tk.Button(text="Press", command=button_clicked)
my_button.pack()

correct_img = tk.PhotoImage(file="images/right.png")        # ❤️❤️❤️❤️❤️
correct_button = tk.Button(image=correct_img, highlightthickness=0, command=is_known)   # image instead of text
correct_button.grid(row=1, column=1)

# Entry
input_entry = tk.Entry(width=10)                            # Assign Entry as input ❤️❤️❤️❤️❤️
input_entry.insert(0, "Default")
input_entry.focus()                                         # Focus cursor here
input_entry.pack()
input_entry.delete(0, tk.END)                               # Clear entry

# Canvas class
canvas = tk.Canvas(width=200, height=224)
tomato_img = tk.PhotoImage(file="images/tomato.png")        # Note: Need convert image to PhotoImage class
canvas.create_image(102, 112, image=tomato_img)             # Based on canvas size
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)                                # Note: can't use .grid() and pack() in same program ❤️❤️❤️❤️❤️

# window.bind("<Button-1>", lambda event: window.destroy()) # Bind ANY mouse click to exit (like in turtle)
window.mainloop()                                           # Start GUI event loop (while True)

# Side Quest: columnspan
import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()

    r = tk.Label(bg="red", width=20, height=5)
    r.grid(row=0, column=0)

    g = tk.Label(bg="green", width=20, height=5)
    g.grid(row=1, column=1)

    b = tk.Label(bg="blue", width=40, height=5)         # Note: Had to increase width as well
    b.grid(row=2, column=0, columnspan=2)               # columnspan attribute ❤️❤️❤️❤️❤️
    b.config(highlightthickness=0)

    window.mainloop()

import tkinter.messagebox               # Go to Definition ❤️❤️❤️❤️❤️
tkinter.messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
tkinter.messagebox.askokcancel(title=website_entry.get(), message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")

import pyperclip                        # pip3 install pyperclip ❤️❤️❤️❤️❤️
# Copy password into clipboard w/ import pyperclip
pyperclip.copy(password)

import smtplib          # For sending emails in Python

"""
Gmail:      smtp.gmail.com
Hotmail:    smtp.live.com
Outlook:    outlook.office365.com
Yahoo:      smtp.mail.yahoo.com
"""

SENDER_EMAIL = "duprogramllc@gmail.com"                         # Used for botting because each sender need diff password
PASSWORD = "PLACEHOLDER"                                        # Password got from sender gmail
RECEIVER_EMAIL = "trungminhdu@gmail.com"

    # connection = smtplib.SMTP(host="smtp.gmail.com")          # smtp is from Sender (You)
    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()                                   # Transport Layer Security (Secure Connection)
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECEIVER_EMAIL, msg="Subject:Hello\n\nTesting Message")
        # connection.close()

import datetime as dt                           # For changing date format

current_time = dt.datetime.now()                # 2026-01-23 20:45:14.274074
print(current_time)
print(type(current_time))                       # <class 'datetime.datetime'>   datetime.py class datetime

current_year = current_time.year                # Property
print(current_year)

day_of_week = current_time.weekday()
print(day_of_week)                              # 4 where Monday = 0

print(dir(current_time))

# Create a datetime object
date_of_birth = dt.datetime(year=1337, month=12, day=25)    # ... means default arg not required ❤️❤️❤️❤️❤️
print(date_of_birth)                                        # 1337-12-25 00:00:00

import html                                                 # Remove HTML Character Entities

my_string = "In &quot;Mario Kart64&quot;, Walugigi is a playable character"
print(html.unescape(my_string))

# import time
time.sleep(seconds=1)                                       # Not good for tkinter
window.after_cancel(timer)                                  # Note: cancel a function if not fully run
timer = window.after(1000, count_down, count -1)            # Important: window.mainloop() messes up all while() ❤️❤️❤️❤️❤️

# Environment Variables
in terminal (temp) >    export OWM_API_KEY=PLACEHOLDER
online servers:         export OWN_APIKEY=PLACEHOLDER; python3 main.py

import os

api_key = os.environ.get("OWM_API_KEY")                              

# --- APIs ---
import requests             # pip3 install requests

API_KEY = "PLACEHOLDER"                                                     # Don't do this easy to be hacked

parameters = {"lat":MY_LAT, "lng":MY_LONG, "formatted":0,"appid": API_KEY}                   # if required: ❤️❤️❤️❤️❤️

headers = {
    "X-USER-TOKEN":TOKEN
}

response = requests.get(url="http://api.open-notify.org/iss-now.json", parems=parameters, headers=headers)      # Endpoint URL
# print(response)                                                           # <Response [200]>
response.raise_for_status()                                                 # Raise custom error if not 200

data = response.json()                                                      # Same as open url in browser
print(data)                 
# {'message': 'success', 'iss_position': {'longitude': '82.5180', 'latitude': '-40.3078'}, 'timestamp': 1769370910}  

longitude = data["iss_position"]["longitude"]

# SMS APP
from twilio.rest import Client              # pip3 install twilio

account_sid = "fromtwiliodashboard"
auth_token = "fromtwiliodashboard"          
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body="Hi there",
        from_="+11234567890",
        to="15558675310"                    # Note: have to be verified numbers on twilio
    )

print(message.sid)
print(message.status)

# CRUD API: 3 ways to read/load data from API
# RESTful Pokémon API
# Documentation: https://pokeapi.co/docs/v2

'''
Tip: Use a Python Formatter and Beautifier to view Data Type it is complex
BASE_ENDPOINT: https://pokeapi.co/api/v2/       # {"pokemon":"https://pokeapi.co/api/v2/pokemon/"}
Browser: https://pokeapi.co/api/v2/pokemon/ditto

# -=-= cURL in Linux, macOS, WSL =-=-
curl "https://pokeapi.co/api/v2/pokemon/ditto"

# Note: This will get error, header and HTTP GET method
curl -X GET "https://pokeapi.co/api/v2/pokemon/ditto" \
  -H "Content-Type: application/json"

# -=-= ⚠️ Window Powershell cURL is different than cURL ⚠️ =-=-
# curl is actually an alias for Invoke-WebRequest
# PS > Get-Alias curl
# Alias           curl -> Invoke-WebRequest

# Method 1: Expand the Content field
# (curl https://pokeapi.co/api/v2/pokemon/ditto).Content    
# (Invoke-WebRequest https://pokeapi.co/api/v2/pokemon/ditto).Content 

# -=-= Java Script (automatic beautify) =-=-
# Note: POST, PUT, DELETE only need method becuase fetch() defaults to GET ❤️❤️❤️
# Content-Type tells the server what you are sending but GET requests send no body
const response = await fetch('https://pokeapi.co/api/v2/pokemon/ditto');

const data = await response.json();
console.log(data);

# Pro: One-Liner (fetches data converts to .json() then console.log it) ❤️❤️❤️❤️❤️
fetch('https://pokeapi.co/api/v2/pokemon/ditto')
  .then(r => r.json())
  .then(console.log);

# Example when parameters matters
await fetch('/api/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    username: 'ash',
    password: 'pikachu'
  })
});

# JS Rule: await only works inside a async function (if trying build website)❤️
async function loadPokemon() {
  const response = await fetch(...);
}
'''

import requests
import json

URL_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/ditto"

if __name__ == "__main__":
    response = requests.get(url=URL_ENDPOINT)
    response.raise_for_status()

    data = response.json()                          # Raw json
    formatted_data = (json.dumps(data, indent=4))
    print(formatted_data)
```

# Main Side Quest: Quizzler App from above convert CLI to GUI with tkinter
# Master this
```python
import requests
import html                                 # unescape HTML character Entities
import tkinter

THEME_COLOR = "#375362"

parameters = {
    "amount":10, 
    "category":18, 
    "type":"boolean"
}

class Question:
    """
    class for question and answer
    """
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    """
    class for algorithm/logics of program
    """
    def __init__(self, q_list):                 # Note: data as q_list added as parameter to be passed ❤️❤️❤️❤️❤️
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        # self.check_answer(user_answer)
        return f"Q.{self.question_number}: {self.current_question.text}"
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower()[0] == correct_answer.lower()[0]:
            self.score += 1
            print("You got it right!")
            return True                                             # New
        else:
            print("That's wrong.")
            return False

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

class QuizInterface:                                                # New ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    """
    Interface of Quiz as a class
    """
    def __init__(self, quiz_brain: QuizBrain):
        self.window = tkinter.Tk()                                  # Remember: use self w/ classes
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Label Property
        self.score_label = tkinter.Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1)

        # Canvas Property
        # Note: Width on create_text text wraps it must be smaller than width of canvas ❤️❤️❤️❤️❤️
        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Amazing", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280) # Note: canvas uses fill not fg=
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        # Button Property
        true_image = tkinter.PhotoImage(file="images/right.png")    # Note: Don't need self because use 1 time
        false_image = tkinter.PhotoImage(file="images/wrong.png")
        self.true_button = tkinter.Button(image=true_image, background=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.false_button = tkinter.Button(image=false_image, background=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.quiz = quiz_brain                      # ❤️❤️❤️❤️❤️

        self.get_next_question()                    # Remove placeholder text
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background="white")                   # RESET canvas bg

        if self.quiz.still_has_questions():                             # Important
            self.score_label.config(text=f"Score: {self.quiz.score}")   # Important: uses configure
            question_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=question_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="Game Over") # Note: canvas uses itemconfigure not configure
            self.true_button.config(state="disabled")                   # Important: disable buttons ❤️❤️❤️❤️❤️
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True")) 

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            # Turn canvas bg green
            self.canvas.configure(background="green")
        else:
            # Turn canvas bg red
            self.canvas.configure(background="red")
        # RESET canvas bg color
        self.window.after(1000, self.get_next_question)

question_bank = []

if __name__ == "__main__":
    # Use API to get questions and answers
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    data = response.json()

    """
    {
        'response_code': 0, 
        'results': [
            {   'type': 'boolean', 
                'difficulty': 'medium', 
                'category': 'Science: Computers', 
                'question': 'MacOS is based on Linux.', 
                'correct_answer': 'False', 
                'incorrect_answers': ['True']}, 
            {'type': 'boolean', 'difficulty': 'easy', 'category': 'Science: Computers', 'question': 'Pointers were not used in the original C programming language; they were added later on in C++.', 'correct_answer': 'False', 'incorrect_answers': ['True']}
        ]
    }
    """

    question_data = data["results"]

    for question in question_data:
        question_text = html.unescape(question["question"])
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)                 # ❤️❤️❤️❤️❤️ call app logic and assign to quiz
    quiz_ui = QuizInterface(quiz)                   # New, pass logics into quiz interface ❤️❤️❤️❤️❤️

    # while quiz.still_has_questions():
    #     quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
```