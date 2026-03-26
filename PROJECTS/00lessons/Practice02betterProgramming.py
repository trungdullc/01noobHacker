"""
Main Purpose:
    Objects should be invokeable on their own (better programming)

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    MyApp().mainloop() but can't configure root_window

Created by HackerDu
"""

import sys
import tkinter

# Best practice to inherit but tkinter.Frame or tkinter.Tk
# Note: With tkinter.Frame can't edit comment out attributes so usualy use tkinter.Tk is better

class MyApp(tkinter.Frame):
    def __init__(self, master = None):                  # Default master is None
        tkinter.Frame.__init__(self, master)            # Note: Could also use super
        
        self.root_window = master
        # self.root_window.title("Learning class objects")
        # self.root_window.geometry("300x100")
        # self.root_window.resizable(0,0)               # Look at comment out parts
        self.pack()                                     # Important

        tkinter.Button(self, text="Click Me", command=self.output_hi).pack()
        
        self.output_label = tkinter.Label(self, text="")
        self.output_label.pack()

    def output_hi(self):
        print("hi")
        self.output_label.configure(text="hi")

def main():
#    root_window = tkinter.Tk()                             # Look at comment out parts
#    app = MyApp(master = root_window)                      # Important concept
#    root_window.mainloop()
    MyApp().mainloop()                                      # Allow class to run stand-alone

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()