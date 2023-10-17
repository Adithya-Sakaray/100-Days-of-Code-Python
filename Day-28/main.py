from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TICKS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #

def timer_reset():
    global REPS, TICKS, TIMER

    # noinspection PyTypeChecker
    window.after_cancel(TIMER)
    REPS = 0
    TICKS = 0
    timer_label.config(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    canvas.itemconfig(timer_value, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
    tick_mark.config(text="", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS, TICKS

    work_secs = WORK_MIN * 60
    small_sec = SHORT_BREAK_MIN * 60
    large_sec = LONG_BREAK_MIN * 60

    REPS += 1

    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        TICKS += 1
        timer_label.config(text="Work", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
        count_down(work_secs)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        timer_label.config(text="Short Break", font=(FONT_NAME, 40, "bold"), fg=PINK, bg=YELLOW)
        count_down(small_sec)
    elif REPS == 8:
        timer_label.config(text="Long Break", font=(FONT_NAME, 40, "bold"), fg=RED, bg=YELLOW)
        count_down(large_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    global TICKS, TIMER
    count_min = count // 60
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_value, text=f"{count_min}:{count_sec}")

    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        s = TICKS * "✓"
        tick_mark.config(text=s, font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomorodo")
window.config(padx=100, pady=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_value = canvas.create_text(100, 122, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=2)

timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=2)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=1)

reset_button = Button(text="Reset", command=timer_reset)
reset_button.grid(row=2, column=3)

tick_mark = Label(text="", font=(FONT_NAME, 20), fg=GREEN, bg=YELLOW)
tick_mark.grid(row=3, column=2)



window.mainloop()
