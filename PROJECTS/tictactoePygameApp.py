"""
Main Purpose:
   Using numpy as the data type for the tic tac toe game using pygame
   TODO: Later figure out algorithm of how to win

Idea stolen from:
   https://pythongeeks.org/python-tic-tac-toe-game/

Level: Advanced
What I learned:
   Nothing yet need to look at code more

Created by HackerDu
"""

import numpy as np
import pygame
import math
import sys

class TicTacToe:
   def draw_board(self):
      """
      Method to call the other helper methods to draw the board
      """
      self.draw_lines()
      self.draw_figures()

   def draw_lines(self):
      """
      Method to draw the 2 horizontal and 2 vertical lines with pygame.draw.line()
      """
      pygame.draw.line(Screen, line_color, (0, 200), (600, 200), 10)
      pygame.draw.line(Screen, line_color, (0, 400), (600, 400), 10)
      pygame.draw.line(Screen, line_color, (200, 0), (200, 600), 10)
      pygame.draw.line(Screen, line_color, (400, 0), (400, 600), 10)

   def draw_figures(self):
      """
      Method that decides to draw circle or x depending on Board[row][col]
      """
      for col in range(COLUMNS):
         for row in range(ROWS):
            if Board[row][col] == 1:
               pygame.draw.circle(Screen, circle_color, (int(col * square_size + square_size / 2), int(row * square_size + square_size / 2)), circle_radius, circle_line_width)
            elif Board[row][col] == 2:
               pygame.draw.line(Screen, x_color, (col * square_size + offset, row * square_size + offset), (col * square_size + square_size - offset, row *square_size + square_size - offset), x_line_width)
               pygame.draw.line(Screen, x_color, (col * square_size + offset, row * square_size + square_size - offset), (col * square_size + square_size - offset, row * square_size + offset), x_line_width)

   def fullboard(self):
      for col in range(COLUMNS):
         for row in range(ROWS):
            if Board[row][col] == 0:
               return False
      return True

   def available_square(self, row, col):
      """
      Method checks if empty spot and returns a bool
      """
      is_available = Board[row][col] == 0
      return is_available

   def mark_square(self, row, col, player):
      """
      Method that assigns Board[row][col] to player 0 or 1
      """
      Board[row][col] = player

   def win(self, player):
      """
      Algorithm to check for win
      """
      verwin = self.vertical_win(player)
      horwin = self.horizontal_win(player)
      diagwin = self.diagonal_win(player)

      if verwin or horwin or diagwin:
         return True
      else:
         return False

   def vertical_win(self, player):
      """
      Method checks for vertical win is possible
      """
      for col in range(COLUMNS):
         if Board[0][col] == player and Board[1][col] == player and Board[2][col] == player:
            self.draw_vertical_line(col, player)
            return True
      return False

   def horizontal_win(self, player):
      """
      Method checks for horizontal win is possible
      """
      for row in range(ROWS):
         if Board[row][0] == player and Board[row][1] == player and Board[row][2] == player:
            self.draw_horizontal_line(row, player)
            return True
      return False

   def diagonal_win(self, player):
      """
      Method checks if diagonal win is possible
      """
      if Board[0][0] == player and Board[1][1] == player and Board[2][2] == player:
         self.draw_diagonal_line(player)
         return True
      elif Board[2][0] == player and Board[1][1] == player and Board[0][2] == player:
         self.draw_diagonal_line(player, False)
         return True
      else:
         return False

   def draw_vertical_line(self, col, player):
      """
      Method draws a vertical line
      """
      posX = col * square_size + square_size / 2

      if player == 1:
         pygame.draw.line(Screen, circle_color, (posX, 10), (posX, screen_height - 10), circle_line_width)
      else:
         pygame.draw.line(Screen,x_color, (posX, 10), (posX, screen_height - 10), circle_line_width)

   def draw_horizontal_line(self, row, player):
      """
      Method draws a horizontal line
      """
      posY = row * square_size + square_size/ 2

      if player == 1:
         pygame.draw.line(Screen, circle_color, (10, posY), (screen_width - 10, posY), circle_line_width)
      else:
         pygame.draw.line(Screen, x_color, (10, posY), (screen_width - 10, posY), circle_line_width)

   def draw_diagonal_line(self, player, down_diag=True):
      """
      Method draws a diagonal line
      """
      if down_diag:
         if player == 1:
            pygame.draw.line(Screen, circle_color, (25, 25), (screen_width - 25, screen_height - 25), x_line_width)
         else:
            pygame.draw.line(Screen, circle_color, (25, 25), (screen_width - 25, screen_height - 25), x_line_width)
      else:
         if player == 1:
            pygame.draw.line(Screen, circle_color, (25, screen_height - 25), (screen_width - 25, 25), x_line_width)
         else:
            pygame.draw.line(Screen, x_color, (25, screen_height - 25), (screen_width - 25, 25), x_line_width)

def main():
   global ROWS, COLUMNS, square_size, circle_radius, offset, circle_line_width, x_line_width, screen_width
   global screen_height, line_color, background_color, circle_color, x_color, Board, player, Screen

   # Note: This would of been better if coded in the class
   ROWS = 3
   COLUMNS = 3
   square_size = 200
   circle_radius = 60
   offset = 55
   circle_line_width= 15
   x_line_width = 25
   screen_width = COLUMNS * square_size
   screen_height = ROWS * square_size
   line_color = (0,0,0)
   background_color = (255,255,0)
   circle_color= (255,105,180)
   x_color = (255,0,0)

   # Initialize tictactoe object
   tictactoe = TicTacToe()

   Board = np.zeros((ROWS,COLUMNS))                # Data Structure that decides things
   pygame.init()
   pygame.display.set_caption("TIC TAC TOE GAME")
   Screen = pygame.display.set_mode((screen_width, screen_height))
   Screen.fill(background_color)
   tictactoe.draw_lines()
   pygame.display.update()
   player = 0
   gameover = False

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            sys.exit()

         if event.type == pygame.MOUSEBUTTONDOWN and not gameover:
            positiony = event.pos[1]
            row = int(math.floor(positiony / square_size))
            positionx = event.pos[0]
            col = int(math.floor(positionx / square_size))

            if player % 2 == 0:
               if tictactoe.available_square(row, col):
                  tictactoe.mark_square(row, col, 1)

                  if tictactoe.win(1):
                     gameover = True

                  player += 1

            else:
               if tictactoe.available_square(row, col):
                  tictactoe.mark_square(row, col, 2)

                  if tictactoe.win(2):
                     gameover = True

                  player += 1

            if tictactoe.fullboard():
               gameover = True

      tictactoe.draw_figures()
      pygame.display.update()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()