"""
Main Purpose:
    mp3 music player from pygame

Idea stolen from:
    https://pythongeeks.org/python-music-player/

Level: Intermediate
What I learned:
    import pygame.mixer as mixer

Created by HackerDu
"""

import os, sys
from tkinter import *
from tkinter import filedialog
try:
    import pygame.mixer as mixer
except ImportError:
    print("pip3 install pygame")

class MusicPlayer:
    def __init__(self):
        mixer.init()                                # Initializing the mixer

        self.root_window = Tk()
        self.root_window.geometry('700x220')
        self.root_window.title('Music Player')
        self.root_window.resizable(0, 0)

        # All the frames
        song_frame = LabelFrame(self.root_window, text='Current Song', bg='LightBlue', width=400, height=80)
        song_frame.place(x=0, y=0)

        button_frame = LabelFrame(self.root_window, text='Control Buttons', bg='Turquoise', width=400, height=120)
        button_frame.place(y=80)

        listbox_frame = LabelFrame(self.root_window, text='Playlist', bg='RoyalBlue')
        listbox_frame.place(x=400, y=0, height=200, width=300)

        # All StringVar variables
        current_song = StringVar(self.root_window, value='<Not selected>')
        song_status = StringVar(self.root_window, value='<Not Available>')

        playlist = Listbox(listbox_frame, font=('Helvetica', 11), selectbackground='Gold')

        scroll_bar = Scrollbar(listbox_frame, orient=VERTICAL)
        scroll_bar.pack(side=RIGHT, fill=BOTH)

        playlist.config(yscrollcommand=scroll_bar.set)

        scroll_bar.config(command=playlist.yview)

        playlist.pack(fill=BOTH, padx=5, pady=5)

        # SongFrame Labels
        Label(song_frame, text='CURRENTLY PLAYING:', bg='LightBlue', font=('Times', 10, 'bold')).place(x=5, y=20)

        song_lbl = Label(song_frame, textvariable=current_song, bg='Goldenrod', font=("Times", 12), width=25)
        song_lbl.place(x=150, y=20)

        # Buttons in the main screen
        pause_btn = Button(button_frame, text='Pause', bg='Aqua', font=("Georgia", 13), width=7,command=lambda: self.pause_song(song_status))
        pause_btn.place(x=15, y=10)

        stop_btn = Button(button_frame, text='Stop', bg='Aqua', font=("Georgia", 13), width=7,command=lambda: self.stop_song(song_status))
        stop_btn.place(x=105, y=10)

        play_btn = Button(button_frame, text='Play', bg='Aqua', font=("Georgia", 13), width=7,command=lambda: self.play_song(current_song, playlist, song_status))
        play_btn.place(x=195, y=10)

        resume_btn = Button(button_frame, text='Resume', bg='Aqua', font=("Georgia", 13), width=7,command=lambda: self.resume_song(song_status))
        resume_btn.place(x=285, y=10)

        load_btn = Button(button_frame, text='Load Directory', bg='Aqua', font=("Georgia", 13), width=35,command=lambda: self.load(playlist))
        load_btn.place(x=10, y=55)

        Label(self.root_window, textvariable=song_status, bg='SteelBlue', font=('Times', 9), justify=LEFT).pack(side=BOTTOM, fill=X)

        self.root_window.update()
        self.root_window.mainloop()

    def play_song(self, song_name: StringVar, songs_list: Listbox, status: StringVar):
        """
        Play method
        """

        song_name.set(songs_list.get(ACTIVE))

        mixer.music.load(songs_list.get(ACTIVE))
        mixer.music.play()

        status.set("Song PLAYING")

    def stop_song(self, status: StringVar):
        """
        Stop Method
        """

        mixer.music.stop()
        status.set("Song STOPPED")

    def load(self, listbox):
        """
        Load Method
        """

        os.chdir(filedialog.askdirectory(title='Open a songs directory'))

        tracks = os.listdir()

        for track in tracks:
            listbox.insert(END, track)

    def pause_song(self, status: StringVar):
        """
        Pause Song Method
        """

        mixer.music.pause()
        status.set("Song PAUSED")

    def resume_song(self, status: StringVar):
        """
        Resume Song Method
        """

        mixer.music.unpause()
        status.set("Song RESUMED")

def main():
    MusicPlayer()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()