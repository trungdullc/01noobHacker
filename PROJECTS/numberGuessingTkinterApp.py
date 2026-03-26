"""
Main Purpose:
   Learn the importance of global keyword when other functions use it, best to place in main functions
   Remember that when a function is left all variables get destroyed
Idea stolen from:
   https://pythongeeks.org/python-number-guessing-game-project-with-source-code/

Level: Intermediate
What I learned:
   global keyword best to be used in main function
   tkinter.StringVar() is a class
   tkinter.IntVar() is a class
	.place() using relx and rely instead of x and y
     
Created by HackerDu
"""

import sys, random
from tkinter import *

RANDOM_NUMBER = random.randint(1,50)

class NumberGuesser:
	"""
	Remember when creating a class use self for all functions
	Need to initialize object in main function and use numberGuesser.check_guess when Button is clicked in command parameter
	"""
	def check_guess(self):
		"""
		Function to check if guess is correct or not when Button is clicked,
		not using lambda function since return is more complex
		"""
		my_guess = guess.get()									# Assign guess.get() so doesn't call it multiple times
		final_score.set(score.get())

		# Algorithm to check if my_guess equals RANDOM_NUMBER
		if score.get() > 0:										# Main loop instead of while
			if RANDOM_NUMBER == my_guess:
				hint.set("Congratulation YOU WON!!!")		# Remember: when you set this goes back to root_window.mainloop() to update
				score.set(score.get()-1)
				final_score.set(score.get())
			elif RANDOM_NUMBER > my_guess:
				hint.set("Your guess was too low: Guess a number higher ")
				score.set(score.get()-1)
				final_score.set(score.get())
			elif RANDOM_NUMBER < my_guess:
				hint.set("Your guess was too High: Guess a number Lower ")
				score.set(score.get()-1)
				final_score.set(score.get())
		else:
			hint.set("Game Over You Lost")

def main():
   global guess, final_score, score, hint				# Important: Need to declare global if used by other functions

   numberGuesser = NumberGuesser()
   
   root_window = Tk()
   root_window.geometry("750x750")
   root_window.title("Guess the number")
   root_window.resizable(width=0,height=0)
   
	# Assign data types
   # Note: Using StringVar() and IntVar() instead of str and int can use .get() with textvariable and .place()
   hint = StringVar()                               # tkinter.StringVar() is a class
   # print(type(hint))                              # <class 'tkinter.StringVar'>
   score = IntVar()
   final_score = IntVar()
   guess = IntVar()

	# Assign values
   hint.set("Guess a number between 1 to 50 ")
   score.set(5)
   final_score.set(score.get())
   
	# Note: .place() using relx and rely instead of x and y ⭐
   # Note: when assign as textvariable can use .get() from other functions instead of text ❤️❤️❤️❤️❤️
   Entry(root_window, textvariable=guess, width=3,font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
   Entry(root_window, textvariable=hint, width=50,font=('Courier', 15), relief=GROOVE,bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
   Entry(root_window, text=final_score, width=2,font=('Ubuntu', 24), relief=GROOVE).place(relx=0.61, rely=0.85, anchor=CENTER)
   
   Label(root_window, text='I challenge you to guess the number ',font=("Courier", 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
   Label(root_window, text='Score out of 5',font=("Courier", 25)).place(relx=0.3, rely=0.85, anchor=CENTER)
   
	# Used function instead of lambda for command
   Button(root_window, width=8, text='CHECK', font=('Courier', 25), command=numberGuesser.check_guess, relief=GROOVE,bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

   root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()