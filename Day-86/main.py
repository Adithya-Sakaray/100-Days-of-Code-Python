from tkinter import *
from data import paragraphs
import random

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Arial"

SCORE = 0
SECONDS = 60
PARAGRAPH = random.choice(paragraphs).split()
CURRENT_LINE = 0
CURRENT_WORD = 0
WORDS_IN_LINE = 10
LINE = PARAGRAPH[CURRENT_LINE: CURRENT_LINE + WORDS_IN_LINE]


def get_line(LINE):
    s = ""
    for word in LINE:
        s += word
        s += " "

    return s


def space_pressed(event):
    global CURRENT_LINE, CURRENT_WORD, WORDS_IN_LINE, LINE, PARAGRAPH, SCORE, SECONDS
    LINE = PARAGRAPH[CURRENT_LINE: CURRENT_LINE + WORDS_IN_LINE]


    word = input_field.get("1.0", "end")
    input_field.delete("1.0", "end")

    # print(f"Word: {word}")
    # print(f"Current word {PARAGRAPH[CURRENT_WORD]}")

    print(LINE)


    if word.lower().strip() == PARAGRAPH[CURRENT_WORD].lower():
        SCORE += 1

    if PARAGRAPH[CURRENT_WORD] == LINE[-1]:
        CURRENT_LINE += WORDS_IN_LINE
        LINE = PARAGRAPH[CURRENT_LINE: CURRENT_LINE + WORDS_IN_LINE]
        text_label.config(text=get_line(LINE), font=(FONT_NAME, 12), fg=PINK, bg=YELLOW, pady=20)

    CURRENT_WORD += 1


def start_timer():
    global SECONDS
    SECONDS = 60
    update_timer()


def update_timer():
    global SECONDS
    timer_label.config(text=f"Time left: {SECONDS} secs")
    if SECONDS > 0:
        SECONDS -= 1
        window.after(1000, update_timer)
    else:
        timer_label.config(text="Time's up!")
        score_label.config(text=f"Your score is {SCORE} wpm")


def reset():
    global SECONDS, CURRENT_WORD, CURRENT_LINE, SCORE

    SECONDS = 60
    CURRENT_WORD = 0
    CURRENT_LINE = 0
    SCORE = 0
    LINE = PARAGRAPH[CURRENT_LINE: CURRENT_LINE + WORDS_IN_LINE]
    text_label.config(text=get_line(LINE), font=(FONT_NAME, 12), fg=PINK, bg=YELLOW, pady=20)


window = Tk()
window.title("Typing test")
window.config(padx=100, pady=100, bg=YELLOW)

window.bind("<space>", space_pressed)

title_label = Label(text="Typing Speed Test", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW, pady=20)
title_label.grid(row=0, column=0)

text_label = Label(text=get_line(LINE), font=(FONT_NAME, 12), fg=PINK, bg=YELLOW, pady=20)
text_label.grid(row=1, column=0)

timer_label = Label(text=f"Time left: {SECONDS} secs", font=(FONT_NAME, 11), bg=YELLOW, fg="black", pady=20)
timer_label.grid(row=2, column=0)

input_field = Text(height=1, width=20)
input_field.grid(row=3, column=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=4, column=0, columnspan=2)

end_button = Button(text="Reset", command=reset)
end_button.grid(row=4, column=1, columnspan=2)

score_label = Label(text="", font=(FONT_NAME, 15), bg=YELLOW, fg=RED)
score_label.grid(row=5, column=0)

window.mainloop()
