"""
Main Purpose:
    Drop Down Menu using tkinter.Menu()

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    tkinter.Menu()
        
Created by HackerDu
"""

import sys
import tkinter

class MyApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Menu")
        self.minsize(300,100)

        # Note: Menu does not need packing
        self.menu_bar = tkinter.Menu(self)
        self.configure(menu=self.menu_bar)       # Attach to root_window

        # Create a new Menu instance
        self.file_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_call)
        self.file_menu.add_command(label="Open", command=self.open_call)

        self.about_menu = tkinter.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="About Us", menu=self.about_menu)
        self.about_menu.add_command(label="About", command=self.about_call)
    
        # Created a thing to output down below menu
        self.label_0 = tkinter.Label(self, text="")
        self.label_0.pack()

    def new_call(self):
        print("New call")
        self.label_0.configure(text="Hacked")           # New change

    def open_call(self):
        print("Open call")
    
    def about_call(self):
        print("About call")

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()