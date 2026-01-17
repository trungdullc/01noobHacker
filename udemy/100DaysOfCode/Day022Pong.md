# Day 022
```python
# Create the screen height 600 and width 800 with black background
# Create and move a paddle
# Create another paddle
# Create the ball and make it move
# Detect collision with wall and bounce
# Detect collision with paddle
# Detect when paddle misses
# Keep score
```

# Side Quest: Pong Game, create blank screen
```python
from turtle import Turtle, Screen

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")

    screen.exitonclick()
```

# Side Quest: Snake Game, create and move a paddle
```python
from turtle import Turtle, Screen

def move_up():
    new_y = paddle.ycor() + 20
    paddle.setposition(paddle.xcor(), new_y)

def move_down():
    new_y = paddle.ycor() - 20
    paddle.setposition(paddle.xcor(), new_y)

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    # Create Right Paddle (don't turn it into class yet)
    # width = 20
    # height = 100
    # x_pos = 350
    # y_pos = 0
    paddle = Turtle()
    paddle.penup()
    paddle.setposition(350, 0)
    paddle.color("white")
    paddle.shape("square")
    paddle.shapesize(5, 1)

    # up/down move pixels by 20
    screen.listen()
    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")
    
    while not gameover:
        screen.update()
        
    screen.exitonclick()
```

# Side Quest: Create Paddle class and call 2nd paddle
```python
from turtle import Turtle, Screen

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        # paddle.setposition(350, 0)
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350,0))
    left_paddle = Paddle((-350,0))

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while not gameover:
        screen.update()

    screen.exitonclick()
```

# Side Quest: Create ball class and make it move
```python
from turtle import Turtle, Screen
import time

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        # paddle.setposition(350, 0)
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
    
    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.setposition(new_x, new_y) 

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350,0))
    left_paddle = Paddle((-350,0))
    ball = Ball()

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while not gameover:
        time.sleep(0.1)                         # New
        screen.update()
        ball.move()                             # New

    screen.exitonclick()
```

# Side Quest: Pong Game, modify ball bounce logic for top and bottom walls
```python
from turtle import Turtle, Screen
import time

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10                            # Need attributes
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move           # Need change hardcoded to dynamic w/ attributes
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y) 

    def bounce(self):
        # y needs to reverse
        self.y_move *= -1

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350,0))
    left_paddle = Paddle((-350,0))
    ball = Ball()

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while not gameover:
        time.sleep(0.1)
        screen.update()
        ball.move()

        # Detect top/bottom wall collision w/ ball
        if ball.ycor() > 280 or ball.ycor() < -280:
            # call bounce method
            ball.bounce()

    screen.exitonclick()
```

# Side Quest: Pong Game, detect collision with paddle
```python
from turtle import Turtle, Screen
import time

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y) 

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):                         # New
        self.x_move *= -1

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350,0))
    left_paddle = Paddle((-350,0))
    ball = Ball()

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while not gameover:
        time.sleep(0.1)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Detect collision with right paddle
        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < - 320:
            # print("Ball collided w/ right paddle")
            ball.bounce_x()

    screen.exitonclick()
```

# Side Quest: Pong Game, detect when ball goes out of bounds and reset ball position to center going opposite direction
```python
from turtle import Turtle, Screen
import time

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y) 

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.bounce_x()
        self.setposition((0,0))

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350,0))
    left_paddle = Paddle((-350,0))
    ball = Ball()

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while not gameover:
        time.sleep(0.1)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < - 320:
            ball.bounce_x()

        # Detect ball went out of bounds, later need do seperate to determine which player gets a point
        if ball.xcor() > 380 or ball.xcor() < -380:
            print("Ball went out of bounds")
            ball.reset_position()

    screen.exitonclick()
```

# Side Quest: Pong Game, create Scoreboard class
```python
from turtle import Turtle, Screen
import time

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.setposition(position)
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y) 

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
    
    def reset_position(self):
        self.bounce_x()
        self.setposition((0,0))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.left_score = 0                             # Note: Better to have attributes
        self.right_score = 0
        self.update_score()
    
    def update_score(self):                             # New
        self.clear()
        self.setposition((-100, 200))
        self.write(self.left_score, align = "center", font = ("Courier", 70, "normal"))
        self.setposition((100, 200))
        self.write(self.right_score, align = "center", font = ("Courier", 70, "normal"))

    def increase_left_score(self):
        self.left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.right_score += 1
        self.update_score()

gameover = False

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width = 800, height = 600)
    screen.bgcolor("black")
    screen.title("Pong Game")
    screen.tracer(0)

    right_paddle = Paddle((350,0))
    left_paddle = Paddle((-350,0))
    ball = Ball()
    scoreboard = Scoreboard()                   # New

    screen.listen()
    screen.onkeypress(right_paddle.move_up, "Up")
    screen.onkeypress(right_paddle.move_down, "Down")

    screen.onkeypress(left_paddle.move_up, "w")
    screen.onkeypress(left_paddle.move_down, "s")

    while not gameover:
        time.sleep(0.1)
        screen.update()
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < - 320:
            ball.bounce_x()

        if ball.xcor() > 380:
            ball.reset_position()
            scoreboard.increase_left_score()

        if ball.xcor() < -380:
            ball.reset_position()
            scoreboard.increase_right_score()

    screen.exitonclick()
```