"""
Main Purpose:
   Learn about Frame widget and Scrollbar and ListBox

Idea stolen from:
   https://pythongeeks.org/python-contact-address-book-project/

Level: Intermediate
What I learned:
   Create Frame widget inside root_window
      Scrollbar inside Frame()
      ListBox inside Frame()
      If i need to create a Scrollbar Object in tkinter just copy the code ❤️

Created by HackerDu
"""

import sys
from tkinter import *
from tkinter import messagebox

contactlist: list[list[str,str]] = [
   ['Siddharth Nigam','369854712'],
   ['Gaurav Patil', '521155222'],
   ['Abhishek Nikam', '78945614'],
   ['Sakshi Gaikwad', '58745246'],
   ['Mohit Paul', '5846975'],
   ['Karan Patel', '5647892'],
   ['Sam Sharma', '89685320'],
   ['John Maheshwari', '98564785'],
   ['Ganesh Pawar','85967412']
]

class Book:
   def selected(self):
      """
      Get selected value
      """

      print(f"DEBUG: 0 means not selected {len(select.curselection())}")

      if len(select.curselection())==0:
         messagebox.showerror("Error", "Please Select the Name")
      else:
         return int(select.curselection()[0])

   def add_contact(self):
      """
      Add new contact
      """

      # Makes sure entry fields not empty with and logic
      if Name.get()!="" and Number.get()!="":
         contactlist.append([Name.get() ,Number.get()])
         # print(f"DEBUG: {contactlist}")

         self.display_contacts()
         self.reset_contact_fields()
         messagebox.showinfo("Confirmation", "Successfully Add New Contact")
      else:
         messagebox.showerror("Error","Please fill the information")

   def update_contact(self):
      """
      Edit existing contacts
      """

      if Name.get() and Number.get():
         contactlist[self.selected()] = [Name.get(), Number.get()]
         messagebox.showinfo("Confirmation", "Successfully Update Contact")
         self.reset_contact_fields()
         self.display_contacts()
      elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
         messagebox.showerror("Error", "Please fill the information")
      else:
         if len(select.curselection())==0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
         else:
            message1 = """To Load the all information of \nselected row press Load button\n."""   
            messagebox.showerror("Error", message1)

   def reset_contact_fields(self):
      """
      Reset entries
      """
      Name.set('')
      Number.set('')

   def delete_contact(self):
      """
      Delete selected contact
      """
      if len(select.curselection())!=0:
         result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
         
         if result==True:
            del contactlist[self.selected()]
            self.display_contacts()
      else:
         messagebox.showerror("Error", 'Please select the Contact')
      
   def view(self):
      """
      View contact
      """
      NAME, PHONE = contactlist[self.selected()]
      Name.set(NAME)
      Number.set(PHONE)
         
   def exit(self):
      """
      Exit game window
      """
      root_window.destroy()

   def display_contacts(self) :
      contactlist.sort()                  # sort global contactlist
      select.delete(0,END)                # clear select

      for name,phone in contactlist:
         select.insert(END, name)         # add sorted contactlist to select

def main():
   global select, Name, Number, root_window

   book = Book()
   
   root_window = Tk()
   root_window.geometry('700x550')
   root_window.config(bg = '#d3f3f5')
   root_window.title('Contact Book')
   root_window.resizable(height=0,width=0)

   Name = StringVar()
   Number = StringVar()

   # Create Frame widget inside root_window
   frame_window = Frame(root_window)                # ❤️❤️❤️❤️❤️
   frame_window.pack(side = RIGHT)

   # Just copy this aint no way I remembering this
   scroll = Scrollbar(master=frame_window, orient=VERTICAL)
   select = Listbox(master=frame_window, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=20,height=20,borderwidth=3,relief="groove")
   scroll.config (command=select.yview)
   scroll.pack(side=RIGHT, fill=Y)
   select.pack(side=LEFT,  fill=BOTH, expand=1)

   Label(root_window, text = 'Name', font=("Times new roman",25,"bold"), bg = 'SlateGray3').place(x= 30, y=20)
   Entry(root_window, textvariable = Name, width=30).place(x= 200, y=30)

   Label(root_window, text = 'Contact No.', font=("Times new roman",22,"bold"),bg = 'SlateGray3').place(x= 30, y=70)
   Entry(root_window, textvariable = Number, width=30).place(x= 200, y=80)

   Button(root_window,text="ADD", font='Helvetica 18 bold',bg='#e8c1c7', command = book.add_contact, padx=20). place(x= 50, y=140)
   Button(root_window,text="EDIT", font='Helvetica 18 bold',bg='#e8c1c7',command = book.update_contact, padx=20).place(x= 50, y=200)
   Button(root_window,text="DELETE", font='Helvetica 18 bold',bg='#e8c1c7',command = book.delete_contact, padx=20).place(x= 50, y=260)
   Button(root_window,text="VIEW", font='Helvetica 18 bold',bg='#e8c1c7', command = book.view).place(x= 50, y=325)
   Button(root_window,text="RESET", font='Helvetica 18 bold',bg='#e8c1c7', command = book.reset_contact_fields).place(x= 50, y=390)
   Button(root_window,text="EXIT", font='Helvetica 24 bold',bg='tomato', command = book.exit).place(x= 250, y=470)

   book.display_contacts()

   root_window.mainloop()

if __name__ == "__main__":
   try:
      main()
   except KeyboardInterrupt:
      sys.exit()