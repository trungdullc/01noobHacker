"""
Main Purpose:
    Display image on tkinter

Idea stolen from:
    https://pythongeeks.org/python-dice-rolling-simulator/

Level: Intermediate
What I learned:
    from PIL import Image, ImageTk          # Not used as much anymore since PIL.ImageTk does same thing
    from PIL.ImageTk import PhotoImage      # PhotoImage Data Type

Created by HackerDu
"""

import tkinter
from PIL import Image, ImageTk
import random, sys

# Top level widgets which represents the main window of the application
from PIL.ImageTk import PhotoImage

# Images
DICE = [r'image/die1.png',r'image/die2.png',r'image/die3.png',r'image/die4.png',r'image/die5.png',r'image/die6.png']

class Dice:
    def __init__(self):
        self.root_window=tkinter.Tk()
        self.root_window.geometry('400x400')
        self.root_window.title("Roll the Dice")

        # Simulating the dice with random variables 1 to 6 and generate image
        # image1=ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image1 = PhotoImage(Image.open(random.choice(DICE)))                # Better if self.image1

        self.label1 = tkinter.Label(master=self.root_window,image=image1)    # label1.image = image1
        self.label1.pack(expand=True)                                        # Packing a widget in parent widget

        # Adding buttons,and command will use rolling_dice function
        button=tkinter.Button(self.root_window,text="Roll the dice",fg="green",command=self.rolling_dice)
        button.pack(expand="True")                                      # Pack a widget in parent widget

        self.root_window.mainloop()

    def rolling_dice(self):
        """
        Rolling dice function activated by clicking button
        """

        image1 = ImageTk.PhotoImage(Image.open(random.choice(DICE)))
        self.label1.configure(image=image1)         # Update image self.label1["image"] = image1
        self.label1.image=image1                    # Keep a reference (needed) ❤️
                                                    # since image1 is only stored in a local variable inside fx better if self.image1

def main():
   Dice()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()