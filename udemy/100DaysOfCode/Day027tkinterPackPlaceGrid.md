# Day 027
```python
# Documentation: https://docs.python.org/3/library/tkinter.html
# Creating Windows and Labels with tkinter

import tkinter as tk

window = tk.Tk()                                            # Create window (Screen in turtle)

window.title("Title goes here")                             # Set the title of the window
window.geometry("500x300")                                  # Set the size of the window
# window.minsize(width=500, height=300)

# Label
my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="top")                                  # place it on screen default centered


window.bind("<Button-1>", lambda event: window.destroy())   # Bind ANY mouse click to exit (like in turtle)
window.mainloop()                                           # Start GUI event loop (while True)
```

# Side Quest: Default arguments
```python
def add(a=0, b=0, c=0):                                     # Default arguments
    return a + b + c

if __name__ == "__main__":
    print(add(20, c=40))                                    # Override default arguments
```

# Side Quest: *args
```python
def add(*arg):                                              # Unlimited arguments as a tuple
    return sum(arg)

if __name__ == "__main__":
    print(add(20, 40))
```

# Side Quest: **kwargs
```python
# Many keyword arguments
def calculator(**kwargs):                               # Returns dict
    if "add" in kwargs:
        return add(*kwargs["add"])
    elif "subtract" in kwargs:
        return subtract(*kwargs["subtract"])
    return None

def add(*args):
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
```

# Side Quest: **kwargs used in class
```python
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]                              # Important: If make attribute not exist would crash
        self.model = kwargs["model"]                            # kwargs.get("model")       Always use get() returns None
    
    def __str__(self):
        return f"Driving my {self.make} {self.model}"

if __name__ == "__main__":
    my_car = Car(make="Toyota", model="Rav4")                   # Only see **kwargs not all the attributes
    print(my_car)
```

# Side Quest: Using both *arg, and **kwarg
```python
def print_me(num: int, *arg, **kwargs):
    print(num, arg, kwargs)

if __name__ == "__main__":
    print_me(1337, 69, 42, 777, 666, x=0, y=67)     # 1337 (69, 42, 777, 666) {'x': 0, 'y': 67}
```

# Side Quest: Buttons in tkinter
```python
import tkinter as tk

def button_clicked():
    print("I got clicked")

window = tk.Tk()

window.title("Title goes here")
window.geometry("500x300")

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"                               # Reassign since dict
my_label.config(text="New Text")                            # Same as above

# Create a Button class object
my_button = tk.Button(text="Press", command=button_clicked)
my_button.pack()

# window.bind("<Button-1>", lambda event: window.destroy())
window.mainloop()   
```

# Challenge: When press on button output in label instead of terminal (Mimic Javascript modifying html elements)
```python
import tkinter as tk

def button_clicked():
    # print("I got clicked")
    if my_label["text"] == "I am a label":                  # Reassign since dict
        my_label["text"] = "I got clicked"
    elif my_label["text"] == "I got clicked":
        my_label["text"] = "I got clicked again"
    else:
        my_label["text"] = "Stop that" 

window = tk.Tk()

window.title("Title goes here")
window.geometry("500x300")

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_button = tk.Button(text="Press", command=button_clicked)
my_button.pack()

# window.bind("<Button-1>", lambda event: window.destroy())
window.mainloop()   
```

# Side Quest: Entry class in tkinter
```python
import tkinter as tk

def button_clicked():
    user_input = input.get()                    # get()
    my_label["text"] = user_input
    print(user_input)

window = tk.Tk()

window.title("Title goes here")
window.geometry("500x300")

my_label = tk.Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack()

my_button = tk.Button(text="Press", command=button_clicked)
my_button.pack()

input = tk.Entry(width=10)
input.pack()

# window.bind("<Button-1>", lambda event: window.destroy())
window.mainloop()   
```

# Side Quest: Other tkinter Widgets(Text, Spinbox, Scale, Checkbutton, RadioButton, Listbox)
```python
from tkinter import *

def action():
    print("Do something")

def spinbox_used():
    print(spinbox.get())                                    # Gets the current value in spinbox

def scale_used(value):
    print(value)

def checkbutton_used():
    print(checked_state.get())                      # Prints 1 if On button checked, otherwise 0.

def radio_used():
    print(radio_state.get())

def listbox_used(event):
    print(listbox.get(listbox.curselection()))      # Gets current selection from listbox

window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

# Labels class
label = Label(text="This is old text")
label.config(text="This is new text")       # label["text"] = "This is new text"
label.pack()

# Button class
button = Button(text="Click Me", command=action)
button.pack()

# Entry class similar to input = text
"""
<form action="/action_page.php">
    <label for="fname">First name:</label>
    <input type="text" id="fname" name="fname"><br><br>
    <label for="lname">Last name:</label>
    <input type="text" id="lname" name="lname"><br><br>
    <input type="submit" value="Submit">
</form>
"""
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
print(entry.get())                              # Note: return string and print to terminal
entry.pack()

# Text class similar to textarea
"""
<textarea id="w3review" name="w3review" rows="4" cols="50">
Hackerdu was here
</textarea>
"""
text = Text(height=5, width=30)
text.focus()                                                # Puts cursor in textbox
text.insert(END, "Example of multi-line text entry.")       # Adds some text to begin with
print(text.get("1.0", END))                                 # Get's current value in textbox at line 1, character 0
text.pack()

# Spinbox class 
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale class
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton class
checked_state = IntVar()                            # variable to hold on to checked state, 0 is off, 1 is on.
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton class
radio_state = IntVar()              # Variable to hold on to which radio button value is checked.
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

# Listbox class
listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]

for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()
```

# Side Quest: tkinter layouts(pack(), place(), grid())
```python
# pack()            used for quick placement in program
# place(x=0, y=0)   has x and y value at top left different than turtle similar to pygame
# grid(row=0, column=0)     most popular, start at top left

# Important: can't use grid() and pack() in same program get error

# change padding
window.config(padx=20, pady=20)
```

# Side Quest: Miles to Kilometers Converter and how to change bg/fg colors
```python
# Title Mile to Km Converter
# Setup as grid()
#                   [InputBox]      Miles
# is equal to           0           Km
#                   [Calculate]

# Google: 1 mile = 1.609344 km

import tkinter as tk

def setup_window():
    window.title("Miles to Kilometer Converter")
    window.minsize(width=330, height=100)
    window.config(padx=50, pady=20)

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609344
    km_results_label["text"] = f"{km}"

if __name__ == "__main__":
    window = tk.Tk()
    setup_window()

    miles_input = tk.Entry(text="0", width=10, bg="light blue", fg="red")
    miles_label = tk.Label(text="Miles")
    is_equal_to_label = tk.Label(text="is equal to")
    km_results_label = tk.Label(text="0")
    km_label = tk.Label(text="Kilometers")
    calculate_button = tk.Button(text="Calculate", command=miles_to_km, bg="yellow", fg="#000000")      # Color chg w/ bg, fg

    miles_input.grid(row=0, column=1)
    miles_label.grid(row=0, column=2)
    is_equal_to_label.grid(row=1, column=0)
    km_results_label.grid(row=1, column=1)
    km_label.grid(row=1, column=2)
    calculate_button.grid(row=2, column=1)

    window.mainloop()
```