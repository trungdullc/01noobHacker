"""
Main Purpose:
   Create basic Hangman CLI

Idea stolen from:
   https://pythongeeks.org/python-hangman-word-guessing-game-project/

Level: Intermediate
What I learned:
   This does only 1 letter at a time not all glitch
   TypeError: 'str' object does not support item assignment
   Don't use globals in a class
   builtins.exit()
   
Created by HackerDu
"""

import random, sys
import time

WORDS = ['programming', 'data', 'python', 'code', 'geeks', 'computer', 'engineer', 'word', 'science', 
         'machine', 'java', 'college', 'player', 'mobile', 'image'] 

class Hangman:
   def __init__(self):
      """"
      Best not to use global in class
      """

      self.CHOSEN_WORD = random.choice(WORDS)
      self.count = 0
      self.length = len(self.CHOSEN_WORD)
      self.display = '*' * self.length          # Displays ***** depends on length
      self.already_guessed = []                 # Keeps track of already_guessed characters
      self.playGame = ""                        # Input checks to see if want to retry

      # Initial Steps to invite in the game
      print("\n\n***  Welcome to Hangman Game ***\n")
      name = input("Enter your name: ")
      print("Good Luck!", name)
      time.sleep(2)
      print("LET'S PLAY HANGMAN! A word will be chosen randomly. You will have to guess it!\n")
      time.sleep(3)
      self.hangman_init()

   def play_again(self):
      """
      Ask if want to replay game
      """

      playGame = input("Do You want to play again? y = yes, n = no \n")
      
      # Note: Uses not in style
      while playGame not in ["y", "n","Y","N"]:
         playGame = input("Do You want to play again? y = yes, n = no \n")

      if playGame == "y":
         main()
      elif playGame == "n":
         print("Thanks For Playing!")
         exit()                              # Note: There is a exit() in builtins.py not sys.exit()

   def hangman_init(self):
      """
      Initializing all the conditions 
      """

      lives = 6
      guess = input("This is the Hangman Word: " + self.display + "\nEnter your guess: \n").strip()

      if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
         print("Invalid Input, Try a letter\n")
         self.hangman_init()                       # Retry method until valid input
      elif guess in self.CHOSEN_WORD:
         # This is where algorithm decides if correct character was guessed
         self.already_guessed.extend([guess])
         index = self.CHOSEN_WORD.find(guess)      # if finds only the first index so it not act like real hangman
         self.CHOSEN_WORD = self.CHOSEN_WORD[:index] + "_" + self.CHOSEN_WORD[index + 1:]
         # One way of modifying the display ❤️
         self.display = self.display[:index] + guess + self.display[index + 1:]
         # TypeError: 'str' object does not support item assignment
         print(self.display + "\n")
      elif guess in self.already_guessed:
         print("Try another letter.\n")
      else:                      
         self.count += 1

         if self.count == 1:              # Guess wrong letter you get hang
            time.sleep(1)
               
            print("H A N G M A N\n"
               "  +---+\n"
               "  |   |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "=========\n")
            print("Wrong guess. " + str(lives - self.count) + " guesses remaining\n")
         elif self.count == 2:
            time.sleep(1)

            print("H A N G M A N\n"
               "  +---+\n"
               "  |   |\n"
               "  o   |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "=========\n")
            print("Wrong guess. " + str(lives - self.count) + " guesses remaining\n")
         elif self.count == 3:
            time.sleep(1)

            print("H A N G M A N\n"
               "  +---+\n"
               "  |   |\n"
               "  o   |\n"
               "  |   |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "=========\n")
            print("Wrong guess. " + str(lives - self.count) + " guesses remaining\n")
         elif self.count == 4:
            time.sleep(1)
            print("H A N G M A N\n"
               "  +---+\n"
               "  |   |\n"
               "  o   |\n"
               " /|\  |\n"
               "      |\n"
               "      |\n"
               "      |\n"
               "=========\n")
            print("Wrong guess. " + str(lives - self.count) + " guesses remaining\n")
         elif self.count == 5:
            time.sleep(1)

            print("H A N G M A N\n"
               "  +---+\n"
               "  |   |\n"
               "  o   |\n"
               " /|\  |\n"
               " /    |\n"
               "      |\n"
               "      |\n"
               "=========\n")
            print("Wrong guess. " + str(lives - self.count) + " last guess remaining\n")
         elif self.count == 6:
            time.sleep(1)
            
            print("H A N G M A N\n"
               "  +---+\n"
               "  |   |\n"
               "  o   |\n"
               " /|\  |\n"
               " / \  |\n"
               "      |\n"
               "      |\n"
               "=========\n")
            print("Wrong guess. You are hanged, Sorry!!!\n")
            print("The word was:",self.already_guessed,self.CHOSEN_WORD)
            self.play_again()

      if self.CHOSEN_WORD == '_' * self.length:
         print("Congrats, you guessed the word! YOU WIN!!")
         self.play_again()
      elif self.count != lives:
         self.hangman_init()

def main():    
   Hangman()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()