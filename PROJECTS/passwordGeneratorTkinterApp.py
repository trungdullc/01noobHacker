"""
Main Purpose:
   messagebox not party of tkinter/__init__.py
   learn random module and difference between:
      random.randint()
      random.random()
      random.shuffle()
      random.choices()
      random.sample()

Idea stolen from:
   https://pythongeeks.org/python-password-generator/

Level: Intermediate
What I learned:
   Need root_window as global if another method creaters tkinter.Label(), tkinter.Entry()
   random.sample() is unique vs random.choices()
   When creating a new entry from another method betterto use StringVar() instead of str

Created by HackerDu
"""

import sys, random
from tkinter import *                  # imports things defined in tkinter/__init__.py but not automatically all submodules like:
from tkinter import messagebox         # tkinter.messagebox, tkinter.filedialog, tkinter.colorchooser
# import tkinter.messagebox as messagebox
POSSIBLE_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

class PasswordGenerator:
   def generate_password(self):
      """
      When button gets pressed this is method that generates a password
      """

      # Tries to typecast entry from string to int
      try:
         repeat = int(repeat_entry.get())                   # This is where the global entries are used
         length = int(length_entry.get())
      except Exception as e:
         messagebox.showerror(title="You got an error", message=f"Please key in the required inputs\n{e}")
         return                                             # Note: need return so method done or else goes to repeat
   
      # Check if user allows repetition of characters
      if repeat == 1:                                       # Remember Checkbutton: True/False but Entry gets str converted to int from above
         password = random.sample(POSSIBLE_CHARACTERS,k=length)         # random.sample is unique vs random.choices
      else:
         password = random.choices(POSSIBLE_CHARACTERS,k=length)

      # Note: password is a list need to convert to string w/ join
      password=''.join(password)
      password_variable = StringVar()
      password="Created password: "+ str(password)
      password_variable.set(password)

      # Note: Reason need root_window as global to create a new tkinter.Entry() ⭐
      # Note: When creating a new entry from another method betterto use StringVar() instead of str
      Entry(master=root_window, bd=0, bg="gray85", textvariable=password_variable, state="readonly").place(x=10, y=140, height=50, width=320)

def main():
   global repeat_entry, length_entry, root_window
   
   password_generator = PasswordGenerator()

   root_window = Tk()
   root_window.geometry("350x200")
   root_window.title("Simple Password Generator")
   root_window.resizable(height=0, width=0)

   title_label = Label(master=root_window, text="Password Generator", font=('Ubuntu Mono',12))
   title_label.pack()

   length_label = Label(master=root_window, text="Enter length of password: ")
   length_label.place(x=20,y=30)                                           # Remember have to do seperate since didn't assign as tkinter.IntVar()
   length_entry = Entry(master=root_window, width=3)                       # Want as global
   length_entry.place(x=190,y=30)

   repeat_label = Label(master=root_window, text="Repetition? 1: no repetition, 2: otherwise: ")
   repeat_label.place(x=20,y=60)
   repeat_entry = Entry(master=root_window, width=3)                       # Want as global
   repeat_entry.place(x=300,y=60)

   password_button = Button(master=root_window, text="Generate Password", command=password_generator.generate_password)
   password_button.place(x=100,y=100)

   root_window.mainloop()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()