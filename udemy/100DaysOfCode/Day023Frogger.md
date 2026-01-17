# Day 023
```python
from turtle import Turtle, Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
import time

gameover = False

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player:
    pass

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    pass

FONT = ("Courier", 24, "normal")

class Scoreboard:
    pass

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    while not gameover:
        time.sleep(0.1)
        screen.update()

    screen.exitonclick()

# Note: turtle is 20x20 pixel (default)
# Note: cars are height=20, width=40
# Note: Each round cars go faster
# Note: No cars generated in top and bottom 50px of screen
# Note: Generate new car every 6th time game loop runs

# Game Plan
# Create and move turtle
# Create and move cars
# Detect collision with car
# Detect when turtle reaches other side
# Create a scoreboard
```

# Side Quest: Frogger, create and move turtle
```python
from turtle import Turtle, Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
import time

gameover = False

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):                               # Modify
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)                         # Face north
        self.setposition(STARTING_POSITION)

    def go_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)
    
    def go_left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    pass

FONT = ("Courier", 24, "normal")

class Scoreboard:
    pass

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()                               # New

    screen.listen()                                 # New
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_left, "Left")
    screen.onkey(player.go_right, "Right")

    while not gameover:
        time.sleep(0.1)
        screen.update()
    
    screen.exitonclick()
```

# Side Quest: Frogger, Create and move cars
```python
from turtle import Turtle, Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
import time
import random                                       # New

gameover = False

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def go_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)
    
    def go_left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):                                       # Modified
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_car(self):
        # reduce spawn rate, if get 1 spawn car
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)         # 40x20
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.setposition(300, random_y)
            self.all_cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)             # car.backwards(STARTING_MOVE_DISTANCE)
            car.fd(STARTING_MOVE_DISTANCE)

FONT = ("Courier", 24, "normal")

class Scoreboard:
    pass

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    car = CarManager()                          # New

    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_left, "Left")
    screen.onkey(player.go_right, "Right")

    while not gameover:
        time.sleep(0.1)
        screen.update()

        car.create_car()                        # New
        car.move_cars()                         # New

    screen.exitonclick()
```

# Side Quest: Frogger, detect collision with car
```python
from turtle import Turtle, Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
import time
import random

gameover = False

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.setposition(STARTING_POSITION)

    def go_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)
    
    def go_left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.setposition(300, random_y)
            self.all_cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.all_cars:
            car.setheading(180)
            car.fd(STARTING_MOVE_DISTANCE)

FONT = ("Courier", 24, "normal")

class Scoreboard:
    pass

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    cars = CarManager()

    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_left, "Left")
    screen.onkey(player.go_right, "Right")

    while not gameover:
        time.sleep(0.1)
        screen.update()

        cars.create_car()
        cars.move_cars()

        # Detect collision
        for car in cars.all_cars:
            if player.distance(car) < 20:
                # print("DEBUG: Collisiion Detected")
                gameover = True
                
    screen.exitonclick()
```

# Side Quest: Frogger, detect successful crossing and respawn
```python
from turtle import Turtle, Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
import time
import random

gameover = False

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        # self.setposition(STARTING_POSITION)             # Note: could do Player.go_to_start(self)
        self.go_to_start()

    def go_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)
    
    def go_left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            # self.setposition(STARTING_POSITION)         # Note: could do Player.go_to_start(self)
            self.go_to_start()
            return True
        return False

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.setposition(300, random_y)
            self.all_cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
        If car reaches finish line increase speed of cars
        """
        self.car_speed += MOVE_INCREMENT


FONT = ("Courier", 24, "normal")

class Scoreboard:
    pass

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    cars = CarManager()

    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_left, "Left")
    screen.onkey(player.go_right, "Right")

    while not gameover:
        time.sleep(0.1)
        screen.update()

        cars.create_car()
        cars.move_cars()

        for car in cars.all_cars:
            if player.distance(car) < 20:
                gameover = True
        
        # Detect successful crossing, can also Player.is_at_finish_line(self)
        # if player.ycor() > FINISH_LINE_Y:
            # print("DEBUG: Reached FINISH_LINE_Y")
        #    player.setposition(STARTING_POSITION)
        if player.is_at_finish_line():
            cars.level_up()

    screen.exitonclick()
```

# Side Quest: Frogger, create scoreboard and game over
```python
from turtle import Turtle, Screen
# from player import Player
# from car_manager import CarManager
# from scoreboard import Scoreboard
import time
import random

gameover = False

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("green")
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        self.setheading(90)
        self.fd(MOVE_DISTANCE)
    
    def go_left(self):
        self.setheading(180)
        self.fd(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.fd(MOVE_DISTANCE)
    
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            self.go_to_start()
            return True
        return False

    def go_to_start(self):
        self.setposition(STARTING_POSITION)

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.setposition(300, random_y)
            self.all_cars.append(new_car)
        else:
            pass

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):                               # Modify
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.current_level = 1
        self.update_scoreboard()

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def increase_level(self):
        self.current_level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setposition(-280, 250)
        self.write(f"Level: {self.current_level}", align="left", font=FONT)
        self.setposition(100, 250)
        self.write(f"Score: {self.score}", font=FONT)

    def game_over(self):
        self.setposition(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        
if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    cars = CarManager()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.go_up, "Up")
    screen.onkey(player.go_left, "Left")
    screen.onkey(player.go_right, "Right")

    while not gameover:
        time.sleep(0.1)
        screen.update()

        cars.create_car()
        cars.move_cars()

        for car in cars.all_cars:
            if player.distance(car) < 20:
                gameover = True
                scoreboard.game_over()          # New
        
        if player.is_at_finish_line():
            cars.level_up()
            scoreboard.increase_score()         # New
            scoreboard.increase_level()         # New

    screen.exitonclick()
```