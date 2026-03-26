"""
Main Purpose:
	Learn sqlite3 with tkinter to create Library System
    library.db
    Difference between tkinter.messagebox and tkinter.simpledialog

Idea stolen from:
	https://pythongeeks.org/python-library-management-system-project/

Level: Advanced
What I learned:
    import sqlite3
    place instead of grid or pack

Created by HackerDu
"""

import sys
import sqlite3

from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb             # Note: Display and Buttons
import tkinter.simpledialog as sd           # Note: Get an input such as library card number

class Library:
    def __init__(self):
        self.data_base_connection()         # Note: Remember this for future good way to connect style

        # Variables
        lf_bg = 'LightSkyBlue'                  # Left Frame Background Color
        rtf_bg = 'DeepSkyBlue'                  # Right Top Frame Background Color
        rbf_bg = 'DodgerBlue'                   # Right Bottom Frame Background Color
        self.btn_hlb_bg = 'SteelBlue'           # Background color for Head Labels and Buttons

        lbl_font = ('Georgia', 13)              # Font for all labels
        entry_font = ('Times New Roman', 12)    # Font for all Entry widgets
        self.btn_font = ('Gill Sans MT', 13)

        # Initializing the main GUI window
        self.root_window = Tk()
        self.root_window.title('Library Management System')
        self.root_window.geometry('1010x530')
        self.root_window.resizable(0, 0)

        Label(self.root_window, text='LIBRARY MANAGEMENT SYSTEM', font=("Noto Sans CJK TC", 15, 'bold'), bg=self.btn_hlb_bg, fg='White').pack(side=TOP, fill=X)

        self.bk_status = StringVar()
        self.bk_name = StringVar()
        self.bk_id = StringVar()
        self.author_name = StringVar()
        self.card_id = StringVar()

        # Frames
        self.left_frame = Frame(self.root_window, bg=lf_bg)
        self.left_frame.place(x=0, y=30, relwidth=0.3, relheight=0.96)

        RT_frame = Frame(self.root_window, bg=rtf_bg)
        RT_frame.place(relx=0.3, y=30, relheight=0.2, relwidth=0.7)

        RB_frame = Frame(self.root_window)
        RB_frame.place(relx=0.3, rely=0.24, relheight=0.785, relwidth=0.7)

        # Left Frame
        Label(self.left_frame, text='Book Name', bg=lf_bg, font=lbl_font).place(x=98, y=25)
        Entry(self.left_frame, width=25, font=entry_font, text=self.bk_name).place(x=45, y=55)

        Label(self.left_frame, text='Book ID', bg=lf_bg, font=lbl_font).place(x=110, y=105)
        self.bk_id_entry = Entry(self.left_frame, width=25, font=entry_font, text=self.bk_id)
        self.bk_id_entry.place(x=45, y=135)

        Label(self.left_frame, text='Author Name', bg=lf_bg, font=lbl_font).place(x=90, y=185)
        Entry(self.left_frame, width=25, font=entry_font, text=self.author_name).place(x=45, y=215)

        Label(self.left_frame, text='Status of the Book', bg=lf_bg, font=lbl_font).place(x=75, y=265)
        dd = OptionMenu(self.left_frame, self.bk_status, *['Available', 'Issued'])
        dd.configure(font=entry_font, width=12)
        dd.place(x=75, y=300)

        submit = Button(self.left_frame, text='Add new record', font=self.btn_font, bg=self.btn_hlb_bg, width=20, command=self.add_record)
        submit.place(x=50, y=375)

        self.clear = Button(self.left_frame, text='Clear fields', font=self.btn_font, bg=self.btn_hlb_bg, width=20, command=self.clear_fields)
        self.clear.place(x=50, y=435)

        # Right Top Frame
        Button(RT_frame, text='Delete book record', font=self.btn_font, bg=self.btn_hlb_bg, width=17, command=self.remove_record).place(x=8, y=30)
        Button(RT_frame, text='Delete full inventory', font=self.btn_font, bg=self.btn_hlb_bg, width=17, command=self.delete_inventory).place(x=178, y=30)
        Button(RT_frame, text='Update book details', font=self.btn_font, bg=self.btn_hlb_bg, width=17, command=self.update_record).place(x=348, y=30)
        Button(RT_frame, text='Change Book Availability', font=self.btn_font, bg=self.btn_hlb_bg, width=19, command=self.change_availability).place(x=518, y=30)

        # Right Bottom Frame
        Label(RB_frame, text='BOOK INVENTORY', bg=rbf_bg, font=("Noto Sans CJK TC", 15, 'bold')).pack(side=TOP, fill=X)

        self.tree = ttk.Treeview(RB_frame, selectmode=BROWSE, columns=('Book Name', 'Book ID', 'Author', 'Status', 'Issuer Card ID'))

        XScrollbar = Scrollbar(self.tree, orient=HORIZONTAL, command=self.tree.xview)
        YScrollbar = Scrollbar(self.tree, orient=VERTICAL, command=self.tree.yview)
        XScrollbar.pack(side=BOTTOM, fill=X)
        YScrollbar.pack(side=RIGHT, fill=Y)

        self.tree.config(xscrollcommand=XScrollbar.set, yscrollcommand=YScrollbar.set)

        self.tree.heading('Book Name', text='Book Name', anchor=CENTER)
        self.tree.heading('Book ID', text='Book ID', anchor=CENTER)
        self.tree.heading('Author', text='Author', anchor=CENTER)
        self.tree.heading('Status', text='Status of the Book', anchor=CENTER)
        self.tree.heading('Issuer Card ID', text='Card ID of the Issuer', anchor=CENTER)

        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('#1', width=225, stretch=NO)
        self.tree.column('#2', width=70, stretch=NO)
        self.tree.column('#3', width=150, stretch=NO)
        self.tree.column('#4', width=105, stretch=NO)
        self.tree.column('#5', width=132, stretch=NO)

        self.tree.place(y=30, x=0, relheight=0.9, relwidth=1)

        self.clear_and_display()

        self.root_window.update()
        self.root_window.mainloop()

    def data_base_connection(self):
        # Connecting to sqlite3 offline Database
        self.connector = sqlite3.connect('data/library.db')           # Important: Where database is stored in same location
        self.cursor = self.connector.cursor()

        # Creates a table if not exists
        self.connector.execute('CREATE TABLE IF NOT EXISTS Library (BK_NAME TEXT, BK_ID TEXT PRIMARY KEY NOT NULL, AUTHOR_NAME TEXT, BK_STATUS TEXT, CARD_ID TEXT)')

    def issuer_card(self):
        Cid = sd.askstring('Issuer Card ID', 'What is the Issuer\'s Card ID?\t\t\t')

        if not Cid:
            mb.showerror('Issuer ID cannot be zero!', 'Can\'t keep Issuer ID empty, it must have a value')
        else:
            return Cid

    def display_records(self):
        self.tree.delete(*self.tree.get_children())

        curr = self.connector.execute('SELECT * FROM Library')
        data = curr.fetchall()

        for records in data:
            self.tree.insert('', END, values=records)

    def clear_fields(self):
        self.bk_status.set('Available')

        for i in ['self.bk_id', 'self.bk_name', 'self.author_name', 'self.card_id']:
            exec(f"{i}.set('')")
            self.bk_id_entry.config(state='normal')
        try:
            self.tree.selection_remove(self.tree.selection()[0])
        except:
            pass

    def clear_and_display(self):
        self.clear_fields()
        self.display_records()

    def add_record(self):
        if self.bk_status.get() == 'Issued':
            self.card_id.set(self.issuer_card())
        else:
            self.card_id.set('N/A')

        surety = mb.askyesno('Are you sure?',
                    'Are you sure this is the data you want to enter?\nPlease note that Book ID cannot be changed in the future')

        if surety:
            try:
                self.connector.execute(
                'INSERT INTO Library (BK_NAME, BK_ID, AUTHOR_NAME, BK_STATUS, CARD_ID) VALUES (?, ?, ?, ?, ?)',
                    (self.bk_name.get(), self.bk_id.get(), self.author_name.get(), self.bk_status.get(), self.card_id.get()))
                self.connector.commit()

                self.clear_and_display()

                mb.showinfo('Record added', 'The new record was successfully added to your database')
            except sqlite3.IntegrityError:
                mb.showerror('Book ID already in use!',
                            'The Book ID you are trying to enter is already in the database, please alter that book\'s record or check any discrepancies on your side')

    def view_record(self):
        if not self.tree.focus():
            mb.showerror('Select a row!', 'To view a record, you must select it in the table. Please do so before continuing.')
            return

        current_item_selected = self.tree.focus()
        values_in_selected_item = self.tree.item(current_item_selected)
        selection = values_in_selected_item['values']

        self.bk_name.set(selection[0])
        self.bk_id.set(selection[1])
        self.bk_status.set(selection[3])
        self.author_name.set(selection[2])

        try:
            self.card_id.set(selection[4])
        except:
            self.card_id.set('')

    def update_record(self):
        """
        Note: Nested method if wanted to split must create 2 methods
        """
        def update():
            if self.bk_status.get() == 'Issued':
                self.card_id.set(self.issuer_card())
            else:
                self.card_id.set('N/A')

            self.cursor.execute('UPDATE Library SET BK_NAME=?, BK_STATUS=?, AUTHOR_NAME=?, CARD_ID=? WHERE BK_ID=?',
                        (self.bk_name.get(), self.bk_status.get(), self.author_name.get(), self.card_id.get(), self.bk_id.get()))
            self.connector.commit()
            
            self.clear_and_display()

            edit.destroy()
            self.bk_id_entry.config(state='normal')
            self.clear.config(state='normal')

        self.view_record()

        self.bk_id_entry.config(state='disable')
        self.clear.config(state='disable')

        edit = Button(self.left_frame, text='Update Record', font=self.btn_font, bg=self.btn_hlb_bg, width=20, command=update)
        edit.place(x=50, y=375)

    def remove_record(self):
        if not self.tree.selection():
            mb.showerror('Error!', 'Please select an item from the database')
            return

        current_item = self.tree.focus()
        values = self.tree.item(current_item)
        selection = values["values"]

        self.cursor.execute('DELETE FROM Library WHERE BK_ID=?', (selection[1], ))
        self.connector.commit()

        self.tree.delete(current_item)

        mb.showinfo('Done', 'The record you wanted deleted was successfully deleted.')

        self.clear_and_display()

    def delete_inventory(self):
        if mb.askyesno('Are you sure?', 'Are you sure you want to delete the entire inventory?\n\nThis command cannot be reversed'):
            self.tree.delete(*self.tree.get_children())

            self.cursor.execute('DELETE FROM Library')
            self.connector.commit()
        else:
            return

    def change_availability(self):
        if not self.tree.selection():
            mb.showerror('Error!', 'Please select a book from the database')
            return

        current_item = self.tree.focus()
        values = self.tree.item(current_item)
        BK_id = values['values'][1]
        BK_status = values["values"][3]

        if BK_status == 'Issued':
            surety = mb.askyesno('Is return confirmed?', 'Has the book been returned to you?')
            if surety:
                self.cursor.execute('UPDATE Library SET bk_status=?, card_id=? WHERE bk_id=?', ('Available', 'N/A', BK_id))
                self.connector.commit()
            else: mb.showinfo(
                'Cannot be returned', 'The book status cannot be set to Available unless it has been returned')
        else:
            self.cursor.execute('UPDATE Library SET bk_status=?, card_id=? where bk_id=?', ('Issued', self.issuer_card(), BK_id))
            self.connector.commit()

        self.clear_and_display()

def main():
    Library()

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		sys.exit()