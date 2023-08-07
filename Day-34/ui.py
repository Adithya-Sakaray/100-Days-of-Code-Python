from tkinter import *
from quiz_brain import QuizBrain
from time import sleep

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=240,
                                                     text="Question",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=50)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=1)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            q_text = "You have reached the end of the quiz!!!!"
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        is_correct = self.quiz_brain.check_answer("true")
        self.give_feedback(is_correct)

    def false_pressed(self):
        is_correct = self.quiz_brain.check_answer("false")
        self.give_feedback(is_correct)

    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(250, self.get_next_question)
        self.score_label.config(text=f"Score: {self.quiz_brain.score}")



