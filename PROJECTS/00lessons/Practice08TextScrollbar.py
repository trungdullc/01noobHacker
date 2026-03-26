"""
Main Purpose:
    Connecting tkinter.Text(self) to tkinter.Scrollbar()

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    self.text = tkinter.Text(self)
    tkinter.Scrollbar(self, orient="vertical", command=self.text.yview)
    self.text.configure(yscrollcommand=self.scroll_y.set)

Created by HackerDu
"""

import sys
import tkinter

# Inheritance from tkinter.Frame
class MyApp(tkinter.Frame):
    def __init__(self, parent):                         # (self, master=None)
        super().__init__(parent)                        # (master)
        self.pack(fill="both", expand=True)

        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        # Text widget
        self.text = tkinter.Text(self)
        self.text.pack(side="left", fill="both", expand=True)

        # Vertical scrollbar
        self.scroll_y = tkinter.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.scroll_y.pack(side="right", fill="y")

        # Important: Connect scrollbar to text
        # Note: Hard to do without documentation
        self.text.configure(yscrollcommand=self.scroll_y.set)

        # Optional: add sample text
        for i in range(25):
            self.text.insert("end", f"Line {i+1}\n")

def main():
    root_window = tkinter.Tk()
    root_window.title("Text + Scrollbar Example")
    app = MyApp(root_window)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()