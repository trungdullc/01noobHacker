"""
Main Purpose:
    Create a notepad app using Menu and ScrollBar widgets from tkinter

Idea stolen from:
    https://pythongeeks.org/python-create-text-editor/

Level: Advanced
What I learned:
    tkinter.Menu()
    tkinter.ScrollBar()

Created by HackerDu

Notepad.png source: https://www.iconfinder.com/icons/285631/notepad_icon
"""

import os, sys
from tkinter import *
import tkinter.filedialog as fd
import tkinter.messagebox as mb
from PIL import Image, ImageTk

class Notepad:
    def __init__(self):
        self.root_window = Tk()
        self.root_window.title("Untitled - Notepad")
        self.root_window.geometry('800x500')
        self.root_window.resizable(0, 0)

        self.root_window.bind("<Control-a>", lambda e: self.select_all())       # Note: Put bind in __init__

        self.root_window.columnconfigure(0, weight=1)
        self.root_window.rowconfigure(0, weight=1)

        icon = ImageTk.PhotoImage(Image.open('images/Notepad.png'))                    # Icon image
        self.root_window.iconphoto(False, icon)

        self.file = ''

        # Setting the basic components of the window
        # Note: New tkinter.Menu() widget
        menu_bar = Menu(self.root_window)
        self.root_window.config(menu=menu_bar)          # Menu option

        self.text_area = Text(self.root_window, font=("Times New Roman", 12))
        self.text_area.grid(sticky=NSEW)

        scroller = Scrollbar(self.text_area, orient=VERTICAL)
        scroller.pack(side=RIGHT, fill=Y)

        scroller.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=scroller.set)

        # Adding the File Menu and its components
        file_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

        file_menu.add_command(label="New", command=self.open_new_file)
        file_menu.add_command(label="Open File", command=self.open_file)
        file_menu.add_command(label="Save As", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Close File", command=self.exit_application)

        menu_bar.add_cascade(label="File", menu=file_menu)

        # Adding the Edit Menu and its components
        edit_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

        edit_menu.add_command(label='Copy', command=self.copy_text)
        edit_menu.add_command(label='Cut', command=self.cut_text)
        edit_menu.add_command(label='Paste', command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label='Select All', command=self.select_all)
        edit_menu.add_command(label='Delete', command=self.delete_last_char)

        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        # Adding the Help Menu and its components
        help_menu = Menu(menu_bar, tearoff=False, activebackground='DodgerBlue')

        help_menu.add_command(label='About Notepad', command=self.about_notepad)
        help_menu.add_command(label='About Commands', command=self.about_commands)

        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.root_window.config(menu=menu_bar)

        # Adding a label to the bottom that counts the number of characters in the text
        # Label(root, text=f"{len(text_area.get(1.0, END))} characters", font=("Times New Roman", 12)).place(anchor=S, y=490)

        self.root_window.update()
        self.root_window.mainloop()

    def open_file(self):
        file = fd.askopenfilename(defaultextension='.txt', filetypes=[('All Files', '*.*'), ("Text File", "*.txt*")])

        if file != '':
            self.root_window.title(f"{os.path.basename(file)}")
            self.text_area.delete(1.0, END)
            with open(file, "r") as file_:
                self.text_area.insert(1.0, file_.read())
                file_.close()
        else:
            file = None

    def open_new_file(self):
        self.root_window.title("Untitled - Notepad")
        self.text_area.delete(1.0, END)

    """
    def save_file(self):
        global file
        if file == '':
            file = None
        else:
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
            file.close()

        if file is None:
            file = fd.asksaveasfilename(initialfile='Untitled.txt', defaultextension='.txt',
                                        filetypes=[("Text File", "*.txt*"), ("Word Document", '*,docx*'), ("PDF", "*.pdf*")])
        else:
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
            file.close()
            root.title(f"{os.path.basename(file)} - Notepad")
    """

    def save_file(self):
        # If no file selected yet → ask where to save
        if not file:
            file = fd.asksaveasfilename(
                initialfile='Untitled.txt',
                defaultextension='.txt',
                filetypes=[("Text File", "*.txt"), ("All Files", "*.*")]
            )

        # If user didn't cancel
        if file:
            with open(file, "w") as f:
                f.write(self.text_area.get(1.0, END))
            self.root_window.title(f"{os.path.basename(file)} - Notepad")

    def exit_application(self):
        self.root_window.destroy()

    def copy_text(self):
        self.text_area.event_generate("<<Copy>>")            # <<>> are built-in virtual events in Tkinter

    def cut_text(self):
        self.text_area.event_generate("<<Cut>>")

    def paste_text(self):
        self.text_area.event_generate("<<Paste>>")

    def select_all(self):
        # self.text_area.event_generate("<<Control-Keypress-A>>")    # event does not exist
        # self.text_area.tag_add('sel', '1.0', 'end')                # Manual tagging works but bind to Ctrl+A better
        self.text_area.tag_add("sel", "1.0", "end")
        self.text_area.mark_set("insert", "1.0")
        self.text_area.see("insert")

    def delete_last_char(self):
        # self.text_area.event_generate("<<KP_Delete>>")
        try:
            self.text_area.delete("sel.first", "sel.last")
        except:
            pass

    def about_notepad(self):
        mb.showinfo("About Notepad", "This is just another Notepad, but this is better than all others")

    def about_commands(self):
        commands = """
    Under the File Menu:
    - 'New' clears the entire Text Area
    - 'Open' clears text and opens another file
    - 'Save' saves your current file 
    - 'Save As' saves your file in another extension

    Under the Edit Menu:
    - 'Copy' copies the selected text to your clipboard
    - 'Cut' cuts the selected text and removes it from the text area 
    - 'Paste' pastes the copied/cut text
    - 'Select All' selects the entire text
    - 'Delete' deletes the last character  
    """

        mb.showinfo(title="All commands", message=commands)

def main():
    Notepad()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()