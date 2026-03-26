"""
Main Purpose:
    Tkinter Hangman that checks all letteres not just find first one

Idea stolen from:
    https://pythongeeks.org/python-hangman-word-guessing-game-project/

Level: Advanced
What I learned:
    nonlocal keyword to check closest variable vs global

Created by HackerDu
"""

import random, sys
from tkinter import *
from tkinter import messagebox

class Hangman:
    def __init__(self):
        """
        Runs tkinter interface when class created
        """
        self.score = 0
        self.run = True

        self.root_window = Tk()
        self.root_window.geometry('905x700')
        self.root_window.title('HANGMAN')
        self.root_window.config(bg='#ffffe7')

        self.start_game()
        self.root_window.mainloop()

    def start_game(self):
        """
        Starts the game
        """
        self.count = 0
        self.win_count = 0

        words = ['geeks']                       # Debug: Change to more words later
        self.word = random.choice(words)

        # Create blanks
        self.dashes = []
        x = 250

        for i in range(len(self.word)):
            x += 60
            label = Label(self.root_window, text="_", bg="#ffffe7", font=("arial",40))
            label.place(x=x, y=450)
            self.dashes.append(label)

        # Hangman Images
        self.hang_imgs = []
        for i in range(1,8):
            img = PhotoImage(file=f"images/h{i}.png")
            self.hang_imgs.append(img)

        self.hang_label = Label(self.root_window, bg="#ffffe7", image=self.hang_imgs[0])
        self.hang_label.place(x=300, y=-50)

        # Buttons
        letters = 'abcdefghijklmnopqrstuvwxyz'
        self.buttons = {}

        x = 0
        y = 595

        for i, letter in enumerate(letters):
            btn = Button(
                self.root_window,
                bd=0,
                bg="#ffffe7",
                activebackground="#ffffe7",
                command=lambda l=letter: self.check(l)
            )

            # Logic behind how to create btn object and place into a dictionary ❤️
            img = PhotoImage(file=f"images/{letter}.png")
            btn.config(image=img)
            btn.image = img

            btn.place(x=x, y=y)
            self.buttons[letter] = btn          # Create a dictionary of buttons

            x += 70
            if (i+1) == 13:
                x = 0
                y = 645

        # Exit button
        img = PhotoImage(file='images/exit.png')
        exit_btn = Button(self.root_window, bd=0, command=self.close, bg="#ffffe7", image=img)
        exit_btn.image = img
        exit_btn.place(x=770, y=10)

        # Score
        self.score_label = Label(self.root_window, text=f"SCORE:{self.score}", bg="#ffffe7", font=("arial",25))
        self.score_label.place(x=10,y=10)

    def close(self):
        """
        Ask if want to replay game
        """
        answer = messagebox.askyesno('ALERT','YOU WANT TO EXIT THE GAME?')

        if answer:
            self.root_window.destroy()

    def check(self, letter):
        """
        Checks if won or lost game
        """
        self.buttons[letter].destroy()

        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.win_count += 1
                    self.dashes[i].config(text=letter.upper())

            if self.win_count == len(self.word):
                self.score += 1
                answer = messagebox.askyesno('GAME OVER','YOU WON!\nWANT TO PLAY AGAIN?')
                if answer:
                    self.root_window.destroy()
                    Hangman()
                else:
                    self.root_window.destroy()

        else:
            self.count += 1
            self.hang_label.config(image=self.hang_imgs[self.count])

            if self.count == 6:
                answer = messagebox.askyesno('GAME OVER','YOU LOST!\nWANT TO PLAY AGAIN?')
                if answer:
                    self.root_window.destroy()
                    Hangman()
                else:
                    self.root_window.destroy()

if __name__ == "__main__":
    try:
        Hangman()
    except KeyboardInterrupt:
        sys.exit()