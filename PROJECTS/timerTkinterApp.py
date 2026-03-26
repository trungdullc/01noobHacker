"""
Main Purpose:
   Learn how to use datetime module and learn how to play a sound and popup a notification on windows only

Idea stolen from:
   https://pythongeeks.org/python-countdown-clock-timer/

Level: Intermediate
What I learned:
   tkinter has a BooleanVar() type ⭐
   tkinter has new widget: tkinter.Checkbutton ⭐
   To use another method in tkinteruse .after() due to .mainloop() ⭐⭐⭐⭐⭐
   winsound.Beep()
   win10toast.ToastNotifier() has a show_toast() method

Created by HackerDu
"""

import sys
import tkinter as tk
from datetime import datetime                      # Display current time
try:
   from win10toast import ToastNotifier            # Display desktop notification
except ImportError:
   print("pip3 install win10toast")
try:
   import winsound                                    # plays sound only for windows
except ImportError:
   print("pip3 install winsound")

class Timer:
   def countdown(self, current_time):
      """
      Step 2: The start method call this method
      """
      if current_time > 0:
         mins, secs = divmod(current_time, 60)                          # (current_time // 60, current_time % 60)
         display = f"{mins:02d}:{secs:02d}"                             # format text ⭐

         timer_label.config(text=display)                               # print(display)
         root_window.after(1000, self.countdown, current_time-1)        # Important: To use another method in tkinteruse .after() due to .mainloop()
      else:
         timer_label.config(text="Time-Up")

         if check.get():                                                # if Checkbutton is true then play sound with winsound module
            winsound.Beep(frequency=440, duration=1000)                 # Note: This is how to make it Beep vs PlaySound ❤️❤️❤️❤️❤️

         toast = ToastNotifier()                                                       # Create ToastNotifier Object
         toast.show_toast("Notification", "Timer is Off", duration=10, threaded=True)  # ❤️❤️❤️❤️❤️

   def start(self):
      """
      Step 1: When the button gets pressed this method gets called and its variable gets passed as an argument
      """
      current_time = hour.get()*3600 + minus.get()*60 + second.get()
      self.countdown(current_time)

def main():
   global hour, minus, second, timer_label, root_window, check        # Note: Make usesable to other func
   
   timer = Timer()

   root_window = tk.Tk()                                             # Note: Need to do this since didn't use: from tkinter import *
   root_window.geometry('600x600')
   root_window.title('Countdown Timer with Notification')
   root_window.resizable(width=0, height=0)

   tk.Label(master=root_window, text="Countdown Clock and Timer", font=('Calibri 15')).pack(pady=20)

   # Get current time using datetime module
   now = datetime.now().strftime("%H:%M:%S")
   tk.Label(master=root_window, text=now).pack()                     # print(now) only works in CLI

   # Assign data types to variables to be used with .get() and textvariable=
   check = tk.BooleanVar()                                           # New tkinter datatype learned ❤️ to be used w/ textvariable
   hour = tk.IntVar()                                                # Note: Default value is 0
   minus = tk.IntVar()
   second = tk.IntVar()

   timer_label = tk.Label(root_window, font=('bold',20))             # Note: Initially not have text parameter so can't see
   timer_label.pack(pady=20)

   tk.Label(root_window, text="Enter time in HH:MM:SS", font=('bold')).pack()

   tk.Entry(root_window, textvariable=hour, width=30).pack()
   tk.Entry(root_window, textvariable=minus, width=30).pack()
   tk.Entry(root_window, textvariable=second, width=30).pack()

   tk.Checkbutton(root_window, text='Check for Music', variable=check).pack()    # Note: tkinter has Checkbutton widget
   tk.Button(root_window, text="Set Countdown", command=timer.start, bg='yellow').pack()

   root_window.mainloop()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()