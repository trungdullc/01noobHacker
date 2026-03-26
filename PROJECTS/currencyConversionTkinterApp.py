"""
Main Purpose:
    Learn about tkinter.OptionMenu() and how it automatically assigns value

Idea stolen from:
    https://pythongeeks.org/python-weight-converter-tkinter/

Level: Intermediate
What I learned:
    tkinter.END
    tkinter.OptionMenu
    from forex_python.converter import CurrencyRates for dynamic exchange rates
    
Created by HackerDu
"""

import sys
from tkinter import *
import tkinter.messagebox

class Currency:
    def RealTimeCurrencyConversion(self):
        """
        Import a dynamic currency converterto help with current rates
        """
   
        try:
            from forex_python.converter import CurrencyRates        # Get current rates vs hardcoding it
        except ImportError:
            print("pip3 install forex_python")

        currencyRates = CurrencyRates()

        from_currency = currency_option_1.get()
        to_currency = currency_option_2.get()

        if (Amount1_field.get() == ""):
            tkinter.messagebox.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")
        elif (from_currency == "currency" or to_currency == "currency"):
            tkinter.messagebox.showinfo("Error !!", "Currency Not Selected.\n Please select FROM and TO Currency form menu.")
        else:
            new_amt = currencyRates.convert(from_currency, to_currency, float(Amount1_field.get()))     # Main logic
            new_amount = float("{:.4f}".format(new_amt))
            Amount2_field.insert(0, str(new_amount))

    def clear_all(self):
        """
        Clearn the Entry fields
        """
        Amount1_field.delete(0, tkinter.END)
        Amount2_field.delete(0, tkinter.END)

def main():
    global Amount1_field, Amount2_field, currency_option_1, currency_option_2

    currency = Currency()

    root_window = tkinter.Tk()
    root_window.title("Currency Conversion")
    root_window.configure(background='#e6e5e5')
    root_window.geometry("700x400")
    root_window.resizable(width=0,height=0)

    Tops = Frame(master=root_window, bg='#e6e5e5', pady=2, width=1850, height=100, relief="ridge")
    Tops.grid(row=0, column=0)

    # Note: master=Tops
    # W is tkinter.W
    head_label = tkinter.Label(master=Tops, font=('lato black', 19, 'bold'), text='Currency Converter', bg='#e6e5e5', fg='black')
    head_label.grid(row=1, column=0, sticky=W)

    currency_option_1, currency_option_2 = tkinter.StringVar(master=root_window), tkinter.StringVar(master=root_window)
    currency_option_1.set("currency")
    currency_option_2.set("currency")

    currency_code_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"]

    # Gives empty padding
    Label(root_window, font=('lato black', 27, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black").grid(row=1, column=0, sticky=W)

    tkinter.Label(root_window, font=('lato black', 15, 'bold'), text="Amount: ", bg="#e6e5e5", fg="black").grid(row=2, column=0, sticky=W)
    tkinter.Label(root_window, font=('lato black', 15, 'bold'), text="From Currency: ", bg="#e6e5e5", fg="black").grid(row=3, column=0, sticky=W)
    tkinter.Label(root_window, font=('lato black', 15, 'bold'), text="To Currency: ", bg="#e6e5e5", fg="black").grid(row=4, column=0, sticky=W)

    Label(root_window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black").grid(row=5, column=0, sticky=W)
    Label(root_window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black").grid(row=7, column=0, sticky=W)

    # Note: Needed \t\t\t or sticky acts wierdcould have done columnspan
    tkinter.Label(root_window, font=('lato black', 15, 'bold'), text="Converted Amount:  \t\t\t", bg="#e6e5e5", fg="black").grid(row=8, column=0, sticky=W)

    # New widget tkinter.OptionMenu accepts the currency_code_list and automatically assigns value to currency_option_1 and currency_option_2
    # Note: the * before the list makes it go vertical ❤️
    tkinter.OptionMenu(root_window, currency_option_1, *currency_code_list).grid(row=3, column=0, ipadx=45, sticky=E)
    tkinter.OptionMenu(root_window, currency_option_2, *currency_code_list).grid(row=4, column=0, ipadx=45, sticky=E)

    Amount1_field = tkinter.Entry(root_window)
    Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)

    Amount2_field = tkinter.Entry(root_window)
    Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)

    Button(root_window, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="lightblue", fg="white", 
           command=currency.RealTimeCurrencyConversion).grid(row=6, column=0)

    Label(root_window, font=('lato black', 7, 'bold'), text="", padx=2, pady=2, bg="#e6e5e5", fg="black").grid(row=9, column=0, sticky=W)

    Button(root_window, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="lightblue", fg="white", 
           command=currency.clear_all).grid(row=10, column=0)

    root_window.mainloop()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()