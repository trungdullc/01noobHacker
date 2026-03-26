"""
# Note: Not finished

Main Purpose:
    Learn turtle module vs tkinter or pygame
    See how another coder creates the Pong class
    Instead of creating seperate class for paddle and ball this user created in one single class
    Main focus is __init__(self) handles everyting

Idea stolen from:
    https://pythongeeks.org/python-pong-game-source-code/

Level: Advanced
What I learned:
    __init__(self) calls the the other methods to start the game in turtle
    self.root
    self.left_paddle
    self.right_paddle
    self.ball

Created by HackerDu
"""

import sys
import turtle

class PONG:
    def __init__(self):
        """
        Note: This function calls all the other methods ❤️
        """
        self.create_window()                        # Create the canvas
        self.create_left_paddle()                   # Create the objects
        self.create_right_paddle()
        self.create_ball()
        self.keys()                                 # Handle Movements
        self.game()                                 # Game Rules and collision detection

    def create_window(self):
        """
        Setup the canvas so things can be drawn on
        """
        self.root = turtle.Screen()
        self.root.title("PONG GAME")
        self.root.bgcolor("yellow")
        self.root.setup(width=600, height=400)
        self.root.tracer(n=0)

    def create_left_paddle(self):
        """
        Creates a red left paddle
        """
        self.left_paddle = turtle.Turtle()
        self.left_paddle.speed(0)
        self.left_paddle.shape('square')
        self.left_paddle.color('red')
        self.left_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.left_paddle.penup()
        self.left_paddle.goto(-280, 0)                      # Placement of left paddle

    def create_right_paddle(self):
        """
        Creates a white right paddle
        """
        self.right_paddle = turtle.Turtle()
        self.right_paddle.speed(0)
        self.right_paddle.shape('square')
        self.right_paddle.color('white')
        self.right_paddle.shapesize(stretch_wid=7, stretch_len=1.2)
        self.right_paddle.penup()
        self.right_paddle.goto(280, 0)                      # Placement of right paddle

    def create_ball(self):
        """
        Creates a green ball in the center with x and y directions
        """
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape('circle')
        self.ball.color('green')
        self.ball.penup()
        self.ball.goto(5,5)
        self.ball_direction_x = 0.2                         # dynamic x value
        self.ball_direction_y = 0.2                         # dynamic y value

    def left_paddle_up(self):
        """
        Update self.left_paddle.sety()
        """
        y_current = self.left_paddle.ycor()
        y_updated = y_current + 20
        self.left_paddle.sety(y_updated)

    def left_paddle_down(self):
        """
        Update self.left_paddle.sety()
        """
        y_current = self.left_paddle.ycor()
        y_updated = y_current - 20
        self.left_paddle.sety(y_updated)

    def right_paddle_up(self):
        """
        Update self.right_paddle.sety()
        """
        y_current = self.right_paddle.ycor()
        y_updated = y_current + 20
        self.right_paddle.sety(y_updated)

    def right_paddle_down(self):
        """
        Update self.right_paddle.sety()
        """
        y_current = self.right_paddle.ycor()
        y_updated = y_current - 20
        self.right_paddle.sety(y_updated)

    def keys(self):
        """
        Enable event listenerto listen to when certain key is pressed
        """
        self.root.listen()                                          # event Listener
        self.root.onkeypress(self.left_paddle_up, "w")              # call method left_addle_up when w is pressed
        self.root.onkeypress(self.left_paddle_down, "s")
        self.root.onkeypress(self.right_paddle_up, "Up")
        self.root.onkeypress(self.right_paddle_down, "Down")

    def game(self):
        while True:
            self.root.update()                                      # Similar to tkinter mainloop()

            # Update ball direction
            self.ball.setx(self.ball.xcor() + self.ball_direction_x)
            self.ball.sety(self.ball.ycor() + self.ball_direction_y)

            # Simple wall detection to change ball direction
            if self.ball.ycor() > 190:
                self.ball.sety(190)
                self.ball_direction_y *= -1

            if self.ball.ycor() < -190:
                self.ball.sety(-190)
                self.ball_direction_y *= -1

            if self.ball.xcor() > 260:
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1

            if self.ball.xcor() < -260:
                self.ball.goto(0, 0)
                self.ball_direction_x *= -1

            # Attempt at collision detection of ball and right paddle (not the best, focus on middle of paddle)
            if (self.ball.xcor() > 210) and (self.ball.xcor() < 220) and (
                    self.ball.ycor() < self.right_paddle.ycor() + 40 and self.ball.ycor() > self.right_paddle.ycor() - 40):
                self.ball.setx(210)
                self.ball_direction_x *= -1

            # Attempt at collision detection of ball and left paddle (not the best, focus on middle of paddle))
            if (self.ball.xcor() < -210) and (self.ball.xcor() > -220) and (
                    self.ball.ycor() < self.left_paddle.ycor() + 40 and self.ball.ycor() > self.left_paddle.ycor() - 40):
                self.ball.setx(-210)
                self.ball_direction_x *= -1

def main():
    PONG()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()