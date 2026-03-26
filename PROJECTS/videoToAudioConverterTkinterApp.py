"""
Main Purpose:
   Convert video file mp4 into audio file wav

Idea stolen from:
   https://pythongeeks.org/python-video-to-audio-converter/

Level: Intermediate
What I learned:
   import moviepy
   tkinter.filedialog import *

Created by HackerDu
"""

import sys
try:
    import moviepy
except ImportError:
    print("pip3 install moviepy")
from tkinter.filedialog import *
from tkinter import *

class VideoConverter:
   def __init__(self):
      self.root_window=Tk()
      self.root_window.geometry("700x350")
      self.root_window.title("Video to Audio Converter")
      self.root_window.resizable(width=0,height=0)

      Label(self.root_window, text="VIDEO TO AUDIO CONVERTER laugh.mp4",bg='orange', font=('Calibri 15')).pack()
      Label(self.root_window, text="Choose a File ").pack()

      # Empty Label
      self.pathlab = Label(self.root_window)
      self.pathlab.pack()

      Button(self.root_window,text='Browse',command=self.browse).pack()
      Button(self.root_window,text='SAVE',command=self.save).pack()

      self.root_window.mainloop()
    
   def browse(self):
      """
      Browsing Method
      """

      self.video = askopenfilename()         # tkinter method

      # self.video = moviepy.editor.VideoFileClip(self.video)
      self.video = moviepy.VideoFileClip(self.video)
      
      self.pathlab.config(text=self.video)

   def save(self):
      """
      Converting Video to Audio
      """

      audio = self.video.audio                                    # Convert to audio
      audio.write_audiofile("sounds/sample.wav")                  # Save as audio
      Label(self.root_window, text="Video Converted into Audio and Saved Successfully",bg='blue', font=('Calibri 15')).pack()
    
def main():
   VideoConverter()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
       sys.exit()