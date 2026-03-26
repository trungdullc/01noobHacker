"""
Main Purpose:
    Check if status 200 on website
        http://www.pokemon.com
        www.pokemon.com not work will need http://

Idea stolen from:
    https://pythongeeks.org/python-website-connectivity-checker-project/

Level: Beginner
What I learned:
    Need create a Tk() before declaring tkinter.StringVar()
    import urllib.request

Created by HackerDu
"""

import sys
import urllib.request
from tkinter import *
import tkinter

class WebsiteChecker:
    def __init__(self):
        self.root_window=Tk()
        self.root_window.geometry("700x350")
        self.root_window.title("Website Connectivity Checker")
        Label(self.root_window, text="Website Connectivity Checker", font=('Calibri 15')).pack(pady=20)

        self.url = tkinter.StringVar()      # raise RuntimeError(f"Too early to {what}: no default root window")
        Entry(self.root_window, textvariable=self.url).place(x=200,y=80,height=30,width=280)

        Button(self.root_window, text="Check",command=self.check).place(x=320,y=160)

        self.root_window.mainloop()

    def check(self):
        web = (self.url.get())
        status_code = urllib.request.urlopen(web).getcode()
        website_is_up = status_code == 200

        if website_is_up == TRUE:
            Label(self.root_window, text="Website Available", font=('Calibri 15')).place(x=260,y=200)
        else:
            Label(self.root_window, text="Website Not Available", font=('Calibri 15')).place(x=260,y=200)

def main():
    WebsiteChecker()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()