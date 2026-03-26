"""
Main Purpose:
    Create a solar system in turtle

Idea stolen from:
    https://pythongeeks.org/visualize-a-solar-system-with-python/

Level: Intermediate
What I learned:
    class inheritance
    default class property super().__init__(shape='circle')

Created by HackerDu
"""

import sys
import turtle
from math import *

# Inheritence from turtle module
class Planet(turtle.Turtle):
    def __init__(self,name,radius,color,sun):
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
        self.sun = sun
        
    def move(self):
        """
        Planet movement
        """

        x = self.radius*cos(self.angle)             # Angle in radians
        y = self.radius*sin(self.angle) 

        self.goto(self.sun.xcor()+x,self.sun.ycor()+y)

def main():
   root_window = turtle.Screen()
   root_window.tracer(50)

   # Note: instead of making global made part of Planet __init__(self, ..., sun)
   sun = turtle.Turtle()            # Turtle object for sun
   sun.shape('circle')              # Shape of sun
   sun.color('yellow')              # Colour of sun

   # Making planets, note the sun at end
   mercury = Planet("Mercury",40,'grey',sun)
   venus = Planet("Venus",80,'orange',sun)
   earth = Planet("Earth",100,'blue',sun)
   mars = Planet("Mars",150,'red',sun)
   jupiter = Planet("Jupiter",180,'brown',sun)
   saturn = Planet("Saturn",230,'pink',sun)
   uranus = Planet("Uranus",250,'light blue',sun)
   neptune = Planet("Neptune",280,'black',sun)

   # Adding planets to a list, note no sun
   planet_list = [mercury,venus,earth,mars,jupiter,saturn,uranus,neptune]

   while True:
      root_window.update()              # Updating the screen
      
      for planet in planet_list:
         planet.move()                  # Moving the elements of the list

      # Increase the angle by 0.0x radians
      mercury.angle += 0.05
      venus.angle += 0.03
      earth.angle += 0.01
      mars.angle += 0.007
      jupiter.angle += 0.02
      saturn.angle += 0.018
      uranus.angle += 0.016
      neptune.angle += 0.005

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()