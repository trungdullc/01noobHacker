# Day 029
```python
# Password Manager
#                   LOGO: logo.png
# Website:          []
# Email/Username:   [example@email.com]     Button: Generate Password  ---> saved to clipboard
#                   Button: Add             ----------------------------> data.txt

# data.txt
Amazon | example@yahoo.com | lsfjdkladlfksdj
```

# Side Quest: columnspan
```python
import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()

    r = tk.Label(bg="red", width=20, height=5)
    r.grid(row=0, column=0)

    g = tk.Label(bg="green", width=20, height=5)
    g.grid(row=1, column=1)

    b = tk.Label(bg="blue", width=40, height=5)         # Note: Had to increase width as well
    b.grid(row=2, column=0, columnspan=2)               # columnspan attribute
    b.config(highlightthickness=0)

    window.mainloop()
```

# Side Quest: Password Manager
```python
import tkinter as tk
import tkinter.messagebox               # Go to Definition
import random
import pyperclip                        # pip3 install pyperclip

LOGO_SOURCE="images/logo.png"
FONT_STYLE="Courier"

# ---------------------------- TODO 3: PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project from Day 5

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # password_list = []
    
    # for _ in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for _ in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for _ in range(nr_numbers):
    #     password_list += random.choice(numbers)

    # Shortened with list comprehension
    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    # Shorten w/ join() from a dict, list, tuple to a str
    password = "".join(password_list)
    
    print(f"DEBUG: Your password is: {password}")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, f"{password}")

    # Optional: Copy password into clipboard w/ import pyperclip
    pyperclip.copy(password)

# ---------------------------- TODO 2: SAVE PASSWORD ------------------------------- #
def save():
    # Validation: Check if empty fields and output warning
    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        tkinter.messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = tkinter.messagebox.askokcancel(title=website_entry.get(), message=f"Email: {email_entry.get()}\nPassword: {password_entry.get()}\nIs it ok to save?")           # messagebox.py is module

        if is_ok:
            # print(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}")
            with open("data/data_password.txt", mode="a") as file:
                file.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
            print("DEBUG: Successfully added entry")

            # delete entry from website and password fields only
            website_entry.delete(0, tk.END)
            password_entry.delete(0, tk.END)

            # refocus
            website_entry.focus()
        else:
            pass

# ---------------------------- TODO 1: UI SETUP ------------------------------- #
if __name__ == "__main__":
    window = tk.Tk()
    window.title("Password Manager")
    window.configure(padx=50, pady=50)

    canvas = tk.Canvas(width=200, height=200)
    logo_img = tk.PhotoImage(file=LOGO_SOURCE)
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    # Labels
    website_label = tk.Label(text="Website:")
    website_label.grid(row=1, column=0)
    website_label.config(font=(FONT_STYLE, 16))
    email_username_label = tk.Label(text="Email/Username:")
    email_username_label.grid(row=2, column=0)
    email_username_label.config(font=(FONT_STYLE, 16))
    password_label = tk.Label(text="Password:")
    password_label.grid(row=3, column=0)
    password_label.config(font=(FONT_STYLE, 16))

    # Entry
    website_entry = tk.Entry(width=35)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()                                   # Place cursor so can work right away
    email_entry = tk.Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.insert(0, "example@gmail.com")              # 0 front, END at end
    password_entry = tk.Entry(width=21)
    password_entry.grid(row=3, column=1)

    # Buttons
    password_button = tk.Button(text="Generate Password", command=password_generator)
    password_button.grid(row=3, column=2)
    add_button = tk.Button(text="Add", width=36, command=save)
    add_button.grid(row=4, column=1, columnspan=2)
    
    window.mainloop()
```