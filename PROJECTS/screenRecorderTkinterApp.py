"""
Main Purpose:
    How to use np with cv2

Idea stolen from:
    https://pythongeeks.org/python-screen-recorder/

Level: Intermediate
What I learned:
    from PIL import ImageGrab
    import cv2
    import numpy as np

Created by HackerDu
"""

import sys
try:
    from PIL import ImageGrab
except ImportError:
    print("pip3 install pillow")
try:
    import cv2
except ImportError:
    print("pip3 install opencv-python")
import numpy as np
from tkinter import *
from tkinter import TclError

class ScreenRecorder:
    def __init__(self):
        self.root_window  = Tk()
        self.root_window.geometry("340x220")
        self.root_window.title("Screen Recorder")

        # Show background image using tkinter.PhotoImage() and make optional
        try:
            bg_img = PhotoImage(file = "images/die1.png")           # Note: Select a background image
            # Label(master=self.root_window, image=bg_img, bd=0).pack()
        except TclError:                                            # Note: This is error in tkinter module
            # If can't load image then don't use image tag
            Label(master=self.root_window, bd=0).pack()
        
        Label(self.root_window, text="Screen Recorder",font=("Ubuntu Mono", 16), bg="#02b9e5").place(relx=0.5,rely=0.1, anchor=CENTER)
        Label(self.root_window, text="Enter 'q' to exit screen recording", bg="#02b9e5").place(relx=0.5,rely=0.3, anchor=CENTER)
        Button(self.root_window, text="Record Screen", command=self.record_screen, relief= RAISED).place(relx=0.5,rely=0.6, anchor=CENTER)

        self.root_window.mainloop()

    def record_screen(self):
        # Obtain image dimensions 
        image = ImageGrab.grab()                    # Screen capture
        img_np_arr = np.array(image)                # Convert the object to numpy array
        shape = img_np_arr.shape                    # Extract and print shape of array
        print(shape)

        # Create a video writer and save recorded avi to ⭐
        screen_cap_writer = cv2.VideoWriter('videos/screen_recorded.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 50, (shape[1], shape[0]))

        # To View the screen recording in a separate window (OPTIONAL)
        # This is optional. Use the aspect ratio scaling if you wish to view the screen recording simultaneously
        # Low scale_by_percent implies smaller window
        scale_by_percent = 50 
        width = int(shape[1] * scale_by_percent / 100)
        height = int(shape[0] * scale_by_percent / 100)
        new_dim = (width, height)
        
        # Record the screen
        # Condition to keep recording as a video
        while True:
            image = ImageGrab.grab()                                # Capture screen
            img_np_arr = np.array(image)                            # Convert to array
            final_img = cv2.cvtColor(img_np_arr, cv2.COLOR_RGB2BGR) # OpenCV follows BGR and not RGB, hence we convert
            screen_cap_writer.write(final_img)                      # Write to video

            # OPTIONAL: To view your screen recording in a separate window, resize and use imshow()
            '''
                If you choose to view the screen recording simultaneously,
                It will be displayed and also recorded in your video. 
            '''
            image = cv2.resize(final_img, (new_dim))
            cv2.imshow("image", image)
            
            # Stop and exit screen recoding if user presses 'e' (You can put any letter)
            if cv2.waitKey(1) == ord('q'):
                break
            
        # Release the created the objects
        screen_cap_writer.release()
        cv2.destroyAllWindows()

def main():
    ScreenRecorder()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()