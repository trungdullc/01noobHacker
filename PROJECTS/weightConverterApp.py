"""
Main Purpose:
    Learn how to convert to different measurements and display using tkinter

Idea stolen from:
    https://pythongeeks.org/python-weight-converter-tkinter/

Level: Beginner
What I learned:
    Relearn .pack() vs .place() and .grid()

Created by HackerDu
"""

import sys
import tkinter
from tkinter import *

class WeightConverter:
    def __init__(self):
        self.root_window = Tk()
        self.root_window.title("Weight Converter")
        self.root_window.geometry("500x500")
        self.root_window.resizable(0,0)

        Label(self.root_window,text="WEIGHT CONVERTER",font=("Arial", 20 ),bg="black",fg='yellow').pack()

        self.kg = tkinter.IntVar()

        Label(self.root_window,text="Enter the weight in Kgs",font=("Arial", 14 )).pack()
        Entry(self.root_window,textvariable=self.kg).pack()

        Button(self.root_window,text="Convert to Gram",bg="blue",command=self.convert_to_gram).pack()
        Button(self.root_window,text="Convert to Ounce",bg="blue",command=self.convert_to_ounce).pack()
        Button(self.root_window,text="Convert to Pound",bg="blue",command=self.convert_to_pound).pack()

        self.root_window.mainloop()

    def convert_to_gram(self):
        kg_entry = self.kg.get()
        gram = float(kg_entry) * 1000

        Label(self.root_window,text="This weight in grams would be",font=("Arial", 12 )).pack()
        Label(self.root_window,text=gram,bg="red").pack()

    def convert_to_ounce(self):
        kg1 = self.kg.get()
        ounce = float(kg1) * 35.274

        Label(self.root_window,text="This weight in ounce would be",font=("Arial", 12 )).pack()
        Label(self.root_window,text=ounce,bg="red").pack()

    def convert_to_pound(self):
        kg1 = self.kg.get()
        pound = float(kg1) * 2.20462

        Label(self.root_window,text="This weight in pound would be",font=("Arial", 12 )).pack()
        Label(self.root_window,text=pound,bg="red").pack()

def main():
    WeightConverter()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()