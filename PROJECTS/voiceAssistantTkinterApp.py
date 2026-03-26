"""
Main Purpose:
    Create a basic voice listener in tkinter

Idea stolen from:
    https://pythongeeks.org/python-voice-assistant-project/

Level: Advanced
What I learned:
    import speech_recognition as sr
    import pyttsx3
    import webbrowser

Created by HackerDu
"""

import sys
try:
    import speech_recognition as sr
except ImportError:
    print("pip3 install SpeechRecognition")
import pyttsx3
import webbrowser
import datetime
from tkinter import *
from PIL import ImageTk

# Error: Could not find PyAudio; check installation
# pip3 install pyaudio

class Assistance_Gui:
    def __init__(self, root_window):                # Note: Pass root_window as parameter
        self.root_window = root_window
        self.root_window.title("Voice Assistant")
        self.root_window.geometry('600x600')

        # Background Image (Needed)
        self.bg = ImageTk.PhotoImage(file="images/background.png")
        Label(self.root_window, image=self.bg).place(x=0, y=0)

        # Center Frame Image (Needed)
        self.centre = ImageTk.PhotoImage(file="images/frame_image.jpg")
        Label(self.root_window, image=self.centre).place(x=100, y=100, width=400, height=400)

        Button(self.root_window, text='START', font=("times new roman", 14),command=self.start_option).place(x=150, y=520)
        Button(self.root_window, text='CLOSE', font=("times new roman", 14),command=self.close_window).place(x=350, y=520)

        # Initialize speech engine
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.running = False

    def speak(self, text):
        """
        Speak Method
        """

        self.engine.say(text)
        self.engine.runAndWait()

    def start_option(self):
        """
        Start assistant app
        """
        
        if self.running:
            return                  # Prevent multiple starts

        self.running = True
        self.greet()
        self.process_commands()

    def greet(self):
        """
        Greet Method
        """

        hour = int(datetime.datetime.now().hour)

        if 0 <= hour < 12:
            wish = "Good Morning!"
        elif 12 <= hour < 18:
            wish = "Good Afternoon!"
        else:
            wish = "Good Evening!"

        self.speak("Hello Sir, " + wish + " I am your voice assistant. How may I help you?")

    def take_command(self):
        """
        Take command method
        """

        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.listener.adjust_for_ambient_noise(source)
                audio = self.listener.listen(source, timeout=5)

                print("Recognizing...")
                instruction = self.listener.recognize_google(audio)
                instruction = instruction.lower()

                print("You said:", instruction)
                return instruction

        except sr.UnknownValueError:
            print("Could not understand audio")
            self.speak("Sorry, I did not understand")
            return ""

        except sr.RequestError:
            print("Network error")
            self.speak("Network error")
            return ""

        except Exception as e:
            print("Error:", e)
            return ""

    def run_command(self):
        """
        Run command method to listen for commands and call them if necessary or just speak
        """

        instruction = self.take_command()

        if not instruction:
            return True

        if 'who are you' in instruction:
            self.speak('I am your personal voice assistant')
        elif 'what can you do' in instruction:
            self.speak('I can open websites and tell time')
        elif 'current time' in instruction:
            time_now = datetime.datetime.now().strftime('%I:%M %p')
            self.speak('Current time is ' + time_now)
        elif 'open google' in instruction:
            self.speak('Opening Google')
            webbrowser.open('https://google.com')
        elif 'open youtube' in instruction:
            self.speak('Opening Youtube')
            webbrowser.open('https://youtube.com')
        elif 'open facebook' in instruction:
            self.speak('Opening Facebook')
            webbrowser.open('https://facebook.com')
        elif 'open linkedin' in instruction:
            self.speak('Opening Linkedin')
            webbrowser.open('https://linkedin.com')
        elif 'open gmail' in instruction:
            self.speak('Opening Gmail')
            webbrowser.open('https://gmail.com')
        elif 'open stack overflow' in instruction:
            self.speak('Opening Stack Overflow')
            webbrowser.open('https://stackoverflow.com')
        elif 'shut down' in instruction:
            self.speak('Shutting down. Goodbye!')
            self.running = False
            self.close_window()
            return False
        else:
            self.speak('I did not understand, please repeat.')

        return True

    def process_commands(self):
        """
        Process loop method (non-blocking)
        """

        if self.running:
            if self.run_command():
                self.root_window.after(1000, self.process_commands)

    def close_window(self):
        """
        Close window
        """

        self.running = False
        self.root_window.destroy()

def main():
    root_window = Tk()
    root_window.resizable(width=0,height=0) # Note: Need set this before pass as parameter
    Assistance_Gui(root_window)             # Pass tkinter object as a parameter

    root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()