"""
Main Purpose:
    Convert lbs to kgs

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    .focus()
    .winfo_children()
    .pack_configure()

Created by HackerDu
"""

import sys
import tkinter

class MyApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("lb to kg converter")             # Important: Found way to edit attributes in Frame class ❤️
        self.minsize(300,100)

        self.lbs = tkinter.StringVar()
        lbs_entry = tkinter.Entry(self, width=7, textvariable=self.lbs)
        lbs_entry.pack(side=tkinter.LEFT)
        lbs_entry.focus()                                       # Auto focus this widget

        tkinter.Label(self, text ="lbs").pack(side=tkinter.LEFT)

        tkinter.Button(self, text="Calculate", command=self.calculate).pack(side=tkinter.LEFT)

        self.output = tkinter.DoubleVar()
        output_label = tkinter.Label(self, textvariable=self.output)
        output_label.pack(side=tkinter.BOTTOM)

        # Important: Makes all child widgets adjust configurations ❤️
        for child in self.winfo_children():
            child.pack_configure(padx=5, pady=5)

    def calculate(self):
        try:
            value = float(self.lbs.get())
            kg_calculated = 0.453592 * value
            print(f"The number of kgs is {kg_calculated}")
            self.output.set(kg_calculated)
        except ValueError:
            pass

def main():
    app = MyApp().mainloop()                  # Note: Don't need self.mainloop() if declared here

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()