"""
Main Purpose:
    Learn difference between StringVar() and string

Idea stolen from:
    Noone

Level: Beginner
What I learned:
    Must use .get() to get string type()
    If not use tkinter data types then must use .configure() to edit vs .set()

Created by HackerDu
"""

import sys
import tkinter

class MyApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("500x500")
        self.resizable(width=0,height=0)

        self.label_0_entry = tkinter.StringVar()
        self.label_0_entry.set("Welcome to my program")

        self.create_gui()

    def create_gui(self):
        self.label_0 = tkinter.Label(master=self, textvariable=self.label_0_entry)
        self.label_0.pack()

        tkinter.Button(self, text="Click Me", command=self.add).pack()
    
    def add(self):
        if self.label_0_entry.get() == "1 + 1":         # Important: label_0_entry is StringVar() not a string
            self.label_0_entry.set("2 + 2")
        else:
            self.label_0_entry.set("1 + 1")

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()