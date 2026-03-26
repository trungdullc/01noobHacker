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

class HelloWorld(Frame):                                # Note: Inherance from tkinter.Frame
    def __init__(self, parent):                         # Note: use of parent ❤️
        """
        Note: using parent confusing as hell better to to master = None style
        """
        super(HelloWorld, self).__init__(parent)        # Note: use of parent ❤️
        self.label = Label(self, text="Hello World!")   # Note: master=self not root_window
        self.label.pack(padx=20, pady=20)               # padx and pady direction

def main():
    root_window = Tk()
    root_window.geometry("500x500")
    root_window.title("Hello World")
    root_window.resizable(0,0)
    
    app = HelloWorld(root_window)                       # Pass root_window as argument
    app.pack(fill="both", expand=True)                  # app need to be pack or see nothing

    root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()