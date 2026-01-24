# Day 028
```python
# Color Hunt: Choice color
# Source: https://colorhunt.co/ ❤️❤️❤️

# Pomodoro App
# Title: Pomodora
#       Label: Work
#   Tomato Image Background (tomato.png)
#   Timer inside image: 25:00
# Button: Start             Button: Reset
#
# Work(25min) -> Break(5min) -> Work(25min) -> Break(5min) -> Work(25min) -> Break(5min) -> Work(25min) -> Break(20min)
```

# Side Quest: Canvas Widget in tkinter (similar to JS canvas): Pomodoro App
```python
# Purpose: Show importance of global variables and how Canvas has different config in tkinter
import tkinter as tk
import time

# ---------------------------- CONSTANTS ------------------------------- #
# Color Source: https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
marks = ""

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)                          # Important: stops another fx after ❤️❤️❤️
    # Reset Defaults
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    global marks                                        # check_marks.cofnig(text="")
    marks = ""
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If 8 rep
    if reps == 8:                           # if reps % 8 == 0
        count_down(long_break_sec)
        title_label.config(text="Break", foreground=RED)
    # If 2/4/6 rep                          
    if reps in [2,4,6]:                     # if reps % 2 == 0
        count_down(short_break_sec)
        title_label.config(text="Break", foreground=PINK)
    # If 1/3/5/7 rep
    if reps in [1,3,5,7]:                   # else
        count_down(work_sec)
        title_label.config(text="Work", foreground=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# def say_something(thing):
#   print(thing)

def count_down(count):
    # print(count)                                                      # Remember count decreasing until 0
    count_min = count // 60
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"                                     # Dynamic Type from int to string (only Python)

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")      # Note: Updating Canvas diff then Label

    global marks

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)                # Recursion
    else:
        start_timer()
        # marks = ""

        for _ in range(reps//2):
            marks += "✔️"
        check_marks.config(text=marks)
        
# ---------------------------- UI SETUP ------------------------------- #

if __name__ == "__main__":
    window = tk.Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

    # Label class
    title_label = tk.Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, bg=YELLOW)
    title_label.grid(row=0, column=1)

    # Canvas class
    canvas = tk.Canvas(width=200, height=224)
    tomato_img = tk.PhotoImage(file="images/tomato.png")                # Note: Need convert image to PhotoImage class
    canvas.create_image(102, 112, image=tomato_img)                     # Based on canvas size
    timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(row=1, column=1)

    # Button class: Start
    start_button = tk.Button(text="Start", highlightthickness=0, command=start_timer)
    start_button.grid(row=2, column=0)

    # Button class: Reset
    reset_button = tk.Button(text="Reset", highlightthickness=0, command=reset_timer)
    reset_button.grid(row=2, column=2)

    # Labels
    check_marks = tk.Label(foreground=GREEN, background=YELLOW)
    check_marks.grid(row=3, column=1)

    # after() waits for no clicks, waits 1 ms after first mainloop runs
    # window.after(1000, say_something, "Hello")
    # count_down(5)

    window.mainloop()
```