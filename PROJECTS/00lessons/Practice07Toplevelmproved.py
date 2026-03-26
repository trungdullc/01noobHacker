"""
Main Purpose:
   Create new window using Toplevel() not tkinter.Tk()

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    for widget in self.root_window.winfo_children():
        widget.destroy()
    top.quit vs top.destroy

Created by HackerDu
"""

import sys
from tkinter import *

class MyApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")          # Note: When pass root, VSC not autocomplete .title()
        self.geometry("300x200")           # Note: When pass root, VSC not autocomplete .geometry()
        # self.pack()

        self.setup_main()
        self.mainloop()

    def setup_main(self):
        # Button to open Toplevel window
        Button(self, text="Open New Window", command=self.open_toplevel).pack(pady=10)

        # Button to clear root and show message
        Button(self, text="End Game", command=self.end_game).pack(pady=10)

    def open_toplevel(self):
        """
        Method to create a new window
        """

        top = Toplevel(self)                   # Create new window, don't use Tk()
        top.title("Toplevel Window")

        Label(top, text="This is a new window").pack(padx=20, pady=20)
        Button(top, text="Close", command=top.destroy).pack(pady=10)    # Note: top.quit close entire Tkinter program

    def end_game(self):
        """
        Method to clear root_window
        """
        
        # Destroy all widgets in root window
        for widget in self.winfo_children():
            widget.destroy()

        # Show final message
        Label(self, text="Thank you for playing", font=("Arial", 16)).pack(pady=50)

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()