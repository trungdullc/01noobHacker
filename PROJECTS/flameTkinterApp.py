"""
Main Purpose:
    Learn .pack from tkinter module
    
Idea stolen from:
    https://pythongeeks.org/python-flames-game-source-code/

Level: Beginner
What I learned:
    Nothing, it is review of previous projects

Created by HackerDu
"""

import sys
import tkinter
from tkinter import *

class Flame:
    def match_algorithm(self):
        combine_names = name1_entry.get() + name2_entry.get()

        # Checks to see if entries is empty
        for character in combine_names:
            if combine_names.count(character) != 1:
                combine_names = combine_names.replace(character,"")

        # Algorithm of how love_number is picked not by random but by mod 6
        love_number = len(combine_names) % 6

        relationship_results = ""

        if love_number == 1:
            relationship_results += "Friends"
        elif love_number == 2:
            relationship_results += "Love"
        elif love_number == 3:
            relationship_results += "Affection"
        elif love_number == 4:
            relationship_results += "Marriage"
        elif love_number == 5:
            relationship_results += "Enemy"
        elif love_number == 0:
            relationship_results += "Siblings"
        else:
            pass
        
        Label(root_window,text="According to the Game of Flames the Relation is:").pack()
        Label(root_window,text=relationship_results).pack()

def main():
   global name1_entry, name2_entry, root_window
   
   flame = Flame()

   root_window = Tk()
   root_window.title("PythonGeeks")
   root_window.geometry("500x500")
   Label(root_window,text="Play FLAMES: Love Matcher",font=("Arial", 15 ),bg="blue").pack()

   name1_entry=tkinter.StringVar()
   name2_entry=tkinter.StringVar()

   Label(root_window,text="Enter Your Name").pack()
   Entry(root_window,textvariable=name1_entry).pack()
   Label(root_window,text="Enter Your Crush's Name").pack()
   Entry(root_window,textvariable=name2_entry).pack()

   Button(root_window,text="SHOW RESULT",bg="light blue",command=flame.match_algorithm).pack()

   root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()