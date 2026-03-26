"""
Main Purpose:
    Connecting tkinter.Canvas(self) to tkinter.Scrollbar()

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    Read documentation or use chatgpt to create scrollable canvas    

Created by HackerDu
"""

import sys
import tkinter

# Remember: When inhereit use parent keyword
class MyApp(tkinter.Frame):
    def __init__(self, parent):                             # (self, master=None)
        super().__init__(parent)                            # (master)
        self.grid(row=0, column=0, sticky="nsew")

        # Make the frame expandable
        parent.rowconfigure(0, weight=1)                    # master.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)                 # master.columnconfigure(0, weight=1)

        self.create_widgets()
        self.mainloop()

    def create_widgets(self):
        # Canvas
        self.canvas = tkinter.Canvas(self, width=150, height=150)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        # Draw shapes
        self.canvas.create_oval(10, 10, 20, 20, fill="red")
        self.canvas.create_oval(200, 200, 220, 220, fill="blue")

        # Scrollbars
        self.scroll_x = tkinter.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.scroll_x.grid(row=1, column=0, sticky="ew")

        self.scroll_y = tkinter.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scroll_y.grid(row=0, column=1, sticky="ns")

        # Connect canvas to scrollbars
        self.canvas.configure(
            xscrollcommand=self.scroll_x.set,
            yscrollcommand=self.scroll_y.set
        )

        # IMPORTANT: define scrollable area
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Make canvas expand
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

def main():
    root_window = tkinter.Tk()
    root_window.title("Canvas with Scrollbars")
    app = MyApp(root_window)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()