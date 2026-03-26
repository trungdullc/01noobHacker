"""
Main Purpose:
    I probably would use chatgpt to create a table, it's more faster
    Treeview in tkinter
    
Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    ttk.Style()

Created by HackerDu
"""

import sys
from tkinter import *
from tkinter import ttk

class MyApp(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill=BOTH, expand=True)       # Note: Did this inside class instead of app.pack()

        self.setup_style()
        self.create_tree()

    def setup_style(self):
        style = ttk.Style()

        style.configure(
            "mystyle.Treeview",
            highlightthickness=0,
            bd=0,
            font=('Calibri', 11),
            rowheight=28
        )

        style.configure("mystyle.Treeview.Heading",font=('Calibri', 13, 'bold'))
        style.layout("mystyle.Treeview",[('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

    def create_tree(self):
        self.tree = ttk.Treeview(self, style="mystyle.Treeview")

        # Define columns
        self.tree["columns"] = ("Name", "Age")

        self.tree.column("#0", width=0, stretch=NO)
        self.tree.column("Name", anchor=W, width=150)
        self.tree.column("Age", anchor=CENTER, width=80)

        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")

        # Insert sample data
        self.tree.insert("", "end", values=("Alice", 25))
        self.tree.insert("", "end", values=("Bob", 1337))
        self.tree.insert("", "end", values=("HackerDu", 69))

        self.tree.pack(fill=BOTH, expand=True, padx=20, pady=20)
        self.mainloop()

def main():
    root_window = Tk()
    root_window.title("Styled Treeview Example")
    app = MyApp(root_window)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()