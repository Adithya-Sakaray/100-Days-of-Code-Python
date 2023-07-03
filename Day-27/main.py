from tkinter import *


def calculate():
    miles = int(miles_value.get())
    km = miles * 1.60934
    km = round(km, 1)
    km_value_label.config(text=str(km))


window = Tk()
window.title("Miles to km converter ")
window.config(padx=20, pady=20)

# empty_label = Label(text=" ")
# empty_label.grid(row=0, column=0)

miles_value = Entry(width=10)
miles_value.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)


text_label = Label(text="is equal to")
text_label.grid(row=1, column=0)

km_value_label = Label(text="0")
km_value_label.grid(row=1, column=1)

km_label = Label(text="Kms")
km_label.grid(row=1, column=3)

submit_button = Button(text="Calculate", command=calculate)
submit_button.grid(row=2, column=1)



window.mainloop()
