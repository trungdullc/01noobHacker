"""
Main Purpose:
   Create QR Code from Entry

   Idea stolen from:
   https://pythongeeks.org/python-project-qr-code-generator/

Level: Intermediate
What I learned:
   import pyqrcode
   import png

Created by HackerDu
"""

import sys
try:
   import pyqrcode
   from pyqrcode import QRCode            # Generate QR Code
except ImportError:
   print("pip3 install pyqrcode")
try:
   import png                             # Saves QR Code as an image
except ImportError:
   print("pip3 install pypng ")
from PIL import ImageTk, Image
import PIL.Image
import tkinter as tk 
from tkinter import *

def create_qrcode():
   """
   Generate QR Code
   """
   
   entry_string = qr_string.get()
   qr = pyqrcode.create(entry_string)
   qr.png('images/myqr.png', scale = 6)             # Note: Saved to myqr.png

   Label(root_window,text='QR Code is created and saved successfully to myqr.png').pack()

def main():
   global qr_string, root_window

   root_window = Tk()  
   root_window.geometry('300x350')
   root_window.title('QR Code')

   Label(root_window,text='Lets Create QR Code',font='arial 15').pack()
   
   # String which represents the QR code
   qr_string = tk.StringVar()

   Entry(root_window,textvariable=qr_string,font='arial 15').pack()
   Button(root_window,text='create',bg='pink',command=create_qrcode).pack()

   root_window.mainloop()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()