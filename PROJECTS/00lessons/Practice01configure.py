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

class MyApp(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)                      # super().__init__(root)
        self.root_window = master                                        # Note: store reference to root because self does not have .pack() attribute

        # Configure the main window (root)
        self.root_window.title("Edit this title")
        self.root_window.minsize(400, 400)

        # Attach frame to root                                  # Important
        self.pack()

        self.Label1 = tkinter.Label(self, text="Hi World")  # This is a tkinter.widget, need self or get deleted
        self.Label1.pack()

        self.update_title()                                 # Call method instead of using eventListener
        self.mainloop()

    def update_title(self):
        self.root_window.title("Hacker Updated the title")          # No configure attribute since not a widget
        self.Label1.configure(text="Hacker Updated tkinter.Label")

def main():
    root_window = tkinter.Tk()
    app = MyApp(root_window)            # Note: If have MyApp(root_window).mainloop() no need self.mainloop()
    # root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()