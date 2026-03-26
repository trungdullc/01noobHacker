"""
Main Purpose:
    Solves a random sudoku puzzle
    TODO: Later figure out algorithm and data type grid
    
Idea stolen from:
    https://pythongeeks.org/python-sudoku-solver-using-backtracking/

Level: Advanced
What I learned:
    Place variables that change in __init()

Created by HackerDu
"""

import sys
import pygame
import requests

class Soduku:
    WIDTH = 550                                 # Note: These are constant, place variables that change in __init()
    BACKGROUND_COLOR = (245,251,250)
    BUFFER = 5

    def __init__(self):
        self.solving = 0                        # Note: Best to put global variables inside __init__()

        # Note: Old need find new working link
        # response_API = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
        response_API = requests.get("https://sugoku.onrender.com/board?difficulty=easy")

        # DEBUG to see what type(response_API)
        print(response_API)                     # <Response [200]>
        
        # Note: Will be random each time due to API but type is dict
        print(response_API.json()) 
        # {'board': [[0, 8, 0, 3, 0, 0, 0, 4, 0], [0, 0, 3, 0, 0, 0, 7, 8, 9], [0, 5, 9, 2, 0, 0, 0, 0, 0], [2, 0, 4, 0, 0, 7, 0, 0, 8], [0, 6, 0, 8, 0, 0, 0, 7, 0], [7, 9, 8, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 4, 2, 0, 6, 7], [0, 4, 2, 0, 6, 0, 9, 0, 1], [0, 7, 0, 1, 0, 5, 0, 0, 3]]}

        # Note: Best to place self.grid_board inside def __init__() to act as global variable
        self.grid_board = response_API.json()['board']
    
        # Note: Logic not even used
        # original_grid = [[self.grid_board[x][y] for y in range(len(self.grid_board[0]))] for x in range(len(self.grid_board))]

        # Setting pygame window
        root_window = pygame.display.set_mode((self.WIDTH, self.WIDTH))
        pygame.display.set_caption("Sudoku Solver")
        root_window.fill(self.BACKGROUND_COLOR)                          # Filling background color

        Font = pygame.font.SysFont('Comic Sans MS', 35)             # Declaring font
        
        # Creating grid
        for i in range(0,10):
            if i % 3 == 0:
                pygame.draw.line(root_window, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 4 )
                pygame.draw.line(root_window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 4 )

            pygame.draw.line(root_window, (0,0,0), (50 + 50*i, 50), (50 + 50*i ,500 ), 2 )
            pygame.draw.line(root_window, (0,0,0), (50, 50 + 50*i), (500, 50 + 50*i), 2 )
        pygame.display.update()
        
        # Placing elements on the board
        for i in range(0, len(self.grid_board[0])):
            for j in range(0, len(self.grid_board[0])):
                if(0<self.grid_board[i][j]<10):
                    Value_board = Font.render(str(self.grid_board[i][j]), True,(52, 31, 151))
                    root_window.blit(Value_board, ((j+1)*50 + 15, (i+1)*50 ))
        pygame.display.update()

        # Runs soduku_solver method
        self.sudoku_solver(root_window)
        
        while True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            
    def is_empty(self, number):
        """
        Function to check if grid position is empty or not
        """
        if number == 0:
            return True
        return False

    def is_valid(self, place, number):
        """
        Function for checking if the entered value is valid
        """

        # Checking row
        for i in range(0, len(self.grid_board[0])):
            if(self.grid_board[place[0]][i] == number):
                return False
        
        # Checking column
        for i in range(0, len(self.grid_board[0])):
            if(self.grid_board[i][place[1]] == number):
                return False
        
        # Check sub-grid  
        x = place[0]//3*3
        y = place[1]//3*3
        
        for i in range(0,3):
            for j in range(0,3):
                if(self.grid_board[x+i][y+j]== number):
                    return False
        return True

    def sudoku_solver(self, window):
        """
        Solving Sudoku using Backtracking algorithm
        """

        Font = pygame.font.SysFont('Comic Sans MS', 35)

        for i in range(0,len(self.grid_board[0])):
            for j in range(0, len(self.grid_board[0])):
                if(self.is_empty(self.grid_board[i][j])): 
                    for k in range(1,10):
                        if self.is_valid((i,j), k):                   
                            self.grid_board[i][j] = k
                            pygame.draw.rect(window, self.BACKGROUND_COLOR, ((j+1)*50 + self.BUFFER, (i+1)*50+ self.BUFFER,50 -2*self.BUFFER , 50 - 2*self.BUFFER))
                            value = Font.render(str(k), True, (0,0,0))
                            window.blit(value, ((j+1)*50 +15,(i+1)*50))
                            pygame.display.update()
                            pygame.time.delay(10)
                            
                            self.sudoku_solver(window)
                            
                            # Exit condition
                            if(self.solving == 1):
                                return
                            
                            # If sudoku_solver returns, there's a mismatch
                            self.grid_board[i][j] = 0
                            pygame.draw.rect(window, self.BACKGROUND_COLOR, ((j+1)*50 + self.BUFFER, (i+1)*50+ self.BUFFER,50 -2*self.BUFFER , 50 - 2*self.BUFFER))
                            pygame.display.update()
                    return               
        self.solving = 1
        
def main():    
    pygame.init()                                       # initializing pygame
    sudoku = Soduku()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()