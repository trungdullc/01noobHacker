"""
Main Purpose:
    Shutdown, Restart, Logout using os module
    Beware: Click the buttons will restart your computer
    
Idea stolen from:
    https://pythongeeks.org/python-project-shutdown-restart-logout-computer/

Level: Beginner
What I learned:
    os module
    os.system()

Created by HackerDu
"""

import os, sys
from tkinter import *

class SystemOperations:
    def __init__(self):
        self.root_window=Tk()
        self.root_window.geometry("700x350")
        self.root_window.title("os module")
        self.root_window.resizable(width=0,height=0)

        Label(self.root_window, text="Shutdown, Restart and Logout Using Pc", font=('Calibri 15')).pack(pady=20)

        Button(self.root_window,text='Shutdown',command=self.shutdown,font=('normal',11), bg='yellow').pack()
        Button(self.root_window,text='Restart',command=self.restart,font=('normal',11), bg='yellow').pack()
        Button(self.root_window,text='Logout',command=self.logout,font=('normal',11), bg='yellow').pack()

        self.root_window.mainloop()

    def shutdown(self):
        """
        Shutdown Method
        """

        os.system("shutdown /s /t 0")

    def restart(self):
        """
        Restart Method
        """

        os.system("shutdown /r /t 0")

    def logout(self):
        """
        Logout Method
        """

        os.system("shutdown /l /t 0")

def main():
   SystemOperations()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()