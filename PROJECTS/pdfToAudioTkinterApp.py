"""
Main Purpose:
    Read pdf
    Convert pdf to mp3
    Convert mp3 to pdf
    Note: Didn't change to class

Idea stolen from:
    https://pythongeeks.org/python-convert-pdf-text-to-audio-speech/

Level: Advanced
What I learned:
    Didn't covert this into a class so used global keywords
    from PyPDF4.pdf import PdfFileReader, PdfFileWriter
    import pyttsx3
    from speech_recognition import Recognizer, AudioFile
    from pydub import AudioSegment

Created by HackerDu
"""

import os, sys
import tkinter 
from tkinter import messagebox, Label, Button, Entry, IntVar, StringVar, LEFT
from tkinter import filedialog

try:
    from path import Path
except ImportError:
    print("pip3 install path")
try:
    from PyPDF4.pdf import PdfFileReader, PdfFileWriter
except ImportError:
    print("pip3 install PyPDF4")
import pyttsx3
try:
    from speech_recognition import Recognizer, AudioFile
except ImportError:
    print("pip3 install SpeechRecognition")
try:
    from pydub import AudioSegment
except ImportError:
    print("pip3 install pydub")

pdfPath = None

def read(start_pgNo, end_pgNo):
    """
    Function to open the PDF selected and read text from it
    """

    path = filedialog.askopenfilename()
    pdf_location = open(path, 'rb')                 # Opening the PDF 
    pdf_reader = PdfFileReader(pdf_location)        # Creating a PDF reader object for the opened PDF
    speaker = pyttsx3.init()                        # Initiating a speaker object
    
    start = start_pgNo.get()                        # Getting starting page number input
    end = end_pgNo.get()                            # Getting ending page number input
    
    # Reading all the pages from start to end page number
    for i in range(start,end+1):  
        page = pdf_reader.getPage(i)                # Getting the page 
        txt = page.extractText()                    # Extracting the text 
        speaker.say(txt)                            # Getting the audio output of the text
        speaker.runAndWait()                        # Processing the voice commands

def pdf_to_audio():
    """
    Function to create a GUI and get required inputs for PDF to Audio Conversion 
    """
    
    new_window = tkinter.Tk() 
    new_window.title("PDF to Audio converter")
    new_window.geometry('500x400')
    new_window.config(bg='snow3')
    
    start_page_number = IntVar(new_window)              # Variable to hold the starting page number
    end_page_number = IntVar(new_window)                # Variable to hold the ending page number
    
    Label(new_window, text='PDF to Audio converter',fg='black', font=('Courier', 15)).place(x=60, y=10)
    Label(new_window, text='Enter the start and the end page to read. If you want to read a single \npage please enter the start page and enter the next page as the end page:', anchor="e", justify=LEFT).place(x=20, y=90)
    
    Label(new_window, text='Start Page No.:').place(x=100, y=140)

    startPg = Entry(new_window, width=20, textvariable=start_page_number)
    startPg.place(x=100, y=170)
    
    Label(new_window, text='End Page No.:').place(x=250, y=140)
        
    endPg = Entry(new_window, width=20, textvariable=end_page_number)
    endPg.place(x=250, y=170)
     
    Label(new_window, text='Click the below button to Choose the pdf and start to Listen:').place(x=100, y=230)
    
    # Button(wn1, text="Click Me", bg='ivory3',font=('Courier', 13), command=read).place(x=230, y=260)
    Button(new_window, text="Click Me", bg='ivory3',font=('Courier', 13), command=lambda: read(start_page_number, end_page_number)).place(x=230, y=260)

    new_window.mainloop()

def write_text(filename, text):
    """
    Function to update the PDF file with the text, both given as parameters
    """

    writer = PDFwriter()                        # Creating a PDF writer object
    writer.addBlankPage(72, 72)                 # Creating a blank page
    pdfPath = Path(filename)                    # Getting the path of the PDF 
    with pdf_path.open('ab') as output_file:    # Opening the PDF 
        writer.write(output_file)               # Saving the text in the writer object
        output_file.write(text)                 # Writing the text in the PDF
            
def convert():
    """
    Function to convert audio into text
    """

    path = filedialog.askopenfilename()         # Getting the location of the audio file 
    audioLoc = open(path, 'rb')                 # Opening the audio file
    
    pdf_loc=pdfPath.get()                       # Getting the path of the PDF
    
    # Getting the name and extension of the audio file and checking if it is mp3 or wav
    audioFileName = os.path.basename(audioLoc).split('.')[0]
    audioFileExt = os.path.basename(audioLoc).split('.')[1]
    if audioFileExt != 'wav' and audioFileExt != 'mp3':
        messagebox.showerror('Error!', 'The format of the audio file should be either "wav" and "mp3".')
        
    # If mp3 file converting it into wav file
    if audioFileExt == 'mp3':
        audio_file = AudioSegment.from_file(Path(audioLoc), format='mp3')
        audio_file.export(f'{audioFileName}.wav', format='wav')
    source_file = f'{audioFileName}.wav'
    
    # Creating a recognizer object and converting the audio into text
    recog= Recognizer()

    with AudioFile(source_file) as source:
        recog.pause_threshold = 5
        speech = recog.record(source)
        text = recog.recognize_google(speech)
        write_text(pdf_loc, text)

# Function to create a GUI and get required inputs for Audio to PDF Conversion 
def audio_to_pdf():
    new_window= tkinter.Tk() 
    new_window.title("Audio to PDF converter")
    new_window.geometry('500x400')
    new_window.config(bg='snow3')
    
    pdfPath = StringVar(new_window)         # Variable to get the PDF path input
    
    Label(new_window, text='Audio to PDF converter',fg='black', font=('Courier', 15)).place(x=60, y=10)

    Label(new_window, text='Enter the PDF File location where you want to save (with extension):').place(x=20, y=50)
    Entry(new_window, width=50,textvariable=pdfPath).place(x=20, y=90)
    
    Label(new_window, text='Choose the Audio File location that you want to read (.wav or .mp3 extensions only):', fg='black').place(x=20, y=130)
    
    Button(new_window, text='Choose', bg='ivory3',font=('Courier', 13), command=convert).place(x=50, y=170)

    new_window.mainloop()

def main():
    # Declaring global variables related to PDF to Speech conversion
    global end_pgNo ,start_pgNo
    global LEFT, PDFwriter, pdf_path, pdfPath

    root_window = tkinter.Tk() 
    root_window.title("PDF to Audio and Audio to PDF converter")
    root_window.geometry('700x300')
    root_window.config(bg='LightBlue1')
    
    Label(root_window, text='PDF to Audio and Audio to PDF converter',fg='black', font=('Courier', 15)).place(x=40, y=10)

    Button(root_window, text="Convert PDF to Audio", bg='ivory3',font=('Courier', 15), command=pdf_to_audio).place(x=230, y=80)
    Button(root_window, text="Convert Audio to PDF", bg='ivory3',font=('Courier', 15), command=audio_to_pdf).place(x=230, y=150)

    root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()