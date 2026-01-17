# Day 024
```python
# Note: On flaw on snake program is when exit game high score is gone
```

# Side Quest: Snake Game, add high score
```python
from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].setposition(new_x, new_y)

        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            snake.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            snake.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            snake.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            snake.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle(shape = "square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):                        # New
        for seg in self.segments:
            seg.setposition(1000,1000)      # set offscreen
        
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]        # Remember we cleared segments before is null value

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)


ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.score                    # New
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()                                    # New
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    # def game_over(self):
    #     self.home()
    #     self.write("Game Over", align = ALIGNMENT, font = FONT)

    def reset(self):                                    # New
        if self.score > self.high_score:
            self.high_score = self.score
        
        # Reset score to 0
        self.score = 0

        # Update scoreboard
        self.update_scoreboard()    

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while not gameover:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.refresh()
            snake.extend()
        
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            # scoreboard.game_over()
            # gameover = "True"
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                # scoreboard.game_over()
                # gameover = "True"
                scoreboard.reset()

    screen.exitonclick()
```

# Side Quest: Files (open, close, write)
```python
def read_file(text: str):           # Preferred,not need close()
    file = open(text)               # with open(text) as file
    contents = file.read()
    file.close()
    return contents

# Note: mode="w" will write new file if not exist
# Note: mode="a" will get error if file not exist and trying to append
def write_file(text: str):
    with open(text, mode="a") as file:
        file.write("New text has appeared!")

if __name__ == "__main__":
    read_file("my_file.txt")
    print(read_file)
    write_file("my_file.txt")
```

# Side Quest: Snake Game, read and write high score to a file
```python
from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()
            new_y = self.segments[seg_index - 1].ycor()
            self.segments[seg_index].setposition(new_x, new_y)

        self.segments[0].fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            snake.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            snake.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            snake.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            snake.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle(shape = "square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.setposition(1000,1000)
        
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)


ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.high_score = self.score
        with open("data.txt") as file:                  # New
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align = ALIGNMENT, font = FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score                # Note: order matters
            with open("data.txt", mode="w") as file:    # New
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()    

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while not gameover:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            scoreboard.increase_score()
            food.refresh()
            snake.extend()
        
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.reset()
            snake.reset()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.reset()

    screen.exitonclick()
```

# Side Quest: relative and absolute file path
```
# absolute is full path
/Users/hackerdu/Desktop/

# relative file path (depends in terminal where you currently at CWD (current/present working direct directory))
# Note: this matters alot expecially in pygame
./              current folder
./Documents/new.txt
../Programs/
```

# Side Quest: Mail Merge
```python
file_namelist = ["Hackerdu", "Bob", "Sam", "Roy"]           # instead of this, data.txt

# Saved to Output/ReadyToSend/letter_for_Hackerdu.txt
"""
Dear [name],
    You are invited to my birthday party this Saturday.

Hacker
"""

# builtins.str.strip()
(venv) PS C:\Users\hackerdu> python -c "help(str.strip)"  
Help on method_descriptor:

strip(self, chars=None, /)
    Return a copy of the string with leading and trailing whitespace removed.
    
    If chars is given and not None, remove characters in chars instead.

# TODO: Create a letter using starting_tetter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

if __name__ == "__main__":
    with open("invited_names.txt") as file:
        names: list[str] = file.readlines()

    # print(names)                                        # ['Hackerdu\n', 'Bob\n', 'Sam\n', 'Roy']

    with open("starting_letter.txt") as letter_file:
        letter_contents = letter_file.read()
    
    # print(letter_contents)

    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        # print(new_letter)

        # Note: Need Output\ReadyToSend folder already created or get FileNotFoundError
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as file:
            file.write(new_letter)
```