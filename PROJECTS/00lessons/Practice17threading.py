"""
Main Purpose:
    threading

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    import threading
    threading.Thread()
    threading.start()
    self.after(0, lambda: self.label.configure(text=str(total)))

Created by HackerDu

More Resources: https://users.tricity.wsu.edu/~bobl/cpts481/an-introduction-to-tkinter.pdf
"""

import sys
import tkinter
import threading

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)
        
        self.master.title("Threading Example")
        self.master.minsize(300,100)
        self.pack()

        self.label = tkinter.Label(self, text="Click the button")
        self.label.pack()

        self.button = tkinter.Button(self, text="Add it up", command=self.button_pressed)
        self.button.pack()

    def button_pressed(self):
        # Start thread so GUI doesn't freeze
        thread = threading.Thread(target=self.callback)
        thread.start()
    
    def callback(self):
        total = 0

        for i in range(100_000_000):
            total +=i

        # Update UI safetly using after()
        self.after(0, lambda: self.label.configure(text=str(total)))

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()