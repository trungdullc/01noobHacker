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

class MyApp(tkinter.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.root_window = root                         # Note: Only way to change attributes in class vs initialize in def main()
        self.root_window.title("Radio Button Example")

        self.color_mode = tkinter.StringVar()
        self.color_mode.set("Monochrome")               # Using .set() for tkinter Data Types ❤️

        # Note: This is how to do multiple Radiobuttons using a for loop
        options_list = ["Monochrome","Grayscale","True Color","Color Separation"]

        for option in options_list:
            radio_button = tkinter.Radiobutton(
                self.root_window,
                text=option,
                variable=self.color_mode,
                value=option,                   # Creates a Radiobutton with different value from option_list
                indicatoron=0,                  # 0: Makes it look like buttons
                width=20
            )
            radio_button.pack(pady=2)

        self.output = tkinter.StringVar()
        self.output.set("")

        tkinter.Label(self.root_window, textvariable=self.output).pack(pady=5)

        tkinter.Button(self.root_window,text="Print Choice",command=self.print_choice).pack(pady=10)

        self.mainloop()

    def print_choice(self):
        """
        Print choice in terminal using print()
        """

        print(self.color_mode.get())
        self.output.set(self.color_mode.get())

def main():
    root_window = tkinter.Tk()
    app = MyApp(root_window)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()