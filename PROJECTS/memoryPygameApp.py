"""
Main Purpose:
    Creating a memory game using pygame

Idea stolen from:
    https://pythongeeks.org/python-memory-puzzle-flipping-tiles-game/

Level: Advanced
What I learned:
    assert()
    TODO later: Learn algorithm and data structures used in the program

Created by HackerDu

try:
    x = -3
    assert x > 0                        # if True nothing happens else raises AssertionError
except AssertionError:
    print("DEBUG: Detected False")
"""

import random, sys
import pygame 
from pygame.locals import *

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

BACKGROUND_COLOR = GRAY
LIGHT_BACKGROUND_COLOR = NAVYBLUE
BOX_COLOR = CYAN
HIGHLIGHT_COLOR = YELLOW

CIRCLE = 'circle'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

class Memory:
    def __init__(self):
        self.Frame_Speed = 30 
        self.Window_Width = 640 
        self.Window_Height = 480 
        self.Speed_Reveal = 8 
        self.Box_Size = 40 
        self.Gap_Size = 10
        self.Border_Width = 10 
        self.Border_Height = 7 

        assert (self.Border_Width * self.Border_Height) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
        self.X_margin = int((self.Window_Width - (self.Border_Width * (self.Box_Size + self.Gap_Size))) / 2)
        self.Y_margin = int((self.Window_Height - (self.Border_Height * (self.Box_Size + self.Gap_Size))) / 2)

        self.All_Colors = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
        self.All_Shapes = (CIRCLE, SQUARE, DIAMOND, LINES, OVAL)
        assert len(self.All_Colors)* len(self.All_Shapes) * 2 >= self.Border_Width * self.Border_Height, "Board is too big for the number of shapes/colors defined."

        pygame.init()
        self.Frame_Speed_Clock = pygame.time.Clock()
        self.DIS_PlaySurf = pygame.display.set_mode((self.Window_Width, self.Window_Height))

        self.X_mouse  = 0 
        self.Y_mouse = 0 

    def GenerateData_RevealedBoxes(self, val):
        """
        Revealed box Method
        """

        Boxes_revealed = []

        for i in range(self.Border_Width):
            Boxes_revealed.append([val] * self.Border_Height)
        return Boxes_revealed

    def Randomized_Board(self):
        """
        Creating a randomized board
        """
        icon = []

        for color in self.All_Colors:
            for shape in self.All_Shapes:
                icon.append( (shape, color) )

        random.shuffle(icon) 
        num_IconsUsed = int(self.Border_Width * self.Border_Height / 2) 
        icon = icon[:num_IconsUsed] * 2 
        random.shuffle(icon)
    
        board = []

        for x in range(self.Border_Width):
            column = []
            for y in range(self.Border_Height):
                column.append(icon[0])
                del icon[0] 
            board.append(column)
        return board

    def Split_Groups(self, group_Size, List):
        """
        Splitting a list into lists
        """

        result = []

        for i in range(0, len(List), group_Size):
            result.append(List[i:i + group_Size])
        return result

    def leftTop_Coord(self, x_box, y_box):
        """
        Create coordinate method
        """

        left = x_box * (self.Box_Size + self.Gap_Size) + self.X_margin
        top = y_box * (self.Box_Size + self.Gap_Size) + self.Y_margin

        return (left, top)

    def Box_Pixel(self, x, y):
        """
        Converting to pixel coordinates to box coordinates
        """

        for x_box in range(self.Border_Width):
            for y_box in range(self.Border_Height):
                left, top = self.leftTop_Coord(x_box, y_box)
                box_Rect = pygame.Rect(left, top, self.Box_Size, self.Box_Size)
                if box_Rect.collidepoint(x, y):
                    return (x_box, y_box)
        return (None, None)

    def Draw_Icon(self, shape, color, x_box, y_box):
        """
        Draw icon and synthetic sugar
        """

        quarter = int(self.Box_Size * 0.25)         # syntactic sugar
        half    = int(self.Box_Size * 0.5)          # syntactic sugar

        left, top = self.leftTop_Coord(x_box, y_box)

        # Draw the shapes
        if shape == CIRCLE:
            pygame.draw.circle(self.DIS_PlaySurf, color, (left + half, top + half), half - 5)
            pygame.draw.circle(self.DIS_PlaySurf, BACKGROUND_COLOR, (left + half, top + half), quarter - 5)
        elif shape == SQUARE:
            pygame.draw.rect(self.DIS_PlaySurf, color, (left + quarter, top + quarter, self.Box_Size - half, self.Box_Size - half))
        elif shape == DIAMOND:
            pygame.draw.polygon(self.DIS_PlaySurf, color, ((left + half, top), (left + self.Box_Size - 1, top + half), (left + half, top + self.Box_Size - 1), (left, top + half)))
        elif shape == LINES:
            for i in range(0, self.Box_Size, 4):
                pygame.draw.line(self.DIS_PlaySurf, color, (left, top + i), (left + i, top))
                pygame.draw.line(self.DIS_PlaySurf, color, (left + i, top + self.Box_Size - 1), (left + self.Box_Size - 1, top + i))
        elif shape == OVAL:
            pygame.draw.ellipse(self.DIS_PlaySurf, color, (left, top + quarter, self.Box_Size, half))

    def get_Shape_Color(self, board, x_box, y_box):
        return board[x_box][y_box][0], board[x_box][y_box][1]

    def Box_Cover(self, board, boxes, coverage):
        """
        Drawing box cover
        """

        for box in boxes:
            left, top = self.leftTop_Coord(box[0], box[1])
            pygame.draw.rect(self.DIS_PlaySurf, BACKGROUND_COLOR, (left, top, self.Box_Size, self.Box_Size))
            shape, color = self.get_Shape_Color(board, box[0], box[1])
            self.Draw_Icon(shape, color, box[0], box[1])

            if coverage > 0: 
                pygame.draw.rect(self.DIS_PlaySurf, BOX_COLOR, (left, top, coverage, self.Box_Size))
        pygame.display.update()
        self.Frame_Speed_Clock.tick(self.Frame_Speed)

    def Reveal_Boxes_Animation(self, board, boxesToReveal):
        """
        Revealing and covering animation
        """
        
        for coverage in range(self.Box_Size, (-self.Speed_Reveal) - 1, -self.Speed_Reveal):
            self.Box_Cover(board, boxesToReveal, coverage)

    def Cover_Boxes_Animation(self, board, boxesToCover):
        for coverage in range(0, self.Box_Size + self.Speed_Reveal, self.Speed_Reveal):
            self.Box_Cover(board, boxesToCover, coverage)

    def Draw_Board(self, board, revealed):
        """
        Drawing entire board and Highlight
        """

        for x_box in range(self.Border_Width):
            for y_box in range(self.Border_Height):
                left, top = self.leftTop_Coord(x_box, y_box)
                if not revealed[x_box][y_box]:
                    pygame.draw.rect(self.DIS_PlaySurf, BOX_COLOR, (left, top, self.Box_Size, self.Box_Size))
                else:
                    shape, color = self.get_Shape_Color(board, x_box, y_box)
                    self.Draw_Icon(shape, color, x_box, y_box)

    def Draw_HighlightBox(self, x_box, y_box):
        left, top = self.leftTop_Coord(x_box, y_box)
        pygame.draw.rect(self.DIS_PlaySurf, HIGHLIGHT_COLOR, (left - 5, top - 5, self.Box_Size + 10, self.Box_Size + 10), 4)

    def Start_Game(self, board):
        """
        Start the game animation
        """

        covered_Boxes = self.GenerateData_RevealedBoxes(False)
        boxes = []
        
        for x in range(self.Border_Width):
            for y in range(self.Border_Height):
                boxes.append( (x, y) )
        random.shuffle(boxes)
        box_Groups = self.Split_Groups(8, boxes)

        self.Draw_Board(board, covered_Boxes)
        
        for boxGroup in box_Groups:
            self.Reveal_Boxes_Animation(board, boxGroup)
            self.Cover_Boxes_Animation(board, boxGroup)

    def Game_Won (self, board):
        """
        Creating function for game won
        """

        coveredBoxes = self.GenerateData_RevealedBoxes(True)
        color_1 = LIGHT_BACKGROUND_COLOR
        color_2 = BACKGROUND_COLOR

        for i in range(13):
            color_1, color_2 = color_2, color_1 
            self.DIS_PlaySurf.fill(color_1)
            self.Draw_Board(board, coveredBoxes)
            pygame.display.update()
            pygame.time.wait(300)

    def Won(self, Boxes_revealed):
        """
        Returns True if all the boxes have been revealed, otherwise False
        """

        for i in Boxes_revealed:
            if False in i:
                return False                # return False if any boxes are covered
        return True

def main():
    memory = Memory()
    pygame.display.set_caption('Memory Game')

    Board = memory.Randomized_Board()
    Boxes_revealed = memory.GenerateData_RevealedBoxes(False)

    first_Selection = None

    memory.DIS_PlaySurf.fill(BACKGROUND_COLOR)
    memory.Start_Game(Board)

    while True: 
        mouse_Clicked = False

        memory.DIS_PlaySurf.fill(BACKGROUND_COLOR) 
        memory.Draw_Board(Board, Boxes_revealed)

        for event in pygame.event.get(): 
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                memory.X_mouse, memory.Y_mouse = event.pos
            elif event.type == MOUSEBUTTONUP:
                memory.X_mouse, memory.Y_mouse = event.pos
                mouse_Clicked = True

        x_box, y_box = memory.Box_Pixel(memory.X_mouse, memory.Y_mouse)

        if x_box != None and y_box != None:
            if not Boxes_revealed[x_box][y_box]:
                memory.Draw_HighlightBox(x_box, y_box)
            if not Boxes_revealed[x_box][y_box] and mouse_Clicked:
                memory.Reveal_Boxes_Animation(Board, [(x_box, y_box)])
                Boxes_revealed[x_box][y_box] = True 
                if first_Selection == None: 
                    first_Selection = (x_box, y_box)
                else: 
                    icon1shape, icon1color = memory.get_Shape_Color(Board, first_Selection[0], first_Selection[1])
                    icon2shape, icon2color = memory.get_Shape_Color(Board, x_box, y_box)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        memory.Cover_Boxes_Animation(Board, [(first_Selection[0], first_Selection[1]), (x_box, y_box)])
                        Boxes_revealed[first_Selection[0]][first_Selection[1]] = False
                        Boxes_revealed[x_box][y_box] = False
                    elif memory.Won(Boxes_revealed): 
                        memory.Game_Won(Board)
                        pygame.time.wait(2000)

                        Board = memory.Randomized_Board()
                        Boxes_revealed = memory.GenerateData_RevealedBoxes(False)

                        memory.Draw_Board(Board, Boxes_revealed)
                        pygame.display.update()
                        pygame.time.wait(1000)

                        memory.Start_Game (Board)
                    first_Selection = None 

        pygame.display.update()
        memory.Frame_Speed_Clock.tick(memory.Frame_Speed)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()