"""
Main Purpose:
    configure vs .set()

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    Update arguments with .configure() and can only modify tkinter widgets
    This is used with tkinter control variables often
        StringVar()
        IntVar()
        DoubleVar()
        BooleanVar()
        
Created by HackerDu
"""

import sys
import tkinter

class MyApp(tkinter.Tk):                                    # Note: Inhertance from tkinter.Tk
    def __init__(self):
        super().__init__()

        # Configure the main window (root)
        self.title("Edit this title")
        self.minsize(400, 400)

        # self.pack()                                       # No longer needed so no longer need self.root = root

        self.Label1 = tkinter.Label(self, text="Hi World")
        self.Label1.pack()

        self.update_title()
        # self.mainloop()                                     # Note: Not needed

    def update_title(self):
        self.title("Hacker Updated the title")
        self.Label1.configure(text="Hacker Updated tkinter.Label")

def main():
    MyApp().mainloop()                                      # Note: Used with inhertance tkinter.Tk
    # root_window = tkinter.Tk()
    # app = MyApp(root_window)
    # root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()