"""
Main Purpose:
   Learn different widgets in tkinter Label, Entry, Buttons
Idea stolen from:
   https://pythongeeks.org/python-mad-libs-generator-project/

Level: Intermediate
What I learned:
   tkinter using .place() instead of grid(), pack() ❤️
   Used Toplevel instead of Tk() for new window
   Important: .place(), .grid(), .pack return None so best to do in 2 steps ⚠️⚠️⚠️⚠️⚠️
      Used .get() function to get Entry data

Created by HackerDu
"""

import sys
from tkinter import *                  # Note: Did this so not need do tkinter.Tk(), tkinter.Button()

def Story1(window):
   # Note: child_window type is Toplevel
   def show_madlib1(child_window: Toplevel, name, game, city, player, drink, snack):
      """
      When top button is clicked this function will activate
      """
      # Note: Using f string instead of .format() or %s
      text = f'''
         One day me and my friend {name} decided to play a {game} game in {city}.
         But we were not able to play.So, we went to watch the game and our favourite player {player}.
         We drank {drink} and also ate some {snack} 
         We really enjoyed it! We are looking forward to go again and enjoy '''

      child_window.geometry(newGeometry='500x550')

      Label(master=child_window, text='Story:',  wraplength=child_window.winfo_width()).place(x=160, y=310)
      Label(master=child_window, text=text,wraplength=child_window.winfo_width()).place(x=0, y=330)

   # Note: Used Toplevel instead of Tk() like root_window = Tk()
   new_window = Toplevel(master=window, bg='yellow')
   new_window.title("A Memorable Day")
   new_window.geometry('500x500')
   
   Label(master=new_window, text=' A Memorable Day').place(x=100, y=0)
   Label(master=new_window, text='Name:').place(x=0, y=35)
   Label(master=new_window, text='Enter a game:').place(x=0, y=70)
   Label(master=new_window, text='Enter a city:').place(x=0, y=110)
   Label(master=new_window, text='Enter the name of a player:').place(x=0, y=150)
   Label(master=new_window, text='Enter the name of a drink:').place(x=0, y=190)
   Label(master=new_window, text='Enter the name of a snack:').place(x=0, y=230)
 
   # Important: .place(), .grid(), .pack return None ⚠️⚠️⚠️⚠️⚠️
   Name = Entry(master=new_window, width=17)
   Name.place(x=250, y=35)
   game = Entry(master=new_window, width=17)
   game.place(x=250, y=70)
   city = Entry(master=new_window, width=17)
   city.place(x=250, y=105)
   player = Entry(master=new_window, width=17)
   player.place(x=250, y=150)
   drink = Entry(master=new_window, width=17)
   drink.place(x=250, y=190)
   snack = Entry(master=new_window, width=17)
   snack.place(x=250, y=220)

   # Important: use .get() function to get Entry
   SubmitButton = Button(master=new_window, text="Submit", background="Blue", font=('Times', 12), command=lambda:show_madlib1(new_window, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
   SubmitButton.place(x=150, y=270)

   new_window.mainloop()

def Story2(window):
   def show_madlib2(child_window: Toplevel, profession, noun, feeling, emotion, verb):
      """
      When bottom button is clicked this function will activate
      """
      text = f'''
When I was a child, I wanted to become a {profession}
but as I grew up I got into the {noun} and decided to become an
engineer. Then I went into a job that I was not {feeling} at.
After getting {emotion} I decided to do what I love.
Despite getting lower{verb} than I used to get in my previous job.I am very
feeling '''

      child_window.geometry(newGeometry='500x550')

      Label(child_window, text='Story:',  wraplength=child_window.winfo_width()).place(x=160, y=310)
      Label(child_window, text=text,wraplength=child_window.winfo_width()).place(x=0, y=330)

   new_window = Toplevel(master=window, bg='red')
   new_window.title("Ambitions")
   new_window.geometry('500x500')

   Label(new_window, text='Ambitions').place(x=150, y=0)
   Label(new_window, text='Enter a profession:').place(x=0, y=35)
   Label(new_window, text='Enter a noun:').place(x=0, y=70)
   Label(new_window, text='Enter a feeling:').place(x=0, y=110)
   Label(new_window, text='Enter a emotion:').place(x=0, y=150)
   Label(new_window, text='Enter a verb:').place(x=0, y=190)
   
   Profession = Entry(new_window, width=17)
   Profession.place(x=250, y=35)
   Noun = Entry(new_window, width=17)
   Noun.place(x=250, y=70)
   Feeling = Entry(new_window, width=17)
   Feeling.place(x=250, y=105)
   Emotion= Entry(new_window, width=17)
   Emotion.place(x=250, y=150)
   Verb = Entry(new_window, width=17)
   Verb.place(x=250, y=190)
   
   SubmitButton = Button(new_window, text="Submit", background="Blue", font=('Times', 12), command=lambda:show_madlib2(new_window, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
   SubmitButton.place(x=150, y=270)

   new_window.mainloop()

def main():
   root_window = Tk()
   # print(dir(root_window))                             # Note: VSC type root_window. to see options or look at documentation
   # Note: lambda functions
   root_window.title(string="Mad Libs Generator")        # (variable) def title(string: str) -> None
   root_window.geometry(newGeometry='400x400')           # (variable) def geometry(newGeometry: str) -> None
   root_window.config(bg="pink")                         # Note: Hoover over config to see parameters
   root_window.resizable(width=0,height=0)
   
   # Favorites: pack, place, grid
   Label(master=root_window, text='Mad Libs Generator', font=("Times New Roman", 20), bg="#ffffff").place(x=100, y=20)

   # Note command to lambda function with no parameters
   story1_button = Button(master=root_window, text='A memorable day', font=("Times New Roman", 13),command=lambda: Story1(window=root_window),bg='Blue')
   story1_button.place(x=140, y=90)
   story2_button = Button(root_window, text='Ambitions', font=("Times New Roman", 13),command=lambda: Story2(window=root_window), bg='Yellow')
   story2_button.place(x=150, y=150)

   root_window.update()
   root_window.mainloop()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()