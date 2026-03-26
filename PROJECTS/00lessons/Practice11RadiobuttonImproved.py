"""
Main Purpose:
    tkinter.Radiobutton() and indicatoron option

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    tkinter.Radiobutton()
    .set()

Created by HackerDu
"""

import sys
import tkinter

class MyApp(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title("Radio Button Example")

        self.color_mode = tkinter.StringVar()
        self.color_mode.set("Monochrome")               # Using .set() for tkinter Data Types ❤️

        # Note: This is how to do multiple Radiobuttons using a for loop
        options_list = ["Monochrome","Grayscale","True Color","Color Separation"]

        for option in options_list:
            radio_button = tkinter.Radiobutton(
                self,
                text=option,
                variable=self.color_mode,
                value=option,                   # Creates a Radiobutton with different value from option_list
                indicatoron=0,                  # 0: Makes it look like buttons
                width=20
            )
            radio_button.pack(pady=2)

        self.output = tkinter.StringVar()
        self.output.set("")

        tkinter.Label(self, textvariable=self.output).pack(pady=5)

        tkinter.Button(self,text="Print Choice",command=self.print_choice).pack(pady=10)

        self.mainloop()

    def print_choice(self):
        """
        Print choice in terminal using print()
        """

        print(self.color_mode.get())
        self.output.set(self.color_mode.get())

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()