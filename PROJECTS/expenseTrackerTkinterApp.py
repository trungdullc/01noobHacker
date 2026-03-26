"""
Main Purpose:
	Using DataEntry data type to create a expense tracker
	Saved to ExpenseTracker.db

Idea stolen from:
	https://pythongeeks.org/python-expense-tracker/

Level: Advanced
What I learned:
	tkinter.DoubleVar()
	from tkcalendar import DateEntry

Created by HackerDu
"""

import sys
import datetime
import sqlite3
try:
	from tkcalendar import DateEntry									# Note: datetime data type a pain to work with
except ImportError:
	print("pip3 install tkcalendar")

from tkinter import *
import tkinter.messagebox as mb
import tkinter.ttk as ttk

class ExpenseTracker:
	def __init__(self):
		# Connecting to sqlite3 offline Database
		self.connector = sqlite3.connect("data/ExpenseTracker.db")       # Important: This where database stored
		self.cursor = self.connector.cursor()

		self.connector.execute(
			'CREATE TABLE IF NOT EXISTS ExpenseTracker (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Date DATETIME, Payee TEXT, Description TEXT, Amount FLOAT, ModeOfPayment TEXT)'
		)
		self.connector.commit()

		# Backgrounds anf Fonts
		dataentery_frame_bg = 'Red'
		buttons_frame_bg = 'Tomato'
		self.hlb_btn_bg = 'IndianRed'

		lbl_font = ('Georgia', 13)
		entry_font = 'Times 13 bold'
		self.btn_font = ('Gill Sans MT', 13)

		self.root_window = Tk()
		self.root_window.title('Expense Tracker')
		self.root_window.geometry('1200x550')
		self.root_window.resizable(0,0)

		Label(self.root_window, text='EXPENSE TRACKER', font=('Noto Sans CJK TC', 15, 'bold'), bg=self.hlb_btn_bg).pack(side=TOP, fill=X)

		# Note: DoubleVar variable
		self.description = StringVar()
		self.amnt = DoubleVar()
		self.payee = StringVar()
		self.method_of_payment = StringVar(value='Cash')

		# Frames
		self.data_entry_frame = Frame(self.root_window, bg=dataentery_frame_bg)
		self.data_entry_frame.place(x=0, y=30, relheight=0.95, relwidth=0.25)

		buttons_frame = Frame(self.root_window, bg=buttons_frame_bg)
		buttons_frame.place(relx=0.25, rely=0.05, relwidth=0.75, relheight=0.21)

		tree_frame = Frame(self.root_window)
		tree_frame.place(relx=0.25, rely=0.26, relwidth=0.75, relheight=0.74)

		# Data Entry Frame
		Label(self.data_entry_frame, text='Date (M/DD/YY) :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=50)
		self.date = DateEntry(self.data_entry_frame, date=datetime.datetime.now().date(), font=entry_font)
		self.date.place(x=160, y=50)

		Label(self.data_entry_frame, text='Payee\t             :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=230)
		Entry(self.data_entry_frame, font=entry_font, width=31, text=self.payee).place(x=10, y=260)

		Label(self.data_entry_frame, text='Description           :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=100)
		Entry(self.data_entry_frame, font=entry_font, width=31, text=self.description).place(x=10, y=130)

		Label(self.data_entry_frame, text='Amount\t             :', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=180)
		Entry(self.data_entry_frame, font=entry_font, width=14, text=self.amnt).place(x=160, y=180)

		Label(self.data_entry_frame, text='Mode of Payment:', font=lbl_font, bg=dataentery_frame_bg).place(x=10, y=310)
		dd1 = OptionMenu(self.data_entry_frame, self.method_of_payment, *['Cash', 'Cheque', 'Credit Card', 'Debit Card', 'Paytm', 'Google Pay', 'Razorpay'])
		dd1.place(x=160, y=305)     ;     dd1.configure(width=10, font=entry_font)

		Button(self.data_entry_frame, text='Add expense', command=self.add_another_expense, font=self.btn_font, width=30,
			bg=self.hlb_btn_bg).place(x=10, y=395)
		Button(self.data_entry_frame, text='Convert to words before adding', font=self.btn_font, width=30, bg=self.hlb_btn_bg).place(x=10,y=450)

		# Buttons' Frame
		Button(buttons_frame, text='Delete Expense', font=self.btn_font, width=25, bg=self.hlb_btn_bg, command=self.remove_expense).place(x=30, y=5)

		Button(buttons_frame, text='Clear Fields in DataEntry Frame', font=self.btn_font, width=25, bg=self.hlb_btn_bg,
			command=self.clear_fields).place(x=335, y=5)

		Button(buttons_frame, text='Delete All Expenses', font=self.btn_font, width=25, bg=self.hlb_btn_bg, command=self.remove_all_expenses).place(x=640, y=5)

		Button(buttons_frame, text='View Selected Expense\'s Details', font=self.btn_font, width=25, bg=self.hlb_btn_bg,
			command=self.view_expense_details).place(x=30, y=65)

		Button(buttons_frame, text='Edit Selected Expense', command=self.edit_expense, font=self.btn_font, width=25, bg=self.hlb_btn_bg).place(x=335,y=65)

		Button(buttons_frame, text='Convert Expense to a sentence', font=self.btn_font, width=25, bg=self.hlb_btn_bg,
			command=self.selected_expense_to_words).place(x=640, y=65)

		# Treeview Frame
		self.table = ttk.Treeview(tree_frame, selectmode=BROWSE, columns=('ID', 'Date', 'Payee', 'Description', 'Amount', 'Mode of Payment'))

		X_Scroller = Scrollbar(self.table, orient=HORIZONTAL, command=self.table.xview)
		Y_Scroller = Scrollbar(self.table, orient=VERTICAL, command=self.table.yview)
		X_Scroller.pack(side=BOTTOM, fill=X)
		Y_Scroller.pack(side=RIGHT, fill=Y)

		self.table.config(yscrollcommand=Y_Scroller.set, xscrollcommand=X_Scroller.set)

		self.table.heading('ID', text='S No.', anchor=CENTER)
		self.table.heading('Date', text='Date', anchor=CENTER)
		self.table.heading('Payee', text='Payee', anchor=CENTER)
		self.table.heading('Description', text='Description', anchor=CENTER)
		self.table.heading('Amount', text='Amount', anchor=CENTER)
		self.table.heading('Mode of Payment', text='Mode of Payment', anchor=CENTER)

		self.table.column('#0', width=0, stretch=NO)
		self.table.column('#1', width=50, stretch=NO)
		self.table.column('#2', width=95, stretch=NO)  				# Date column
		self.table.column('#3', width=150, stretch=NO)  			# Payee column
		self.table.column('#4', width=325, stretch=NO)  			# Title column
		self.table.column('#5', width=135, stretch=NO)  			# Amount column
		self.table.column('#6', width=125, stretch=NO)  			# Mode of Payment column

		self.table.place(relx=0, y=0, relheight=1, relwidth=1)

		self.list_all_expenses()

		self.root_window.update()
		self.root_window.mainloop()

	def list_all_expenses(self):
		self.table.delete(*self.table.get_children())

		all_data = self.connector.execute('SELECT * FROM ExpenseTracker')
		data = all_data.fetchall()

		for values in data:
			self.table.insert('', END, values=values)

	def view_expense_details(self):
		if not self.table.selection():
			mb.showerror('No expense selected', 'Please select an expense from the table to view its details')

		current_selected_expense = self.table.item(self.table.focus())
		values = current_selected_expense['values']

		expenditure_date = datetime.date(int(values[1][:4]), int(values[1][5:7]), int(values[1][8:]))

		self.date.set_date(expenditure_date) ; self.payee.set(values[2]) ; self.description.set(values[3]) ; self.amnt.set(values[4]) ; self.method_of_payment.set(values[5])

	def clear_fields(self):
		today_date = datetime.datetime.now().date()

		self.description.set('') ; self.payee.set('') ; self.amnt.set(0.0) ; self.method_of_payment.set('Cash'), self.date.set_date(today_date)
		self.table.selection_remove(*self.table.selection())

	def remove_expense(self):
		if not self.table.selection():
			mb.showerror('No record selected!', 'Please select a record to delete!')
			return

		current_selected_expense = self.table.item(self.table.focus())
		values_selected = current_selected_expense['values']

		surety = mb.askyesno('Are you sure?', f'Are you sure that you want to delete the record of {values_selected[2]}')

		if surety:
			self.connector.execute('DELETE FROM ExpenseTracker WHERE ID=%d' % values_selected[0])
			self.connector.commit()

			self.list_all_expenses()
			mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')

	def remove_all_expenses(self):
		surety = mb.askyesno('Are you sure?', 'Are you sure that you want to delete all the expense items from the database?', icon='warning')

		if surety:
			self.table.delete(*self.table.get_children())

			self.connector.execute('DELETE FROM ExpenseTracker')
			self.connector.commit()

			self.clear_fields()
			self.list_all_expenses()
			mb.showinfo('All Expenses deleted', 'All the expenses were successfully deleted')
		else:
			mb.showinfo('Ok then', 'The task was aborted and no expense was deleted!')

	def add_another_expense(self):
		if not self.date.get() or not self.payee.get() or not self.description.get() or not self.amnt.get() or not self.method_of_payment.get():
			mb.showerror('Fields empty!', "Please fill all the missing fields before pressing the add button!")
		else:
			self.connector.execute(
			'INSERT INTO ExpenseTracker (Date, Payee, Description, Amount, ModeOfPayment) VALUES (?, ?, ?, ?, ?)',
			(self.date.get_date(), self.payee.get(), self.description.get(), self.amnt.get(), self.method_of_payment.get())
			)
			self.connector.commit()

			self.clear_fields()
			self.list_all_expenses()
			mb.showinfo('Expense added', 'The expense whose details you just entered has been added to the database')

	def edit_expense(self):
		def edit_existing_expense():
			current_selected_expense = self.table.item(self.table.focus())
			contents = current_selected_expense['values']

			self.connector.execute('UPDATE ExpenseTracker SET Date = ?, Payee = ?, Description = ?, Amount = ?, ModeOfPayment = ? WHERE ID = ?',
							(self.date.get_date(), self.payee.get(), self.description.get(), self.amnt.get(), self.method_of_payment.get(), contents[0]))
			self.connector.commit()

			self.clear_fields()
			self.list_all_expenses()

			mb.showinfo('Data edited', 'We have updated the data and stored in the database as you wanted')
			edit_btn.destroy()
			return

		if not self.table.selection():
			mb.showerror('No expense selected!', 'You have not selected any expense in the table for us to edit; please do that!')
			return

		self.view_expense_details()

		edit_btn = Button(self.data_entry_frame, text='Edit expense', font=self.btn_font, width=30, bg=self.hlb_btn_bg, command=edit_existing_expense)
		edit_btn.place(x=10, y=395)

	def selected_expense_to_words(self):
		if not self.table.selection():
			mb.showerror('No expense selected!', 'Please select an expense from the table for us to read')
			return

		current_selected_expense = self.table.item(self.table.focus())
		values = current_selected_expense['values']

		message = f'Your expense can be read like: \n"You paid {values[4]} to {values[2]} for {values[3]} on {values[1]} via {values[5]}"'

		mb.showinfo('Here\'s how to read your expense', message)

	def expense_to_words_before_adding(self):
		if not self.date or not self.description or not self.amnt or not self.payee or not self.method_of_payment:
			mb.showerror('Incomplete data', 'The data is incomplete, meaning fill all the fields first!')

		message = f'Your expense can be read like: \n"You paid {self.amnt.get()} to {self.payee.get()} for {self.description.get()} on {self.date.get_date()} via {self.method_of_payment.get()}"'

		add_question = mb.askyesno('Read your record like: ', f'{message}\n\nShould I add it to the database?')

		if add_question:
			self.add_another_expense()
		else:
			mb.showinfo('Ok', 'Please take your time to add this record')

def main():
	ExpenseTracker()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()