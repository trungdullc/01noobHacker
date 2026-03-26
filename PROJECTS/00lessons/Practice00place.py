"""
Main Purpose:
    3 Tkinter geometry managers ❤️
        pack()
        grid()
        place()

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    pack() options
        fill        NONE (default), X (fill horizontally), Y (fill vertically), BOTH (fill both)
        expand      YES (fill any space not used in widgets parent), N)
        side        TOP (default), BOTTOM, LEFT, RIGHT

    place() options
        anchor      Direction: N, E, S, W, NE, NW (default), SE, SW
        bordermode  INSIDE, OUTSIDE
        height      Height of widget in pixels
        width       Width of widget in pixels
        relheight   Float between 0.0 and 1.0 is fraction of height of parent widget
        relwidth    Float between 0.0 and 1.0 is fraction of width of parent widget
        relx        Horizontal offset as float between 0.0 and 1.0 as fraction of width of parent widget
        rely        Vertical offset as float between 0.0 and 1.0 as fraction of height of the parent widget
        x           Horizontal offset in pixel
        y           Vertical offset in pixel
    
    grid() options
        column      0 (default to put widget into)
        columnspan  1 (default)
        ipadx       How many pixels to pad widget horizontally inside widget's border
        ipady       How many pixels to pad widgets vertically inside widget's border
        padx        How many pixel to pad widget horizontally outside widget's borders
        pady        How many pixel to pad widget vertically outside widget's borders
        row         0 (default to put widget into)
        rowspan     1 (default)
        sticky      Direction: N, E, S, W, NE, NW, SE, SW, zero

Created by HackerDu
"""

import sys
import tkinter

# Important: This class doesn't inhert from tkinter.Frame or tkinter.Tk yet
class MyApp:
    def __init__(self, root):
        self = root                                 # Note: Since pass a Tk() can modify it
        self.geometry("500x500")
        self.title("Tkinter Geometry Manager")

        # Absolute height
        btn_height = tkinter.Button(self, text="50px high")
        btn_height.place(height=50, x=200, y=200)

        # Absolute width
        btn_width = tkinter.Button(self, text="60px wide")
        btn_width.place(width=60, x=300, y=300)

        # Relative height (60% of window)
        btn_relheight = tkinter.Button(self, text="Relheight of 0.6")
        btn_relheight.place(relheight=0.6)

        # Relative width (20% of window)
        btn_relwidth = tkinter.Button(self, text="Relwidth of 0.2")
        btn_relwidth.place(relwidth=0.2)

        # Relative X position (30% across)
        btn_relx = tkinter.Button(self, text="Relx of 0.3")
        btn_relx.place(relx=0.3)

        # Relative Y position (70% down)
        btn_rely = tkinter.Button(self, text="Rely of 0.7")
        btn_rely.place(rely=0.7)

        # Absolute X position
        btn_x = tkinter.Button(self, text="X = 400px")
        btn_x.place(x=400)

        # Absolute Y position
        btn_y = tkinter.Button(self, text="Y = 321")
        btn_y.place(y=321)

        self.mainloop()                                  # Important: if not call mainloop in def main()

def main():
    root_window = tkinter.Tk()                          # Note: Passing of a window
    app = MyApp(root_window)
    # root_window.mainloop()                            # Note: if no self.mainloop() must call here

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()