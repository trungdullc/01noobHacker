"""
Main Purpose:
    Binding other languages called Event Listeners using .bind() method
    event object

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    <Button-1>      Left Click also known as <1>
    <Button-2>      Middle Click
    <Button-3>      Right Click
    <Enter>         Mouse pointer enter widget
    <Leave>         Mouse pointer left widget
    <key>           Any key is pressed
    <Control-p>     Ctrl + p

    event object attributes:
        x           current x position in pixels
        y           current y position in pixels
        char        character code as a string
        type        event type
        
Created by HackerDu
"""

import sys
import tkinter
from tkinter import messagebox

class MyApp(tkinter.Frame):
    def __init__(self, master = None):
        tkinter.Frame.__init__(self, master)
        
        self.master.title("Binding")
        self.master.minsize(300,100)
        self.pack()

        # Binding in __init__()
        self.master.bind("a", self.a_callback)
        self.master.bind("<Button-1>", self.mouse_callback)

    # Note: event parameter with binding
    def a_callback(self, event):
        if not messagebox.askyesno("A query", "Did you press the 'a' button?"):
            messagebox.showerror("I am angry!", "Liar!")
    
    def mouse_callback(self, event):
        print(f"clicked {event.x} {event.y}")

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()