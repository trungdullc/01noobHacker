# Day 031
```python
# Flash Card App called Flashy
# BACKGROUND_COLOR = "#B1DDC6"
#   Spanish                         English
#   beber    Wait 3 sec)-->         to drink
#                           Button: Red X      Green ✔️    Foreground: White

# Select a frequency list language
# Source: https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists
# Paste it in A column

# Important: Excel cheat to translate Langunage ❤️❤️❤️
# Documentation: https://support.google.com/docs/answer/3093331?hl=en
# If incorrectly translated go directly into cell and change
    A           B
1   French      English
2   partie      =GOOGLETRANSLATE(A2, "fr", "en")
3   histoire    Drag bottom right corner all way down
# Download as csv
```

# Side Quest: Flash Card App
```python
# Learn canvas uses itemconfig and fill vs Label config and foreground
import tkinter as tk
import random
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
to_learn = []
current_card = {}

def manipulate_csv():
    try:
        words_DF = pandas.read_csv("data/words_to_learn.csv")
    except FileNotFoundError:
        words_DF = pandas.read_csv("data/french_words.csv")
    finally:
        words_dict = words_DF.to_dict()
        # print(words_dict)
        """ Seperated by column
        {
            'French': {0: 'partie', 1: 'histoire', 2: 'chercher', 3: 'seulement', 4: 'police', 5: 'pensais', 6: 'aide', 7: 'demande', 8: 'genre', 9: 'mois', 10: 'frère', 11: 'laisser', 12: 'car', 13: 'mettre', 14: 'aucun', 15: 'laisse', 16: 'eux', 17: 'ville', 18: 'chaque', 19: 'parlé', 20: 'arrivé', 21: 'devrait', 22: 'bébé', 23: 'longtemps', 24: 'heures', 25: 'vont', 26: 'pendant', 27: 'revoir', 28: 'aucune', 29: 
                'place', 30: 'parle', 31: 'compris', 32: 'savais', 33: 'étaient', 34: 'attention', 35: 'voici', 36: 'pourrais', 37: 'affaire', 38: 'donner', 39: 'type', 40: 'leurs', 41: 'donné', 42: 'train', 43: 'corps', 44: 'endroit', 45: 'yeux', 46: 'façon', 47: 'écoute', 48: 'dont', 49: 'trouve', 50: 'premier', 51: 'perdu', 52: 'main', 53: 'première', 54: 'côté', 55: 'pouvoir', 56: 'vieux', 57: 'sois', 58: 'tiens', 59: 'matin', 60: 'tellement', 61: 'enfant', 62: 'point', 63: 'venu', 64: 'suite', 65: 'pardon', 66: 'venez', 67: 'devant', 68: 'vers', 69: 'minutes', 70: 'demandé', 71: 'chambre', 72: 'mis', 73: 'belle', 74: 'droit', 75: 'aimerais', 76: "aujourd'hui", 77: 'mari', 78: 'cause', 79: 'enfin', 80: 'espère', 81: 'eau', 82: 'attendez', 83: 'parti', 84: 'nouvelle', 85: 'boulot', 86: 'arrêter', 87: 'dirait', 88: 'terre', 89: 'compte', 90: 'donne', 91: 'loin', 92: 'fin', 93: 'croire', 94: 'chérie', 95: 'gros', 96: 'plutôt', 97: 'aura', 98: 'filles', 
                99: 'jouer', 100: 'bureau'}, 
            'English': {0: 'part', 1: 'history', 2: 'search', 3: 'only', 4: 'police', 5: 'thought', 6: 'help', 7: 'request', 8: 'kind', 9: 'month', 10: 'brother', 11: 'let', 12: 'because', 13: 'to put', 14: 'no', 15: 'leash', 16: 'them', 17: 'city', 18: 'each', 19: 'speak', 20: 'come', 21: 'should', 22: 'baby', 23: 'long time', 24: 'hours', 25: 'will', 26: 'while', 27: 'meet again', 28: 'any', 29: 'square', 30: 'speak', 31: 'understood', 32: 'knew', 33: 'were', 34: 'Warning', 35: 'here is', 36: 'could', 37: 'case', 38: 'give', 39: 'type', 40: 'their', 41: 'given', 42: 'train', 43: 'body', 44: 'place', 45: 'eyes', 46: 'way', 47: 'listen', 48: 'whose', 49: 
                'find', 50: 'first', 51: 'lost', 52: 'hand', 53: 'first', 54: 'side', 55: 'power', 56: 'old', 57: 'be', 58: 'here', 59: 'morning', 60: 'so much', 61: 'child', 62: 'point', 63: 'came', 64: 'after', 65: 'sorry', 66: 'come', 67: 'in front of', 68: 'towards', 69: 'minutes', 70: 'request', 71: 'bedroom', 72: 'placed', 73: 'beautiful', 74: 'law', 75: 'would like to', 76: 'today', 77: 'husband', 78: 'cause', 79: 'finally', 80: 'hope', 81: 'water', 82: 'Wait', 83: 'left', 84: 'new', 85: 'job', 86: 'Stop', 87: 'would say', 88: 'Earth', 89: 'account', 90: 'given', 91: 'far', 92: 'end', 93: 'believe', 94: 'sweetheart', 95: 'large', 96: 'rather', 97: 'will have', 98: 'girls', 99: 'to play', 100: 'office'}
        }
        """
        # print(words_dict.keys())          # dict_keys(['French', 'English'])

        # Override words_dict since we want a list of dict to work with
        words_list = words_DF.to_dict(orient="records")
        # print(words_list)
        """
        [
            {'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}, {'French': 'chercher', 'English': 'search'}, {'French': 'seulement', 'English': 'only'}, {'French': 'police', 'English': 'police'}, {'French': 'pensais', 'English': 'thought'}, {'French': 'aide', 'English': 'help'}, {'French': 'demande', 'English': 'request'}, {'French': 'genre', 'English': 'kind'}, {'French': 'mois', 
            'English': 'month'}, {'French': 'frère', 'English': 'brother'}, {'French': 'laisser', 'English': 'let'}, {'French': 'car', 'English': 'because'}, {'French': 'mettre', 'English': 'to put'}, {'French': 'aucun', 'English': 'no'}, {'French': 'laisse', 'English': 'leash'}, {'French': 'eux', 'English': 'them'}, {'French': 'ville', 'English': 'city'}, {'French': 'chaque', 'English': 'each'}, {'French': 'parlé', 
            'English': 'speak'}, {'French': 'arrivé', 'English': 'come'}, {'French': 'devrait', 'English': 'should'}, {'French': 'bébé', 'English': 
            'baby'}, {'French': 'longtemps', 'English': 'long time'}, {'French': 'heures', 'English': 'hours'}, {'French': 'vont', 'English': 'will'}, {'French': 'pendant', 'English': 'while'}, {'French': 'revoir', 'English': 'meet again'}, {'French': 'aucune', 'English': 'any'}, {'French': 'place', 'English': 'square'}, {'French': 'parle', 'English': 'speak'}, {'French': 'compris', 'English': 'understood'}, {'French': 'savais', 'English': 'knew'}, {'French': 'étaient', 'English': 'were'}, {'French': 'attention', 'English': 'Warning'}, {'French': 'voici', 'English': 'here is'}, {'French': 'pourrais', 'English': 'could'}, {'French': 'affaire', 'English': 'case'}, {'French': 'donner', 
            'English': 'give'}, {'French': 'type', 'English': 'type'}, {'French': 'leurs', 'English': 'their'}, {'French': 'donné', 'English': 'given'}, {'French': 'train', 'English': 'train'}, {'French': 'corps', 'English': 'body'}, {'French': 'endroit', 'English': 'place'}, {'French': 'yeux', 'English': 'eyes'}, {'French': 'façon', 'English': 'way'}, {'French': 'écoute', 'English': 'listen'}, {'French': 'dont', 'English': 'whose'}, {'French': 'trouve', 'English': 'find'}, {'French': 'premier', 'English': 'first'}, {'French': 'perdu', 'English': 'lost'}, {'French': 'main', 'English': 'hand'}, {'French': 'première', 'English': 'first'}, {'French': 'côté', 'English': 'side'}, {'French': 'pouvoir', 'English': 'power'}, {'French': 'vieux', 'English': 'old'}, {'French': 'sois', 'English': 'be'}, {'French': 'tiens', 'English': 'here'}, {'French': 'matin', 'English': 'morning'}, {'French': 'tellement', 'English': 'so much'}, {'French': 'enfant', 'English': 'child'}, {'French': 'point', 'English': 'point'}, {'French': 'venu', 'English': 'came'}, {'French': 'suite', 'English': 'after'}, {'French': 'pardon', 'English': 'sorry'}, {'French': 'venez', 'English': 'come'}, {'French': 'devant', 'English': 'in front of'}, {'French': 'vers', 'English': 'towards'}, {'French': 'minutes', 'English': 'minutes'}, {'French': 'demandé', 'English': 'request'}, {'French': 'chambre', 'English': 'bedroom'}, {'French': 'mis', 'English': 'placed'}, {'French': 'belle', 'English': 'beautiful'}, {'French': 'droit', 
            'English': 'law'}, {'French': 'aimerais', 'English': 'would like to'}, {'French': "aujourd'hui", 'English': 'today'}, {'French': 'mari', 'English': 'husband'}, {'French': 'cause', 'English': 'cause'}, {'French': 'enfin', 'English': 'finally'}, {'French': 'espère', 'English': 'hope'}, {'French': 'eau', 'English': 'water'}, {'French': 'attendez', 'English': 'Wait'}, {'French': 'parti', 'English': 'left'}, {'French': 'nouvelle', 'English': 'new'}, {'French': 'boulot', 'English': 'job'}, {'French': 'arrêter', 'English': 'Stop'}, {'French': 'dirait', 'English': 'would say'}, {'French': 'terre', 'English': 'Earth'}, {'French': 'compte', 'English': 'account'}, {'French': 'donne', 'English': 'given'}, {'French': 'loin', 'English': 'far'}, {'French': 'fin', 'English': 'end'}, {'French': 'croire', 'English': 'believe'}, {'French': 'chérie', 'English': 'sweetheart'}, {'French': 'gros', 'English': 'large'}, {'French': 'plutôt', 'English': 'rather'}, 
            {'French': 'aura', 'English': 'will have'}, {'French': 'filles', 'English': 'girls'}, {'French': 'jouer', 'English': 'to play'}, {'French': 'bureau', 'English': 'office'}
        ]
        """
        # like a dictionary record style I not seend before
        # print(words_list[0]["French"])
        # print(words_list[0]["English"])

    global to_learn
    to_learn = words_list

def next_card():
    '''
    Configures card and flips card
    '''
    global current_card, flip_timer
    window.after_cancel(flip_timer)                 # Fix person click on button many times cancels current timer

    current_card = random.choice(to_learn)
    # print(current_card["French"])
    # print(current_card["English"])
    canvas.itemconfigure(card_title, text="French", fill="black")               # canvas item manipulate differently than labels
    canvas.itemconfigure(card_word, text=current_card["French"], fill="black")

    # Flip card while changing color and image
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)     # Reset timer

def flip_card():
    """
    Flips card to english dict and changes canvas item using itemconfig
    """
    canvas.itemconfig(card_background, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")                 # Not foreground
    canvas.itemconfigure(card_word, text=current_card["English"], fill="white")

def is_known():
    """
    Remove current card since you know it
    """
    to_learn.remove(current_card)
    print(f"DEBUG: {len(to_learn)}")

    data_DF = pandas.DataFrame(to_learn)
    data_DF.to_csv("data/words_to_learn.csv", index=False)              # Remove index added to csv
    next_card()

if __name__ == "__main__":
    # TODO 2: Maniuplate the csv -> panda Data Frame -> list[dict[str, str]]
    manipulate_csv()

    # TODO 1: Build User Interface
    window = tk.Tk()
    window.title("Flashy")
    window.configure(background=BACKGROUND_COLOR, padx=50, pady=50)

    # Canvas: to be able to draw or write
    canvas = tk.Canvas(height=526, width=800)
    card_front_img = tk.PhotoImage(file="images/card_front.png")            # Note: Don't create inside fx or deleted after
    card_back_img = tk.PhotoImage(file="images/card_back.png")
    card_background = canvas.create_image(400, 263, image=card_front_img)   # Becareful order of 400, 263 can't use keyword
    canvas.grid(row=0, column=0, columnspan=2)
    canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)    # Get rid of border

    card_title = canvas.create_text(400, 150, text="PLACEHOLDER", font=("Ariel", 40, "italic"))
    card_word = canvas.create_text(400, 263, text="PLACEHOLDER", font=("Ariel", 60, "bold"))

    # Buttons    
    correct_image = tk.PhotoImage(file="images/right.png")
    correct_button = tk.Button(image=correct_image, highlightthickness=0, command=is_known)
    correct_button.grid(row=1, column=1)

    wrong_img = tk.PhotoImage(file="images/wrong.png")
    wrong_button = tk.Button(image=wrong_img, highlightthickness=0, command=next_card)
    wrong_button.grid(row=1, column=0)

    flip_timer = window.after(3000, func=flip_card)     # Since sleep in python need be clicked on to activate
    next_card()                                         # Remove PLACEHOLDER with next_card() fx

    window.mainloop()
```