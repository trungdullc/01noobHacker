# Day 026
```python
# List and Dictionary Comprehensions (similer to C/C++ Ternary Operator but creates new list)
#   C/C++: Syntax: condition ? expression_if_true : expression_if_false;

NATO phonetic alphabet
https://en.wikipedia.org/wiki/NATO_phonetic_alphabet

Enter a word: Hacker
['Hotel', 'Alpha', 'Charlie', 'Kilo', 'Echo', 'Romeo']
```

# Side Quest: Create Lists using List Comprehension
```python
# Note: In Pycharm in Python Interpreter on right side has Special Char can view what in list and len

"""
Python Sequences:
    list
    range
    str
    tuple
"""

numbers: list[int] = [1, 2, 3]

def increase_by_1(old_list) -> list[int]:
    new_list = []
    
    for number in old_list:
        add_1 = number + 1
        new_list.append(add_1)
    
    return new_list
        
if __name__ == "__main__":
    print(increase_by_1(numbers))
    # Python List Comprehension
    print([number + 1 for number in numbers])               # Need [] or get <generator object <genexpr> at 0x0000021E83CAC110>
```

# Side Quest: Conditional List Comprehension (if on right)
```python
numbers: list[int] = [1,2,3]

if __name__ == "__main__":
    print([number * 2 for number in numbers if number >= 2])
```

# Side Quest: Challenge
```python
# Squaring Numbers using List Comprehension to create newlist called squared_numbers

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

if __name__ == "__main__":
    # squared_numbers = [pow(number, 2) for number in numbers]
    squared_numbers = [number ** 2 for number in numbers]
    print(squared_numbers)
```

# Side Quest: Challenge
```python
# Filtering Even Numbers using List comprehension
list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']

# List Comprehension to convert list[str]to list[int]
numbers = [int(string) for string in list_of_strings]

if __name__ == "__main__":
    result = [number for number in numbers if number & 1 == 0]      # 2 is 10 & 01 = 00 since both need be 1 to be 1
    print(result)
```

# Side Quest: Challenge
```python
# Data Overlap

file1.txt contains
1
2
3

file2.txt contains
2
3
4

# Job is to find overlap data and return as list[int] called result
if __name__ == "__main__":
    with open("file1.txt") as file1:
        list1 = file1.readlines()

    with open("file2.txt") as file2:
        list2 = file2.readlines()
        
    result = [int(number) for number in list1 if number in list2] 
```

# Side Quest: Apply List Comprehension to US States Game
```python
from turtle import Turtle, Screen
import pandas

IMAGE_PATH = "blank_states_img.gif"
CSV_PATH = "50_states.csv"
OUTPUT_FILE = "states_to_learn.csv"

guessed_correct_states = []

if __name__ == "__main__":
    screen = Screen()
    screen.title("U.S. States Game")

    screen.addshape(IMAGE_PATH)
    turtle = Turtle()
    turtle.shape(IMAGE_PATH)

    data = pandas.read_csv(CSV_PATH)

    all_states = data.state.to_list()

    while len(guessed_correct_states) < 50:
        answer_state = screen.textinput(title=f"{len(guessed_correct_states)}/50 States Correct", prompt="What's another state name?").title()     # Popup version of input()

        if answer_state == "Exit":
            missing_states = [state for state in all_states if state not in guessed_correct_states]     # New
        #     missing_states = []

        #     for state in all_states:
        #         if state not in guessed_correct_states:
        #             missing_states.append(state)
            
            print(f"DEBUG: {missing_states}")

            new_data_frame = pandas.DataFrame(missing_states)
            new_data_frame.to_csv(OUTPUT_FILE)

            break
        
        if answer_state in all_states:
            print("CORRECT")
            turtle_state = Turtle()
            turtle_state.hideturtle()
            turtle_state.penup()

            state_data = data[data.state == answer_state]
            turtle_state.setposition(state_data.x.item(), state_data.y.item())      
            turtle_state.write(answer_state)

    screen.exitonclick()
```

# Challenge: Dictionary Comprehension
```python
# Given a string called sentence seperate each word (delimiter = space) and length of word into dictionary called result
"""
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

Output:
{'What': 4, 'is': 2, 'the': 3, 'Airspeed': 8, 'Velocity': 8, 'of': 2, 'an': 2, 'Unladen': 7, 'Swallow?': 8}
"""

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

if __name__ == "__main__":
    result = {word:len(word) for word in sentence.split(" ")}       # Note: Default split() works also
    print(result)

"""
(venv) PS C:\Users\hackerdu> python -q
>>> sentence = "Hi there Buddy"
>>> dir(sentence)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> print(sentence)
Hi there Buddy
>>> help(sentence.split)
Help on built-in function split:

split(sep=None, maxsplit=-1) method of builtins.str instance
    Return a list of the substrings in the string, using sep as the separator string.

      sep
        The separator used to split the string.

        When set to None (the default value), will split on any whitespace
        character (including \\n \\r \\t \\f and spaces) and will discard
        empty strings from the result.
      maxsplit
        Maximum number of splits (starting from the left).
        -1 (the default value) means no limit.
    
    Note, str.split() is mainly useful for data that has been intentionally
    delimited.  With natural text that includes punctuation, consider using
    the regular expression module.
"""
```

# Challenge: Dictionary Comprehension 2
```python
# Goal: Convert °C to °F using formula (temp_c * 9/5) + 32 = temp_f
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

if __name__ == "__main__":
    weather_f = {key:(value * 9/5) + 32 for key,value in weather_c.items()}
    print(weather_f)
```

# Side Quest: Iterate thru dict
```python
student_dict = {
    "student": ["Hackerdu", "Bob", "Cici"],
    "score": [1337, 39, 69]
}

if __name__ == "__main__":
    for (key, value) in student_dict.items():
        print(key, value)
```

# Side Quest: Iterate thru panda DataFrame w/ .iterrows()
```python
import pandas

student_dict = {
    "student": ["Hackerdu", "Bob", "Cici"],
    "score": [1337, 39, 69]
}

if __name__ == "__main__":
    pandas_DF = pandas.DataFrame(student_dict)
    # print(pandas_DF)

    # Loop thru DataFrame ❤️
    for (index, row) in pandas_DF.iterrows():
        print(row["student"], row["score"])
```

# Side Quest: NATO phonetic alphabet (from above)
```python
# using nato_phonetic_alphabet.csv

import pandas

if __name__ == "__main__":
    # TODO 1: Create a dictionary in this format
    content = pandas.read_csv("nato_phonetic_alphabet.csv")
    alphabet_dict = {row["letter"]:row["code"] for (index, row) in content.iterrows()}
    # print(alphabet_dict)

    # TODO 2: Create a list of the phonetic code words from a word that the user inputs
    user_input: str = input("Enter a word: ").upper()
    output = [alphabet_dict[letter] for letter in user_input]
    print(output)
```