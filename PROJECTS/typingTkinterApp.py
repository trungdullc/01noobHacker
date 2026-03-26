"""
Main Purpose:
    Learn about .bind() and event
    Don't use global inside a class use self.
    Use only one Tk() the other use Toplevel()
    Don't have nested functions in a class

Idea stolen from:
    https://pythongeeks.org/python-typing-test-project/

Level: Intermediate
What I learned:
    .destroy() is important like .close() when open() but not used in class
    .bind() is like eventListener for keyboard

Created by HackerDu
"""

import sys, random
from tkinter import *
import tkinter.font as font
try:
    from english_words import english_words_set
except ImportError:
    print("pip3 install english-words")                 # Note: Couldn't get words so hardcoded it

# words = list(english_words_set)
words = [
    "apple","table","chair","python","keyboard","window",
    "screen","mouse","coffee","school","paper","clock",
    "phone","music","water","light","green","house"
]

class Typing:
    def __init__(self, root_window):
        self.root = root_window
        self.create_main_menu()

    def create_main_menu(self):
        """
        Create main menu window
        """

        self.root.geometry('600x600')
        self.root.title("Typing Test")
        self.root.config(bg='LightBlue1')
        self.root.resizable(width=0,height=0)

        # Creating a frame to show the title of the project
        heading_frame = Frame(self.root, bg="snow3", bd=5)
        heading_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

        heading_label = Label(
            master=heading_frame,
            text="Welcome to \n Typing Test",
            bg='azure2',
            fg='black',
            font=('Courier',15,'bold')
        )
        heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Creating a button to start the game
        button = Button(
            master=self.root,
            text="Start",
            bg='old lace',
            fg='black',
            width=20,
            height=2,
            command=self.start_game
        )
        button['font'] = font.Font(size=12)     # Other way other than .configuration to change parameters
        button.place(x=200,y=300)

    def start_game(self):
        """
        Start game on new window using Toplevel() not Tk() when button is clicked on
        """
        # Reset game values
        self.score = 0
        self.time = 0
        self.count = 0

        self.game_window = Toplevel(self.root)
        self.game_window.geometry('700x600')
        self.game_window.title('Typing Test')
        self.game_window.config(bg='honeydew2')
        self.game_window.resizable(width=0, height=0)

        Label(
            master=self.game_window,
            text='Typing Test',
            font=('arial',25,'italic bold'),
            fg='gray'
        ).place(x=10,y=10)

        self.next_word = Label(
            master=self.game_window,
            text='Press Enter to Start',
            font=('arial',20,'italic bold')
        )
        self.next_word.place(x=30,y=240)

        # Score
        self.score_label = Label(
            master=self.game_window,
            text='Your Score:',
            font=('arial',25,'italic bold'),
            fg='red'
        )
        self.score_label.place(x=10,y=100)

        self.scoreboard = Label(
            master=self.game_window,
            text=self.score,
            font=('arial',25,'italic bold'),
            fg='blue'
        )
        self.scoreboard.place(x=100,y=180)

        # Timer
        self.timer_label = Label(
            master=self.game_window,
            text='Time Elapsed:',
            font=('arial',25,'italic bold'),
            fg='red'
        )
        self.timer_label.place(x=450,y=100)

        self.timer = Label(
            self.game_window,
            text=self.time,
            font=('arial',25,'italic bold'),
            fg='blue'
        )
        self.timer.place(x=560,y=180)

        # Input box
        self.userInput = Entry(
            master=self.game_window,
            font=('arial',25,'italic bold'),
            bd=10,
            justify='center'
        )
        self.userInput.place(x=150,y=330)
        self.userInput.focus_set()

        self.game_window.bind('<Return>', self.main_game)   # Runs main_game function everytime the user presses enter button ❤️❤️❤️

    def time_function(self):
        """
        Timer Function
        Step 2: Does recursion with the .after() method to check time and update score
        """
        if self.count <= 10:
            self.time += 1
            self.timer.config(text=self.time)
            self.timer.after(1000, self.time_function)      # Recursion with .after()
        else:
            self.end_game()                                 # Ends game showing score

    def main_game(self, event):                             # Note: event is needed even though not modified, listening for <Return> key
        """
        Main Game Logic
        Step 1: When <Return> is pressed this method is trigger that calls the time_function()
        """

        # Start timer only once
        if self.time == 0:
            random.shuffle(words)
            self.next_word.config(text=words[0])
            self.userInput.delete(0, END)                       # clear entry widget userInput
            self.time_function()                                # call time function
            return

        # Check answer
        if self.userInput.get() == self.next_word['text']:      # check if user entered correctly
            self.score += 1
            self.scoreboard.config(text=self.score)

        self.count += 1

        if self.count <= 10:
            random.shuffle(words)                               # Repeat, could have created a inner function for this and resetting global variables
            self.next_word.config(text=words[0])
            self.userInput.delete(0, END)

    def end_game(self):
        """
        Function called to end the game
        """
        # Reset counters
        missed = self.count - self.score

        # Show Final score and results
        result = Label(
            master=self.game_window,
            text=f'Time Taken = {self.time}\nScore = {self.score}\nMissed = {missed}',
            font=('arial',25,'italic bold'),
            fg='grey'
        )
        result.place(x=200,y=250)

        # Disable input after finish
        self.userInput.config(state=DISABLED)

def main():
    root_window = Tk()                                  # This acts like the main menu
    app = Typing(root_window)
    root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()