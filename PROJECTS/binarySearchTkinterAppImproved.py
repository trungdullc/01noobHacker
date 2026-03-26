"""
Main Purpose:
   Solve using different method Solution().mainloop() vs root_window = tkinter.Tk() then passing as argument into Solution(root_window)
   Inhertance from tkinter.Tk instead of tkinter.Frame

Idea stolen from:
   https://pythongeeks.org/python-binary-search/

Level: Intermediate
What I learned:
   tkinter.Tk vs tkinter.Frame

Created by HackerDu
"""

import sys
from tkinter import *
import tkinter

# Important: tkinter.Tk = main window vs tkinter.Frame = container inside a window ❤️
class Solution(tkinter.Tk):
   def __init__(self):
      super().__init__()                     # Note: When using Tk don't need pass arguments

      self.geometry("700x350")
      self.title("Binary Search")
      self.resizable(width=0, height=0)

      self.number = IntVar()
      self.sorted_list = StringVar()

      Label(self, text="Let's perform Binary Search", font=('Calibri', 15)).pack(pady=20)

      Label(self, text="Enter a Sorted List (no comma)").pack()
      Entry(self, textvariable=self.sorted_list).pack()

      Label(self, text='Enter number you want to search').pack()
      Entry(self, textvariable=self.number).pack()

      Button(self, text="Search", command=self.binary_search).pack()

      self.output_label = Label(self, text="", font=('Calibri', 12))
      self.output_label.pack(pady=10)

   def binary_search(self):
      try:
         list_of_sorted_numbers = list(map(int, self.sorted_list.get().split()))
         search_this_number = self.number.get()

         first_ptr = 0
         last_ptr = len(list_of_sorted_numbers) - 1
         found = False

         while first_ptr <= last_ptr and not found:
            middle_ptr = (first_ptr + last_ptr) // 2

            if list_of_sorted_numbers[middle_ptr] == search_this_number:
               found = True
            elif search_this_number < list_of_sorted_numbers[middle_ptr]:
               last_ptr = middle_ptr - 1
            else:
               first_ptr = middle_ptr + 1

         if found:
            self.output_label.config(text="Number found in the list")
         else:
            self.output_label.config(text="Number NOT found in the list")

      except ValueError:
         self.output_label.config(text="Invalid input! Use numbers only.")

def main():
   Solution().mainloop()
   
if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
       sys.exit()