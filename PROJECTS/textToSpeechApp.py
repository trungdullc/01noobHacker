"""
Text To Speech Talker

An example program using the text-to-speech features of the pyttsx3 module.

Level: Beginner
What I learned:
    pyttsx3 module
"""

import sys

try:
    import pyttsx3
except ImportError:
    print('The pyttsx3 module needs to be installed to run this')
    print('program. On Windows, open a Command Prompt and run:')
    print('pip install pyttsx3')
    print('On macOS and Linux, open a Terminal and run:')
    print('pip3 install pyttsx3')
    sys.exit()

def main():
    tts = pyttsx3.init()                        # Initialize the TTS engine

    # RATE
    rate = tts.getProperty('rate')              # getting details of current speaking rate
    print (rate)                                # printing current voice rate, 200
    tts.setProperty('rate', 115)                # setting up new voice rate

    # VOICE
    voices = tts.getProperty('voices')          # getting details of current voice
    # tts.setProperty('voice', voices[0].id)    # changing index, changes voices. o for male
    tts.setProperty('voice', voices[1].id)      # changing index, changes voices. 1 for female

    print('Text To Speech Talker')
    print('Text-to-speech using the pyttsx3 module, which in turn uses')
    print('the NSSpeechSynthesizer (on macOS), SAPI5 (on Windows), or')
    print('eSpeak (on Linux) speech engines.')
    print()
    print('Enter the text to speak, or QUIT to quit.')

    while True:
        text = input('> ')

        if text.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        tts.say(text)           # Add some text for the TTS engine to say
        tts.runAndWait()        # Make the TTS engine say it

if __name__ == "__main__":
    main()