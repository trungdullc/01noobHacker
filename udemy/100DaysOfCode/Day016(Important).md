# Day 016
```python
# Procedural Programming
# Going from one function to another: Fortran and Cobal and C

# Object Oriented Programming: C++, Java, Python, Java Script
#   attributes
#   methods
```

# Side Quest: turtle
```python
# Documentation: https://docs.python.org/3/library/turtle.html
# Colors: https://cs111.wellesley.edu/reference/colors

PS C:\Users\hackerdu> python -q
>>> import turtle
>>> dir(turtle)
['Canvas', 'Pen', 'RawPen', 'RawTurtle', 'Screen', 'ScrolledCanvas', 'Shape', 'TK', 'TNavigator', 'TPen', 'Tbuffer', 'Terminator', 'Turtle', 'TurtleGraphicsError', 'TurtleScreen', 'TurtleScreenBase', 'Vec2D', '_CFG', '_LANGUAGE', '_Root', '_Screen', '_TurtleImage', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__forwardmethods', '__func_body', '__loader__', '__methodDict', '__methods', '__name__', '__package__', '__spec__', '__stringBody', '_alias_list', '_make_global_funcs', '_screen_docrevise', '_tg_classes', '_tg_screen_functions', '_tg_turtle_functions', '_tg_utilities', '_turtle_docrevise', '_ver', 'addshape', 'back', 'backward', 'begin_fill', 'begin_poly', 'bgcolor', 'bgpic', 'bk', 'bye', 'circle', 'clear', 'clearscreen', 'clearstamp', 'clearstamps', 'clone', 'color', 'colormode', 'config_dict', 'deepcopy', 'degrees', 
'delay', 'distance', 'done', 'dot', 'down', 'end_fill', 'end_poly', 'exitonclick', 'fd', 'fillcolor', 'filling', 'forward', 'get_poly', 'get_shapepoly', 'getcanvas', 'getmethparlist', 'getpen', 'getscreen', 'getshapes', 'getturtle', 'goto', 'heading', 'hideturtle', 'home', 'ht', 'inspect', 'isdown', 'isfile', 'isvisible', 'join', 'left', 'listen', 'lt', 'mainloop', 'math', 'mode', 'numinput', 'onclick', 'ondrag', 'onkey', 'onkeypress', 'onkeyrelease', 'onrelease', 'onscreenclick', 'ontimer', 'pd', 'pen', 'pencolor', 'pendown', 'pensize', 'penup', 'pos', 'position', 'pu', 'radians', 'read_docstrings', 'readconfig', 'register_shape', 'reset', 'resetscreen', 'resizemode', 'right', 'rt', 'screensize', 'seth', 'setheading', 'setpos', 'setposition', 'settiltangle', 'setundobuffer', 'setup', 'setworldcoordinates', 'setx', 'sety', 'shape', 'shapesize', 'shapetransform', 'shearfactor', 'showturtle', 'simpledialog', 'speed', 'split', 'st', 'stamp', 'sys', 'textinput', 'tilt', 'tiltangle', 'time', 'title', 'towards', 'tracer', 'turtles', 'turtlesize', 'types', 'undo', 'undobufferentries', 'up', 'update', 'warnings', 'width', 'window_height', 'window_width', 'write', 'write_docstringdict', 
'xcor', 'ycor']
```

# Side Quest: turtle.Screen
```python
PS C:\Users\hackerdu> python -q
>>> import turtle
>>> help(turtle.Screen)
Help on function Screen in module turtle:

Screen()
    Return the singleton screen object.
    If none exists at the moment, create a new one and return it,
    else return the existing one.
```

# Side Quest: turtle.Turtle() and turtle.Screen()
```python
from turtle import Turtle, Screen   # orange box: class ⭐ in Visual Studio Code vs PyCharm

# Note: turtle starts off at 0.0, 0.0 in center vs pygame top left 0.0, 0.0 with up and down movements switched
if __name__ == "__main__":
    turtle = Turtle()
    # print(timmy)                  # <turtle.Turtle object at 0x000001BF27496D50>
    turtle.shape('turtle')          # 'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
    turtle.color("red", "green")
    turtle.forward(100)

    my_screen = Screen()            # purple box: method ⭐
    my_screen.canvheight            # blue box: attribute ⭐
    print(my_screen.canvheight)     # 300
    print(my_screen.canvwidth)      # 400
    my_screen.exitonclick()
```

# Side Quest: Add python packages using PyPi (Python Package Index) ⭐⭐⭐⭐⭐⭐⭐⭐⭐⭐
```python
# When looking for other people packages because you lazy: https://pypi.org/ ⭐
# https://pypi.org/search/?q=prettytable&o=
    # https://pypi.org/project/prettytable/

PS C:\Users\hackerdu> python -m venv venv
PS C:\Users\hackerdu> .\venv\Scripts\activate
(venv) PS C:\Users\hackerdu> pip install prettytable
# Note: Go into Visual Studio Code type import prettytable (see quick fix) or Ctrl + Shift + P (Python: Select Interpreter)
# Enter interpreter path...
# Find...
# venv > Scripts > python.exe
# Note: Bottom right of Visual Studio Code see venv
(venv) PS C:\Users\hackerdu> deactivate

# https://pypi.org/
# Documentation: https://pypi.org/project/prettytable/
from prettytable import PrettyTable

if __name__ == "__main__":
    table = PrettyTable()

    table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
    table.add_rows(
        [
            ["Adelaide", 1295, 1158259, 600.5],
            ["Brisbane", 5905, 1857594, 1146.4],
            ["Darwin", 112, 120900, 1714.7],
            ["Hobart", 1357, 205556, 619.5],
            ["Sydney", 2058, 4336374, 1214.8],
            ["Melbourne", 1566, 3806092, 646.9],
            ["Perth", 5386, 1554769, 869.4],
        ]
    )

    table.add_row(["Dallas", 1337, 1234567, 911])
    print(table.align)      # {'base_align_value': 'c', 'City name': 'c', 'Area': 'c', 'Population': 'c', 'Annual Rainfall': 'c'}
    table.align["City name"] = "l"
    print(table)

"""
+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
| Adelaide  | 1295 |  1158259   |      600.5      |
| Brisbane  | 5905 |  1857594   |      1146.4     |
| Darwin    | 112  |   120900   |      1714.7     |
| Hobart    | 1357 |   205556   |      619.5      |
| Sydney    | 2058 |  4336374   |      1214.8     |
| Melbourne | 1566 |  3806092   |      646.9      |
| Perth     | 5386 |  1554769   |      869.4      |
| Dallas    | 1337 |  1234567   |       911       |
+-----------+------+------------+-----------------+
"""
```

# Side Quest: Coffee Machine from Day015 but given starter code
```python
# Source: https://replit.com/@appbrewery/oop-coffee-machine-start
# Note: Given 4 files, basically change only main.py

# coffee_maker.py
class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
        print(f"Here is your {order.name} ☕️. Enjoy!")

# menu.py
class MenuItem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        options = ""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

# money_machine.py
class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False

# main.py
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Write Code below this point
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

if __name__ == "__main__":
    while is_on:
        options = menu.get_items()
        choice = input(f"What would you like? ({options}): ")
        if choice == "off":
            is_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)
            
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
```