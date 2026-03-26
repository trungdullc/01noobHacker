"""
Main Purpose:
   Solve it first in CLI then build tkinter GUI on top of it

Idea stolen from:
   https://pythongeeks.org/python-binary-search/

Level: Intermediate
What I learned:
   How to apply tkinter to a leetcode style question that can be solved
   either Iterative Approach or Recursive Approach
   Must create root_window before declaring tkinter Data Types

Created by HackerDu

def binary_search_iterative(number_list, number_to_find):
    left, right= 0, len(number_list)

    while right > left:
        middle = (left + right) // 2
        if nums[middle] > number_to_find:
            right = middle
        elif nums[middle] < number_to_find :
            left = middle + 1
        else:
            return middle
    return None

def binary_search_recursive(number_list, number_to_find, start, end):
    middle = (start + end) // 2

    if start == end:
        return None
    if number_list[middle] > item:
        return binary_search(number_list, inumber_to_find start, middle)
    elif nums[middle] < number_to_find:
        return binary_search(number_list, number_to_find, middle + 1, end)
    else:
        return middle
"""

import sys
from tkinter import *

class Solution:
   def binary_search():
      """"
      When button is clicked will run this method to search for number in sorted_list not in O(n) but in O(logn)
      This algorithm uses iterative approach to solve the solution

      Runtime Complexity: O(logn)
      Space Complexity: O(1)           # Data Type are constant, if list used can be O(n)
      """
      list_of_sorted_numbers: list[str] = sorted_list.get().split(" ")

      # Convert list[str] to list[int]
      for i in range(0, len(list_of_sorted_numbers)):
         list_of_sorted_numbers[i] = int(list_of_sorted_numbers[i])
      
      search_this_number = (number.get())

      first_ptr = 0
      last_ptr = len(list_of_sorted_numbers) - 1
      found = False

      while( first_ptr <= last_ptr and not found):
         middle_ptr = (first_ptr + last_ptr)//2

         if (list_of_sorted_numbers[middle_ptr] == search_this_number) :
                  found = True
         else:
               if search_this_number < list_of_sorted_numbers[middle_ptr]:
                  last_ptr = middle_ptr - 1
               else:
                  first_ptr = middle_ptr + 1

      if found == True:
         Label(master=root_window, text="Number found in the list", font=('Calibri')).place(x=280,y=180)
      else:
         Label(master=root_window, text="Number NOT found in the list", font=('Calibri')).place(x=240,y=210)

def main():
   global sorted_list, number, root_window

   solution = Solution()                     # Leetcode Answer ⭐⭐⭐⭐⭐

   root_window=Tk()
   root_window.geometry("700x350")
   root_window.title("Binary Search")
   root_window.resizable(width=0, height=0)

   # Important: Must create root_window before declaring tkinter Data Types ❤️❤️❤️❤️❤️
   number = IntVar()                         # .get() returns a int
   sorted_list = StringVar()                 # .get() returns a str

   Label(root_window, text="Let's perform Binary Search", font=('Calibri 15')).pack(pady=20)

   Label(root_window, text="Enter a Sorted List (no comma)", font=('Calibri')).pack()
   Entry(root_window,textvariable=sorted_list).pack()
   Label(root_window,text='Enter number you want to search').pack()
   Entry(root_window,textvariable=number).pack()

   Button(root_window, text="Search", command=solution.binary_search).pack()
   # print(solution.binary_search())         # Leetcode Answer ⭐⭐⭐⭐⭐

   root_window.mainloop()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
       sys.exit()