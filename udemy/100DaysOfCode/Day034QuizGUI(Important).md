# Day 034
```python
# Source: https://opentdb.com/api_config.php
# Generate API URL
    https://opentdb.com/api.php?amount=10&category=18&type=boolean
# End Point
    https://opentdb.com/api.php
# Parameters
{
    amount=10,
    category=18,
    type=boolean
}
```

# Side Quest: HTML Character Entities
```python
# HTML Enties are replaced so not confused with html code
<       &#60       &lt

# Google: How to unescape HTML character entities in python
import html
my_string = "In &quot;Mario Kart64&quot;, Walugigi is a playable character"
print(html.unescape(my_string))
```

# Side Quest: Quizzler App not using question_data (hardcoded dict) and fixing HTML Char Entities
```python
import requests
import html                                 # unescape HTML character Entities

THEME_COLOR = "#375362"

parameters = {
    "amount":10, 
    "category":18, 
    "type":"boolean"
}

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower()[0] == correct_answer.lower()[0]:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

question_bank = []

if __name__ == "__main__":
    # question_data not hardcoded from data.py anymore
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    data = response.json()
    # print(data)

    question_data = data["results"]

    for question in question_data:
        question_text = html.unescape(question["question"])         # Unescape HTML char entities using import html
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
```

# Side Quest: Quizzler App from above convert CLI to GUI with tkinter
```python
import requests
import html                                 # unescape HTML character Entities
import tkinter

THEME_COLOR = "#375362"

parameters = {
    "amount":10, 
    "category":18, 
    "type":"boolean"
}

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # user_answer = input(f"Q.{self.question_number}: {self.current_question.text} (True/False): ")
        # self.check_answer(user_answer)
        return f"Q.{self.question_number}: {self.current_question.text}"
    
    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower()[0] == correct_answer.lower()[0]:
            self.score += 1
            print("You got it right!")
            return True                                             # New
        else:
            print("That's wrong.")
            return False

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

class QuizInterface:                                                # New ❤️❤️❤️❤️❤️❤️❤️❤️❤️❤️
    def __init__(self, quiz_brain: QuizBrain):
        self.window = tkinter.Tk()                                  # Remember: use self w/ classes
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Label Property
        self.score_label = tkinter.Label(text="Score: 0", background=THEME_COLOR, foreground="white")
        self.score_label.grid(row=0, column=1)

        # Canvas Property
        # Note: Width on create_text text wraps it must be smaller than width of canvas ❤️❤️❤️❤️❤️
        self.canvas = tkinter.Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, text="Amazing", fill=THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=1,column=0, columnspan=2, pady=50)

        # Button Property
        true_image = tkinter.PhotoImage(file="images/right.png")
        false_image = tkinter.PhotoImage(file="images/wrong.png")
        self.true_button = tkinter.Button(image=true_image, background=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.false_button = tkinter.Button(image=false_image, background=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.quiz = quiz_brain

        self.get_next_question()                    # Remove placeholder text
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(background="white")                   # RESET canvas bg

        if self.quiz.still_has_questions():                             # Important
            self.score_label.config(text=f"Score: {self.quiz.score}")   # Important
            question_text = self.quiz.next_question()
            self.canvas.itemconfigure(self.question_text, text=question_text)
        else:
            self.canvas.itemconfigure(self.question_text, text="Game Over")
            self.true_button.config(state="disabled")                   # Important: disable buttons
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True")) 

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))
    
    def give_feedback(self, is_right):
        if is_right:
            # Turn canvas bg green
            self.canvas.configure(background="green")
        else:
            # Turn canvas bg red
            self.canvas.configure(background="red")
        # RESET canvas bg color
        self.window.after(1000, self.get_next_question)

question_bank = []

if __name__ == "__main__":
    response = requests.get(url="https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()

    data = response.json()

    question_data = data["results"]

    for question in question_data:
        question_text = html.unescape(question["question"])
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)                   # New ❤️❤️❤️❤️❤️

    # while quiz.still_has_questions():
    #     quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score was: {quiz.score}/{quiz.question_number}")
```