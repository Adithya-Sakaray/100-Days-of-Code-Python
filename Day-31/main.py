import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# fetching data

data = pandas.read_csv(filepath_or_buffer="data/french_words.csv")
answered = []
data_dict = pandas.DataFrame.to_dict(data, orient="records")
print(len(data_dict))
rand_num = random.randint(0, 101)


def generate_random():
    global rand_num
    rand_num = random.randint(1, 101)
    if rand_num in answered:
        generate_random()
    return rand_num


def new_card():
    global rand_num, flip_timer
    rand_num = generate_random()
    window.after_cancel(flip_timer)
    card_french = data_dict[rand_num]["French"]
    canvas.itemconfig(card_image, image=card_back)
    canvas.itemconfig(body, text=card_french)
    canvas.itemconfig(title, text="French")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_english = data_dict[rand_num]["English"]
    canvas.itemconfig(card_image, image=card_front)
    canvas.itemconfig(title, text="English", fill="Black")
    canvas.itemconfig(body, text=card_english, fill="Black")


def answer_known():
    global answered
    answered.append(rand_num)
    new_card()


# UI setup

window = Tk()
window.title(string="Lean Lang")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=528)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 269, image=card_back)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
body = canvas.create_text(400, 300, text="Body", font=("Ariel", 40, "bold"))

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=answer_known)
correct_button.grid(row=3, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=3, column=0)

new_card()

window.mainloop()
