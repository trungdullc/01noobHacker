"""
Main Purpose:
    Control Variables
        tkinter.StringVar()
        tkinter.IntVar()
        tkinter.DoubleVar()
        tkinter.BooleanVar()

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    Control Variables uses .get() and .set()

Created by HackerDu
"""

import sys
import tkinter

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)            # Important: This not optional if pass tkinter.Frame using MyApp().mainloop()
        self.pack(expand = True, fill = tkinter.BOTH)   # Remember to pack Frame onto master

        self.master.title("")                           # When use tkinter.Frame we passed Frame master
        self.master.minsize(300, 100)
    
        # tkinter control variables
        self.var = tkinter.IntVar()

        # Note: Could also use textvariable instead of variable
        check_button = tkinter.Checkbutton(self, text = "Show title", variable = self.var, command = self.click).place(x=50,y=50)

        # self.mainloop()

    def click(self):
        if (self.var.get() == 1):
            self.master.title("Checkbutton clicked")
        else:
            self.master.title("")

def main():
    MyApp().mainloop()                              # Note: Doesn't need root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()