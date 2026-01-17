# Day 025
```python
# Create a excel in Google Sheets but Download as weather_data.csv
day,temp,condition
Monday,12,Sunny
Tuesday,14,Rain
Wednesday,15,Rain
Thursday,14,Cloudy
Friday,21,Sunny
Saturday,22,Sunny
Sunday,24,Sunny
```

# Side Quest: csv vs pandas
```python
PS C:\Users\hackerdu> python -m venv venv
PS C:\Users\hackerdu> .\venv\Scripts\activate
(venv) PS C:\Users\hackerdu> pip install pandas
# Note: Go into Visual Studio Code type import pandas (see quick fix) or Ctrl + Shift + P (Python: Select Interpreter)
# Enter interpreter path...
# Find...
# venv > Scripts > python.exe
# Note: Bottom right of Visual Studio Code see venv
(venv) PS C:\Users\hackerdu> deactivate

# Documentation: https://pypi.org/project/pandas/#documentation
# Extra: https://pandas.pydata.org/docs/

import pandas                                   # pip3 install pandas
import csv

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
        file_list = csv.reader(file)
        # print(file_list)               # <_csv.reader object at 0x0000020566FB7280>
        # print(list(file_list))        # Note: need comment this out since list() does perm changes     

        for row in file_list:
            if row[1] != "temp":
                temperatures_extracted.append(int(row[1]))
        
        print(temperatures_extracted)   # [12, 14, 15, 14, 21, 22, 24]

def read_data_panda(file_location):
    file_data = pandas.read_csv(file_location)      # Note: No need 2 step with and readlines()
    print(file_data)
    """
            day  temp condition
    0     Monday    12     Sunny
    1    Tuesday    14      Rain
    2  Wednesday    15      Rain
    3   Thursday    14    Cloudy
    4     Friday    21     Sunny
    5   Saturday    22     Sunny
    6     Sunday    24     Sunny
    """
    print(file_data["temp"])

if __name__ == "__main__":
    read_data("weather_data.csv")
    # Note: painful to work with string like this
    print(data)                         # ['day,temp,condition', 'Monday,12,Sunny', 'Tuesday,14,Rain', 'Wednesday,15,Rain', 'Thursday,14,Cloudy', 'Friday,21,Sunny', 'Saturday,22,Sunny', 'Sunday,24,Sunny']
    read_data_csv("weather_data.csv")   
    read_data_panda("weather_data.csv")
    """
    [
        ['day', 'temp', 'condition'], 
        ['Monday', '12', 'Sunny'], 
        ['Tuesday', '14', 'Rain'], 
        ['Wednesday', '15', 'Rain'], 
        ['Thursday', '14', 'Cloudy'], 
        ['Friday', '21', 'Sunny'], 
        ['Saturday', '22', 'Sunny'], 
        ['Sunday', '24', 'Sunny']
    ]
    """
```

# Side Quest: pandas Data Types: DataFrames & Series
```python
import pandas

if __name__ == "__main__":
    data = pandas.read_csv("weather_data.csv")
    # Note: pandas 2 primary data sructures are Series (1-D) and DataFrame(2-D)
    print(type(data))                           # <class 'pandas.core.frame.DataFrame'>
    print(data["temp"])
    print(type(data["temp"]))                   # <class 'pandas.core.series.Series'> is a column like a list

    data_dict = data.to_dict()
    print(data_dict)                            # Serialize
    """
    {
        'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 
        'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 
        'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}
    }
    """
    print(data_dict["temp"])                    # {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}

    temp_list = data["temp"].to_list()
    print(temp_list)                            # [12, 14, 15, 14, 21, 22, 24]

    # Challenge: Find average temp of list
    print(sum(temp_list)/len(temp_list))        # 17.428571428571427

    # built-in method from pandas.core.series.Series
    print(data["temp"].mean())                  # 17.428571428571427

    # Challenge: Find max value using pandas.core.series.Series
    print(data["temp"].max())                   # 24
    print(data.temp.max())                      # Note: pandas automatically converted column as a attribute

    # Challenge: Get row data
    print(data[data.day == "Monday"])           # print(data[data["day"]  == "Monday"])
    #       day  temp condition
    # 0  Monday    12     Sunny
    
    # Challenge: Get row data where temp was highest
    print(data[data.temp == data.temp.max()])
    #       day  temp condition
    # 6  Sunday    24     Sunny

    # Create a DataFrame from scratch instead of from csv
    data_dict = {
        "students": ["HackerDu", "Bob", "Chris"],
        "scores": [1337, 56, 12]
    }

    new_data = pandas.DataFrame(data_dict)
    print(new_data)
    """
    0  HackerDu    1337
    1       Bob      56
    2     Chris      12
    """

    # Challenge: convert this pandas.DataFrame into csv ❤️
    new_data.to_csv("new_data.csv")
```

# Side Quest: Great Squirrel Census Data Analysis with pandas
```python
# 2018 Central Park Squirrel Census - Squirrel Data
# Source: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw/about_data
#   Click Export > Download File as CSV
# File: 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260116.csv

# Challenge: Extract data and output squirrel_count.csv of
#   , Primary Fur Color, Count

import pandas

if __name__ == "__main__":
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260116.csv")    # Created a DataFrame
    # print(data)
    print(set(data["Primary Fur Color"]))                                                       # {'Cinnamon', nan, 'Black', 'Gray'}
    gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
    # print(gray_squirrels)                                                                     # [2473 rows x 31 columns]
    print(len(gray_squirrels))                                      # print(gray_squirrels.__len__())

    cinnamon_squirrels = data[data["Primary Fur Color"] == "Cinnamon"]
    black_squirrels = data[data["Primary Fur Color"] == "Black"]
    print(len(cinnamon_squirrels))
    print(len(black_squirrels))

    # Construct DataFrame from results
    data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
    }

    # print(data_dict)

    # Convert Python dictionary into panda DataFrame
    panda_DF = pandas.DataFrame(data_dict)
    # print(panda_DF)

    # Export it as panda_color_count.csv
    panda_DF.to_csv("panda_color_count.csv")
```

# Side Quest: US States Game, get x and y values of all 50 states and record in 50_states.csv
```python
# Site: https://www.sporcle.com/
#   Trivia Quiz Site, search state
# Link: https://www.sporcle.com/games/g/states

# Files used for this program
# 50_states.csv
# blank_states_img.gif                  # turtle not work with img or png

from turtle import Turtle, Screen

def get_mouse_click_coor(x, y):
    print(x, y)

IMAGE_PATH = "blank_states_img.gif"

if __name__ == "__main__":
    screen = Screen()
    screen.title("U.S. States Game")

    screen.addshape(IMAGE_PATH)                 # Note: Required this step
    turtle = Turtle()
    turtle.shape(IMAGE_PATH)

    screen.onscreenclick(get_mouse_click_coor)
    screen.mainloop()
    # screen.exitonclick()
```

# Side Quest: US States Game
```python
from turtle import Turtle, Screen
import pandas

# def get_mouse_click_coor(x, y):
#     print(x, y)

IMAGE_PATH = "blank_states_img.gif"
CSV_PATH = "50_states.csv"
OUTPUT_FILE = "states_to_learn.csv"

guessed_correct_states = []                     # Using this and len don't need counter and gameover flag

if __name__ == "__main__":
    screen = Screen()
    screen.title("U.S. States Game")

    screen.addshape(IMAGE_PATH)                 # Note: Required this step
    turtle = Turtle()
    turtle.shape(IMAGE_PATH)

    # screen.onscreenclick(get_mouse_click_coor)
    # screen.mainloop()

    data = pandas.read_csv(CSV_PATH)
    # print(data.state)                         # Check if get correct column
    all_states = data.state.to_list()           # Save to list ❤️

    while len(guessed_correct_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_correct_states)}/50 States Correct", prompt="What's another state name?").title()     # Popup version of input()
        # print(answer_state)

        # Force quit and give all answers
        if answer_state == "Exit":
            missing_states = []

            for state in all_states:
                if state not in guessed_correct_states:
                    missing_states.append(state)
            
            print(f"DEBUG: {missing_states}")
            # Generates states_to_learn.csv
            new_data_frame = pandas.DataFrame(missing_states)
            new_data_frame.to_csv(OUTPUT_FILE)

            break
        
        if answer_state in all_states:
            # if correct get turtle to write state in correct x,y
            print("CORRECT")
            turtle_state = Turtle()
            turtle_state.hideturtle()
            turtle_state.penup()

            state_data = data[data.state == answer_state]
            # turtle_state.setposition(state_data.x, state_data.y)                  # Error
            turtle_state.setposition(state_data.x.item(), state_data.y.item())      
            # turtle_state.write(state_data.state)
            turtle_state.write(answer_state)                                        # turtle_state.write(state_data.state.item())

    screen.exitonclick()

# Note: This program can be used to teach languages, anatomy, other countries
```