# Day 021
```python
# Inheritance
class Animal:
    def __init__(self):
        self.number_of_eyes = 2
    
    def breath(self):
        print("Inhale, exhale.")

class Fish(Animal):                 # Inheritance
    def __init__(self):
        super().__init__()          # Copies parent methods and attributes
    
    def breath(self):               # Method Modifying vs Method Overriding
        super().breath()
        print("doing this underwater")

    def swim(self):
        print("Moving in water")

if __name__ == "__main__":
    garfield = Animial()
    garfield.breath()

    nemo = Fish()
    nemo.swim()
    nemo.breath()
```

# Side Quest: Snake game detecting food collision
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
            new_segment = Turtle(shape = "square")
            new_segment.penup()
            new_segment.color("green")
            new_segment.setposition(position)
            self.segments.append(new_segment)

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


import random

class Food(Turtle):                                         # New
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)      # Default: 20x20
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setposition(random_x, random_y)

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()                               # New

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    while not gameover:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Food collision detection
        if snake.head.distance(food) < 15:
            # print("Collision detected")
            food.refresh()

    screen.exitonclick()
```

# Side Quest: Snake game create a Scoreboard
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
            new_segment = Turtle(shape = "square")
            new_segment.penup()
            new_segment.color("green")
            new_segment.setposition(position)
            self.segments.append(new_segment)

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

class Scoreboard(Turtle):                                   # New
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        # self.write(f"Score: {self.score}", align = "center", font = ('Arial', 24, 'normal'))
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        # self.write(f"Score: {self.score}", align = "center", font = ('Arial', 24, 'normal'))
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

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
            # scoreboard.score += 1                       # Note: not work since not have access
            scoreboard.increase_score()
            food.refresh()

    screen.exitonclick()
```

# Side Quest: Snake Game, Game Over with Collision with Wall
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
            new_segment = Turtle(shape = "square")
            new_segment.penup()
            new_segment.color("green")
            new_segment.setposition(position)
            self.segments.append(new_segment)

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
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):                                            # New
        self.home()                                                 # Note: Need reset self.setposition(x = 0, y = 260)
        self.write("Game Over", align = ALIGNMENT, font = FONT)

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
        
        # Detect wall collision
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            gameover = "True"

    screen.exitonclick()
```

# Side Quest: Snake Game, increase/extend snake
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
            # new_segment = Turtle(shape = "square")
            # new_segment.penup()
            # new_segment.color("green")
            # new_segment.setposition(position)
            # self.segments.append(new_segment)
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

    def add_segment(self, position):            # New
        new_segment = Turtle(shape = "square")
        new_segment.penup()
        new_segment.color("green")
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):                           # New
        """
        Increase snake
        """
        self.add_segment(self.segments[-1].position())

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
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align = ALIGNMENT, font = FONT)

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
            snake.extend()                          # New
        
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            scoreboard.game_over()
            gameover = "True"

    screen.exitonclick()
```

# Side Quest: Snake Game, detect tail collision
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
        """
        Increase snake
        """
        self.add_segment(self.segments[-1].position())

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
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align = ALIGNMENT, font = FONT)

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
            scoreboard.game_over()
            gameover = "True"
        
        # Detect tail collision
        for segment in snake.segments:
            if segment == snake.head:
                pass
            # if snake.head.distance(segment) < 10 and segement != snake.head:
            elif snake.head.distance(segment) < 10:
                scoreboard.game_over()
                gameover = "True"

    screen.exitonclick()
```

# Side Quest: slicing python lists and tuples
```python
piano_keys: list[str] = ["a", "b", "c", "d", "e", "f", "g"]
paino_tuple: tuple[str] = ("do", "re", "mi", "fa", "so", "la", "ti")

if __name__ == "__main__":
    # slice list
    print(piano_key[2:5])               # Note: excludes last index
    print(piano_key[2:])
    print(piano_key[-1])
    print(piano_key[::2])
    print(piano_key[::-1])              # Reverse list

    # slice tuple
    print(piano_tuple[3:])
```

# Side Quest: Snake Game use slicing to simply code
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
        """
        Increase snake
        """
        self.add_segment(self.segments[-1].position())

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
        self.hideturtle()
        self.penup()
        self.setposition(x = 0, y = 260)
        self.color("white")
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.home()
        self.write("Game Over", align = ALIGNMENT, font = FONT)

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
            scoreboard.game_over()
            gameover = "True"
        
        # Detect tail collision
        for segment in snake.segments[1:]:                      # Slicing
            # if segment == snake.head:
                # pass
            # elif snake.head.distance(segment) < 10:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                gameover = "True"

    screen.exitonclick()
```