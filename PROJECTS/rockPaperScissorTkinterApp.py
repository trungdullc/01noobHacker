"""
Main Purpose:
    Creating Basic Rock Paper Scissor Tkinter game
    
Idea stolen from: 
    https://pythongeeks.org/python-rock-paper-scissors-game/

Level: Intermediate
What I learned:
    PhotoImage() for tkinter    

Created by HackerDu
"""

import random, sys
from tkinter import *

class RockPaperScissors:
    def __init__(self):
        """
        Setup tkinter window interface
        """
        
        self.root_window = Tk()
        self.root_window.title("ROCK, PAPER, SCISSOR GAME")

        width = 650
        height = 580
        window_width, window_height = self.root_window.winfo_screenwidth(), self.root_window.winfo_screenheight()

        x = (window_width / 2) - (width / 2)
        y = (window_height / 2) - (height / 2)

        self.root_window.geometry("%dx%d+%d+%d" % (width, height, x, y))       # This is old school format specifier
        self.root_window.resizable(0, 0)
        self.root_window.config(bg="#e3f4f1")

        self.player_option = 0

        # Load Images
        self.blank_img = PhotoImage(file="images/blank.png")

        self.player_rock = PhotoImage(file="images/rock_player.png")
        self.player_paper = PhotoImage(file="images/paper_player.png")
        self.player_scissor = PhotoImage(file="images/scissor_player.png")

        self.player_rock_btn = self.player_rock.subsample(3,3)
        self.player_paper_btn = self.player_paper.subsample(3,3)
        self.player_scissor_btn = self.player_scissor.subsample(3,3)

        self.comp_rock = PhotoImage(file="images/rock_computer.png")
        self.comp_paper = PhotoImage(file="images/paper_computer.png")
        self.comp_scissor = PhotoImage(file="images/scissor_computer.png")

        # Labels
        Label(self.root_window, text="PLAYER",
              bg="#e8c1c7", fg="black",
              font=('Times New Roman',18,'bold')).grid(row=1,column=1)

        Label(self.root_window, text="COMPUTER",
              bg="#e8c1c7", fg="black",
              font=('Times New Roman',18,'bold')).grid(row=1,column=3)

        self.image_player = Label(self.root_window, image=self.blank_img)
        self.image_computer = Label(self.root_window, image=self.blank_img)

        self.image_player.grid(row=2,column=1,padx=30,pady=20)
        self.image_computer.grid(row=2,column=3,pady=20)

        self.label_status = Label(self.root_window,
                                  text="",
                                  fg="black",
                                  font=('Times New Roman',20,'bold','italic'))

        self.label_status.grid(row=3,column=2)

        # Buttons
        Button(self.root_window,
               image=self.player_rock_btn,
               command=self.rock).grid(row=4,column=1,pady=30)

        Button(self.root_window,
               image=self.player_paper_btn,
               command=self.paper).grid(row=4,column=2,pady=30)

        Button(self.root_window,
               image=self.player_scissor_btn,
               command=self.scissor).grid(row=4,column=3,pady=30)

        Button(self.root_window,
               text="Quit",
               bg="red",
               fg="white",
               font=('Times New Roman',25,'bold'),
               command=self.exit).grid(row=5,column=2)

        self.root_window.mainloop()

    def rock(self):
        """
        Changes player weapon choice and assigns it then calls matching fx
        """
        self.player_option = 1
        self.image_player.configure(image=self.player_rock)
        self.matching()

    def paper(self):
        """
        Changes player weapon choice and assigns it then calls matching fx
        """
        self.player_option = 2
        self.image_player.configure(image=self.player_paper)
        self.matching()

    def scissor(self):
        """
        Changes player weapon choice and assigns it then calls matching fx
        """
        self.player_option = 3
        self.image_player.configure(image=self.player_scissor)
        self.matching()

    def computer_rock(self):
        """
        Checks see who won reassign label_status
        """
        if self.player_option == 1:
            self.label_status.config(text="Game Tie")
        elif self.player_option == 2:
            self.label_status.config(text="Player Win")
        else:
            self.label_status.config(text="Computer Win")

    def computer_paper(self):
        """
        Checks see who won reassign label_status
        """
        if self.player_option == 1:
            self.label_status.config(text="Computer Win")
        elif self.player_option == 2:
            self.label_status.config(text="Game Tie")
        else:
            self.label_status.config(text="Player Win")

    def computer_scissor(self):
        """
        Checks see who won reassign label_status
        """
        if self.player_option == 1:
            self.label_status.config(text="Player Win")
        elif self.player_option == 2:
            self.label_status.config(text="Computer Win")
        else:
            self.label_status.config(text="Game Tie")

    def matching(self):
        """
        Picks computer choice and changes image and calls computer weapon fx
        """
        
        computer_option = random.randint(1,3)       # Randomly pick computer option

        if computer_option == 1:
            self.image_computer.configure(image=self.comp_rock)
            self.computer_rock()

        elif computer_option == 2:
            self.image_computer.configure(image=self.comp_paper)
            self.computer_paper()

        else:
            self.image_computer.configure(image=self.comp_scissor)
            self.computer_scissor()

    def exit(self):
        self.root_window.destroy()              # Destroys Tk()
        sys.exit()

if __name__ == "__main__":
    try:
        RockPaperScissors()
    except KeyboardInterrupt:
        sys.exit()