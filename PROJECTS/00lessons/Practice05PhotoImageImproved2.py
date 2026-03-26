"""
Main Purpose:
    Tkinter support .ppm files from PIL(Python Imaging Library)
        .JPG, .PNG and .GIF   
        bunny.JPG
        snowball.PNG
        cat.gif

Idea stolen from:
    https://riptutorial.com/Download/tkinter.pdf

Level: Beginner
What I learned:
    tkinter.PhotoImage() used for png and gif
    # Note: PIL (Python Imaging Library) can handle 30 file formats but no longer maintained
    ImageTk.PhotoImage() used for jpeg
        Note: The way to resize images is different
    # Note: If not keep reference of PhotoImage or PIL class the object will be garbaged collected

    Use .after() if want use a timer fx inside mainloop()
        Syntax: widget.after(delay_ms, callback, *args)
            delay_ms time
            callback method
        Also used in timers
        
Created by HackerDu
"""

import sys

from tkinter import *
from PIL import Image, ImageTk          # For JPEG

class HelloImages(Tk):
    def __init__(self):
        """
        After gets called everything gets automatically destroyed
        """

        # self.pack(fill="both", expand=True)
        super().__init__()
        
        self.geometry("500x500")
        self.title("Hello Images")
        self.resizable(0,0)

        self.image1 = PhotoImage(file="images/snowball.PNG")            # Create a reference, must be self because destroyed
        self.image1 = self.image1.subsample(2,2)                        # OPTIONAL: subsample vs zoom
        Label(self, image=self.image1).pack()                           # Add image to Button() or Label() using img
        
        # _tkinter.TclError: couldn't recognize data in image file "images/bunny.JPG"
        img2 = Image.open("images/bunny.JPG")                           # Open JPG with Pillow
        img2 = img2.resize((100,100))                                   # OPTIONAL: resize
        self.image2 = ImageTk.PhotoImage(img2)                          # Convert to Tkinter-compatible image
        Label(self, image=self.image2).pack()

        self.label = Label(self)                                        # Setup empty Label
        self.label.pack()

        self.frames = []                                                # Data Type: Load all frames
        index = 0                                                       # Note: Don't need self will auto delete

        while True:
            try:
                frame = PhotoImage(file="images/cat.gif", format=f"gif -index {index}")
                frame = frame.subsample(2,2)
                self.frames.append(frame)
                index += 1
            except:
                break                                                   # Important: Stops when no more frames

        self.current = 0
        self.animate()                                                  # Start animation

        self.mainloop()

    def animate(self):
        self.label.configure(image=self.frames[self.current])
        self.current = (self.current + 1) % len(self.frames)            # Forever loop
        self.after(100, self.animate)                                   # Control speed (milliseconds)

def main():
    # app = HelloImages(root_window)
    HelloImages().mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()