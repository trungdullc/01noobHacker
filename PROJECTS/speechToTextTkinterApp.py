"""
Main Purpose:
    Saved to text_to_speech.mp3
    Saved to recorded_audio.wav

Idea stolen from:
    https://pythongeeks.org/python-text-to-speech-project/

Level: Advanced
What I learned:
    from gtts import gTTS, lang
    import speech_recognition as sr
    tkinter.Text() Widget

Created by HackerDu
"""

import os, sys
from tkinter import *
from tkinter import messagebox
try:
    from gtts import gTTS, lang
except ImportError:
    print("pip3 install gtts")
try:
    import speech_recognition as sr
except ImportError:
    print("pip3 install SpeechRecognition")

class SpeechRecognizer:
    def __init__(self):
        self.root_window = Tk()
        self.root_window.geometry("500x300")
        self.root_window.title("Convert Speech to text and text to Speech")
        self.root_window.resizable(width=0,height=0)

        Label(self.root_window, text="Convert Speech to text and text to Speech").pack()
        Label(self.root_window, text="Text:").place(x=10,y=20)
        
        self.text_entry = Text(self.root_window, width=30,height=5)
        self.text_entry.place(x=80,y=20)

        Label(self.root_window, text="Accent:").place(x=10,y=110)
        self.accent_entry = Entry(self.root_window,  width=26)
        self.accent_entry.place(x=80,y=110)

        Label(self.root_window, text="Duration:").place(x=10,y=140)
        self.duration_entry = Entry(self.root_window,  width=26)
        self.duration_entry.place(x=80,y=140)

        Button(self.root_window,text='List languages', bg = 'Turquoise',fg='Red',command=self.list_languages).place(x=10,y=190)
        Button(self.root_window,text='Convert Text to Speech', bg = 'Turquoise',fg='Red',command=self.text_to_speech).place(x=130,y=190)
        Button(self.root_window,text='Convert Speech to Text', bg = 'Turquoise',fg='Red',command=self.speech_to_text).place(x=305,y=190)

        self.root_window.mainloop()

    def text_to_speech(self):
        """
        Method for converting text to speech
        """    
        
        # Read inputs given by user from textbox/Text Widget 
        text = self.text_entry.get("1.0","end-1c")
        language = self.accent_entry.get()

        # Check if the user submitted inputs
        if (len(text)<=1) | (len(language)<=0):
                messagebox.showerror(message="Enter required details")
                return
            
        # Using the inputs, convert the text to speech
        speech = gTTS(text = text, lang = language, slow = False)
        speech.save("sounds/text_to_speech.mp3")                        # Save speech to an MP3 file
        # Play the file usinf mpg123 in linux and start in windows
        # os.system("mpg123 "+"sounds/text_to_speech.mp3")              # Note: mpg123 is linux
        os.system("start sounds/text_to_speech.mp3")                    # Fix for windows, Note: this is where saved text.mp3

    def list_languages(self):
        """
        Method that list the supported languages and their keys
        """
        # Access languages and access codes using lang.tts_langs()
        messagebox.showinfo(message=list(lang.tts_langs().items()))

    def speech_to_text(self): 
        """
        Method that converts speech to text
        """
        
        # Initialize Recognizer class
        recorder = sr.Recognizer()

        try:
            duration = int(self.duration_entry.get())
        except:
            messagebox.showerror(message="Enter the duration in seconds")
            return

        # Pick correct microphone index (replace 1 with your mic)
        mic_index = 1
        mic = sr.Microphone(device_index=mic_index)

        with mic as source:  
            try:
                print("Adjusting for ambient noise...")
                recorder.adjust_for_ambient_noise(source, duration=0.5)
                # Use the microphone
                messagebox.showinfo(message="Speak into the microphone and wait after finishing the recording")
                print(f"Recording for up to {duration} seconds. Speak now...")

                # Note: Record audio from the user not what it thinks the user said
                audio_input = recorder.listen(source, timeout=2, phrase_time_limit=duration)
                print("Recording finished!")

                # Save WAV file
                with open("sounds/recorded_audio.wav", "wb") as f:
                    f.write(audio_input.get_wav_data())
                print("Saved recording as recorded_audio.wav")

                # Recognize
                text_output = recorder.recognize_google(audio_input)
                messagebox.showinfo(message="You said:\n " + text_output)        
            except sr.WaitTimeoutError:
                messagebox.showerror(message="No speech detected. Speak immediately!")
            except sr.UnknownValueError:
                messagebox.showerror(message="Couldn't understand the audio.")
            except sr.RequestError:
                messagebox.showerror(message="Google Speech Recognition service failed")
            except Exception as e:
                messagebox.showerror(message=f"Error: {e}")

def main():
    SpeechRecognizer()

if __name__ == "__main__":
    try:
         main()
    except KeyboardInterrupt:
         sys.exit()