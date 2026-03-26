"""
Main Purpose:
    Download public Youtube videos into video folder
    
Idea stolen from:
    https://pythongeeks.org/python-youtube-video-downloader-code/

Level: Intermediate
What I learned:
    from pytubefix import YouTube
    
Created by HackerDu
"""

import sys
try:
    from pytubefix import YouTube
except ImportError:
    print("pip3 install pytubefix")
from tkinter import *

class YoutubeDownloader:
    def __init__(self):        
        self.root_window = Tk()
        self.root_window.geometry("700x350")
        self.root_window.title("Youtube Downloader")

        self.text = StringVar()
        self.res1 = IntVar()
        self.res2 = IntVar()
        self.res3 = IntVar()

        Label(self.root_window, text="YOUTUBE VIDEO DOWNLOADER", bg='grey', font=('Calibri 15')).pack()
        Label(self.root_window, text="Enter the public URL (https://youtu.be/dQw4w9WgXcQ) to download", font=('Calibri 12')).pack()

        Entry(self.root_window, textvariable=self.text, width=50).pack()

        Checkbutton(self.root_window, text='360p', onvalue=18, offvalue=0, variable=self.res1).pack()
        Checkbutton(self.root_window, text='720p', onvalue=22, offvalue=0, variable=self.res2).pack()
        Checkbutton(self.root_window, text='1080p', onvalue=37, offvalue=0, variable=self.res3).pack()

        Button(self.root_window, text="Download", bg='green', command=self.downloader).pack()

        self.root_window.mainloop()

    def downloader(self):
        """
        Download public Youtube video into videos/
        """
        
        url = self.text.get()

        if not url:
            Label(self.root_window, text="Please enter a public URL (https://youtu.be/dQw4w9WgXcQ)").pack()
            return

        try:
            video = YouTube(url)

            # Determine resolution itag
            res = None

            if self.res1.get() == 18:
                res = 18
            elif self.res2.get() == 22:
                res = 22
            elif self.res3.get() == 37:
                res = 37
            else:
                Label(self.root_window, text="Select a resolution").pack()
                return

            stream = video.streams.filter(progressive=True, file_extension='mp4').get_by_itag(res)
            stream.download(output_path="videos/")
            print("Downloaded Successfully")

            if stream:
                stream.download(filename="Untitled", output_path=".")
                Label(self.root_window, text="Downloaded Successfully").pack()
            else:
                Label(self.root_window, text="Stream not available").pack()

        except Exception as e:
            Label(self.root_window, text=f"Error: {e}").pack()

def main():
   YoutubeDownloader()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()