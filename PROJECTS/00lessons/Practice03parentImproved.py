"""
Main Purpose:
    Learn modular, object-oriented programming from tkinter

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    python2 and python3 tkinter named differently
    Any class can be inhereited but need use parent keyword

Created by HackerDu
"""

import sys

try:
    import Tkinter                  # python2           # Note: Know this exist, annoying to use with VSC
except ModuleNotFoundError:
    from tkinter import *           # python3           # Note: This way can use auto complete

class HelloWorld(Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)
        self.label = Label(self, text="Hello World!")
        self.label.pack(padx=20, pady=20)

        self.root_window = parent                       # Note: Need to be set to a tkinter.Tk()     
        self.root_window.geometry("500x500")
        self.root_window.title("Hello World")
        self.root_window.resizable(0,0)
        self.pack(fill="both", expand=True)             # app need to be pack or see nothing

        self.mainloop()

def main():
    root_window = Tk()
    app = HelloWorld(root_window)                       # Pass root_window as argument

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()