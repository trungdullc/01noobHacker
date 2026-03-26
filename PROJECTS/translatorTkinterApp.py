"""
Main Purpose:
   https://pypi.org/project/googletrans/
   Translator App using google translator
   
Idea stolen from:
   https://pythongeeks.org/python-language-translator/

Level: Intermediate
What I learned:
   Sometimes newer version of module changes functions and your program fucks up because of it
      pip3 uninstall googletrans ❤️
      pip3 list ❤️
      pip3 show googletrans ❤️
      pip3 install googletrans==4.0.0-rc1 ❤️
   import googletrans
   from googletrans import Translator

Created by HackerDu
"""

import sys
try:
    import googletrans
    from googletrans import Translator
except ImportError:
    print("pip3 install googletrans==4.0.0-rc1")
from tkinter import *
from tkinter import messagebox

class TranslatorApp:
   def __init__(self):
      # Note: typecast dictionary to str to concat
      print("DEBUG (see list of languages): " + str(googletrans.LANGUAGES))

      self.root_window = Tk()
      self.root_window.geometry("500x300")
      self.root_window.title("Language Translator")
      self.root_window.resizable(0,0)

      # Import the Translator class which will read the input and translate
      # Default translation is done by detection of input and to english
      self.translator_object = Translator()
      
      # Title of the app
      Label(self.root_window, text="Language Translator Using Python",font=("Gayathri", 12)).pack()
      
      # Read inputs Text input
      Label(self.root_window, text="Text to translate:").place(x=10,y=20)
      self.text_entry = Text(self.root_window, width=40, height=5,font=("Ubuntu Mono",12))
      self.text_entry.place(x=130,y=20)
      
      # Source language input
      Label(self.root_window, text="Source language (empty: auto-detect):").place(x=10,y=120)
      self.src_entry = Text(self.root_window, width=20,height=1,font=("Ubuntu Mono",12))
      self.src_entry.place(x=275,y=120)
      
      # Destination input
      Label(self.root_window, text="Target language (empty: english-default):").place(x=10,y=150)
      self.dest_entry = Text(self.root_window, width=20,height=1,font=("Ubuntu Mono",12))
      self.dest_entry.place(x=300,y=150)

      # Translate function and clear function activated through buttons
      Button(self.root_window,text='Translate', bg = 'Turquoise',command=self.translate_function).place(x=160,y=190)
      Button(self.root_window,text='Clear', bg = 'Turquoise',command=self.clear).place(x=270,y=190)
      
      self.root_window.mainloop()

   def translate_function(self):
      """
      Since default options are allowed, we check for explicitly given source and destination languages
      """
      
      # Check if the source and target languages are empty  
      if (len(self.src_entry.get("1.0","end-1c"))>1):
         src_v = self.src_entry.get("1.0","end-1c").lower()
         src_v =src_v.replace(" ","")
      else:
         src_v = None
         
      if (len(self.dest_entry.get("1.0","end-1c"))>1):
         dest_v = self.dest_entry.get("1.0","end-1c").lower()
         dest_v =dest_v.replace(" ","")
      else:
         dest_v = None

      # Check if the text is empty. If so, prompt user to key it
      if (len(self.text_entry.get("1.0","end-1c"))<=1):
         messagebox.showerror(message="Enter valid text")
      else:
         # Send the parameters based on user input provided  
         text_v = self.text_entry.get("1.0","end-1c")

         if (not src_v) & (not dest_v):
            translated_text = self.translator_object.translate(text_v)
         elif (not src_v):
            translated_text = self.translator_object.translate(text_v,dest=dest_v)
         elif (not dest_v):
            translated_text = self.translator_object.translate(text_v,src=src_v)
         else:
            translated_text = self.translator_object.translate(text_v,src=src_v,dest=dest_v)
         
         # Display translated text on a prompt
         messagebox.showinfo(message = "TRANSLATED TEXT: "+ (translated_text.text))
         
         """
         Note: translate() is defined as in newer version googletrans 4.x:
            async def translate(...)
         Fix: Downgrade googletrans without changing code
            pip3 uninstall googletrans
            pip3 install googletrans==4.0.0-rc1
         Hacker:
            pip3 list                       # shows all packages and version number install ❤️❤️❤️❤️❤️
            pip3 show googletrans           # shows specific ❤️❤️❤️❤️❤️
         """

   def clear(self):
      """
      Method to clear text boxes
      """
      self.dest_entry.delete("1.0","end-1c")
      self.src_entry.delete("1.0","end-1c")
      self.text_entry.delete("1.0","end-1c")

def main():
   TranslatorApp()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()