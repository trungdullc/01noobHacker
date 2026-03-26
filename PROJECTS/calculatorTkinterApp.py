"""
Main Purpose:
   Learn StringVar and review lambda functions to create a calculator in tkinter
   
Idea stolen from:
   https://pythongeeks.org/python-calculator/

Level: Intermediate
What I learned:
   New tkinter data type StringVar and methods
   lambda functions

Created by HackerDu

Dimensions of Buttons:
    height: 1
    width: 3 (or (height*2)+1)

Distance between two buttons:
    In Rows: 60
    In Columns: 60

Font size in buttons: 9
"""

import sys
from tkinter import *
from tkinter.messagebox import showerror

class Calculator:
   def __init__(self):
      self.root_window = Tk()
      self.root_window.title("Calculator")
      self.root_window.geometry('250x500')
      self.root_window.resizable(0, 0)
      self.root_window.configure(background='LightCyan2')

      # New Data Type: StringVar variables
      entry_strvar = StringVar(self.root_window)

      Label(self.root_window, text='Calculator', font=("Comic Sans MS", 15), bg='LightCyan2').place(x=15, y=0)
      Label(self.root_window, text='Press \'x\' twice for exponentiation', font=("Georgia", 10), bg='LightCyan2').place(x=20, y=30)

      eqn_entry = Entry(self.root_window, justify=RIGHT, textvariable=entry_strvar, width=25, font=12, state='disabled')
      eqn_entry.place(x=10, y=70)

      # Number Buttons
      Button(self.root_window, height=2, width=5, text='7', font=9, bg='Gold', command=lambda: self.add_text("7", entry_strvar)).place(x=5, y=170)
      Button(self.root_window, height=2, width=5, text='8', font=9, bg='Gold', command=lambda: self.add_text('8', entry_strvar)).place(x=65, y=170)
      Button(self.root_window, height=2, width=5, text='9', font=9, bg='Gold', command=lambda: self.add_text('9', entry_strvar)).place(x=125, y=170)
      Button(self.root_window, height=2, width=5, text='4', font=9, bg='Gold', command=lambda: self.add_text('4', entry_strvar)).place(x=5, y=225)
      Button(self.root_window, height=2, width=5, text='5', font=9, bg='Gold', command=lambda: self.add_text('5', entry_strvar)).place(x=65, y=225)
      Button(self.root_window, height=2, width=5, text='6', font=9, bg='Gold', command=lambda: self.add_text('6', entry_strvar)).place(x=125, y=225)
      Button(self.root_window, height=2, width=5, text='1', font=9, bg='Gold', command=lambda: self.add_text('1', entry_strvar)).place(x=5, y=280)
      Button(self.root_window, height=2, width=5, text='2', font=9, bg='Gold', command=lambda: self.add_text('2', entry_strvar)).place(x=65, y=280)
      Button(self.root_window, height=2, width=5, text='3', font=9, bg='Gold', command=lambda: self.add_text('3', entry_strvar)).place(x=125, y=280)
      Button(self.root_window, height=2, width=5, text='0', font=9, bg='Gold', command=lambda: self.add_text('0', entry_strvar)).place(x=5, y=340)

      # Operator Buttons
      Button(self.root_window, height=2, width=5, text='+', font=9, bg='DarkOrange', command=lambda: self.add_text('+', entry_strvar)).place(x=195, y=340)
      Button(self.root_window, height=2, width=5, text='-', font=9, bg='DarkOrange', command=lambda: self.add_text('-', entry_strvar)).place(x=195, y=280)
      Button(self.root_window, height=2, width=5, text='x', font=9, bg='DarkOrange', command=lambda: self.add_text('*', entry_strvar)).place(x=195, y=225)
      Button(self.root_window, height=2, width=5, text='/', bg='DarkOrange', font=9, command=lambda: self.add_text('/', entry_strvar)).place(x=195, y=170)

      Button(self.root_window, height=2, width=5, text='.', font=9, bg='DarkOrange', command=lambda: self.add_text('.', entry_strvar)).place(x=65, y=340)
      Button(self.root_window, height=2, width=5, text='(', font=9, bg='DarkOrange', command=lambda: self.add_text('(', entry_strvar)).place(x=65, y=110)
      Button(self.root_window, height=2, width=5, text=')', font=9, bg='DarkOrange', command=lambda: self.add_text(')', entry_strvar)).place(x=125, y=110)

      # Equal, C and AC buttons
      Button(self.root_window, height=2, width=5, text='=', font=9, bg='Blue', command=lambda: self.submit(eqn_entry, entry_strvar)).place(x=125, y=340)
      Button(self.root_window, height=2, width=5, text='C', font=9, bg='OrangeRed', command=lambda: entry_strvar.set(entry_strvar.get()[:-1])).place(x=195, y=110)
      Button(self.root_window, height=2, width=5, text='AC', font=9, bg='Red', command=lambda: entry_strvar.set('')).place(x=5, y=110)

      # Ok Button
      Button(self.root_window, height=2, width=22, text='Ok', font=9, bg='CadetBlue', command=lambda: self.root_window.destroy()).place(x=20, y=420)

      self.root_window.update()
      self.root_window.mainloop()

   def add_text(self, text, strvar: StringVar):
      """
      Add text to Label
      """

      strvar.set(f'{strvar.get()}{text}')

   def submit(self, entry: Entry, strvar: StringVar):
      """
      Use eval(operation)
      """

      operation = entry.get()

      try:
         strvar.set(f"{strvar.get()}={eval(operation)}")
      except:
         showerror('Error!', 'Please enter a properly defined equation!')

def main():
   Calculator()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()