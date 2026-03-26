"""
Main Purpose:
    3 Different Pop-up windows
    from tkinter import messagebox                  # Easy Popups
        messagebox.showinfo
        messagebox.showwarning
        messagebox.showerror
        messagebox.askquestion                      # returns "yes"/"no"
        messagebox.askyesno                         # returns True/False
        messagebox.askokcancel                      # returns True/False
        messagebox.askretrycancel                   # returns True/False
    from tkinter import simpledialog                # Input type popups
    from tkinter import filedialog                  # File popups

Idea stolen from:
    https://education.scinet.utoronto.ca/pluginfile.php/80431/mod_resource/content/1/tkinter.pdf

Level: Beginner
What I learned:
    messagebox.showinfo()
    messagebox.showwarning()
    messagebox.askyesno()

    simpledialog.askstring()
    simpledialog.askinteger()
    simpledialog.askfloat()

    filedialog.askopenfilename()
    filedialog.asksaveasfilename() 
        
Created by HackerDu
"""

import sys
import tkinter
from tkinter import messagebox                  # Easy Popups
from tkinter import simpledialog                # Input type popups
from tkinter import filedialog                  # File popups

class MyApp(tkinter.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("messagebox")
        self.minsize(300,100)

        tkinter.Button(self, text="Show Message", command=self.popup).pack()
        tkinter.Button(self, text="Show Warning", command=self.warning).pack()
        tkinter.Button(self, text="Show Question", command=self.asking).pack()

        # Forced message
        name = simpledialog.askstring("Input", "What is your name?")
        age = simpledialog.askinteger("Input", "Enter your age:")
        number = simpledialog.askfloat("Input", "Enter a number:")
        print(name, age, number)

        file = filedialog.askopenfilename()                     # with open(file_path, "r") as file:
        save = filedialog.asksaveasfilename()                   # with open(file_path, "w") as file:

        print(file)

    def popup(self):
        messagebox.showinfo(title="My Pop-Up", message="Hi Hackers")        

    def warning(self):
        messagebox.showwarning("Warning", "Beware of Hackers")
    
    def asking(self):
        result = messagebox.askyesno("Question", "Continue: Yes or No")
        print(result)

def main():
    MyApp().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()