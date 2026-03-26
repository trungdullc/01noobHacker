"""
Main Purpose:
    Extract Song Lyrics using public API

Idea stolen from:
    https://pythongeeks.org/python-extract-song-lyrics/

Level: Beginner
What I learned:
    tkinter.Message widget
    from lyrics_extractor import SongLyrics

Created by HackerDu
"""

import sys
import tkinter
from tkinter import *
try:
    from lyrics_extractor import SongLyrics
except ImportError:
    print("pip3 install lyrics-extractor")

class LyricExtractor:
    def __init__(self):
        self.root_window = Tk()
        self.root_window.geometry('600x600')
        self.root_window.title('Song Lyrics Extractor from Internet')
        Label(self.root_window, text="Enter the song you want Lyrics for", font=('Calibri 15')).pack(pady=20)

        self.result = tkinter.StringVar()
        self.song = tkinter.StringVar()

        Entry(self.root_window, textvariable=self.song).pack()

        # Note: new tkinter widget and this is where self.result updates
        Message(self.root_window,textvariable=self.result, bg="light grey").pack(side=TOP,anchor=W,fill=BOTH, expand=1)
        
        Button(self.root_window, text="GO",command=self.get_lyrics).pack()

        self.root_window.mainloop()

    def get_lyrics(self):
        """
        Method to get lyrics using SongLyrics API
        """

        song_name = self.song.get()
        api_key = "AIzaSyAcZ6KgA7pCIa_uf8-bYdWR85vx6-dWqDg"
        engine_id = "aa2313d6c88d1bf22"
        extract_lyrics = SongLyrics(api_key, engine_id)         # Going to website for which we have got engine id
        song_lyrics = extract_lyrics.get_lyrics(song_name)      # Getting the lyrics
        self.result.set(song_lyrics)                            # Setting the result

def main():
    LyricExtractor()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()