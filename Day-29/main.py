from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    password_field.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)
    password_field.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_field.get()
    email = email_field.get()
    password = password_field.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(message="Please fill all the details!!")
    else:
        confirm_msg = f"These are the details entered:\nEmail: {email}\nPassword: {password}\nAre you sure?"
        is_ok = messagebox.askyesno(title=website, message=confirm_msg)

        if is_ok:
            with open("data.txt", "a") as file:
                s = f"{website} | {email} | {password}\n"
                file.write(s)
            website_field.delete(0, END)
            password_field.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image
canvas = Canvas(height=200, width=190)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=lock_img)
canvas.grid(row=0, column=1)

# labels
label1 = Label(text="Website", pady=10)
label1.grid(row=1, column=0)

label2 = Label(text="Email", pady=10)
label2.grid(row=2, column=0)

label3 = Label(text="Password", pady=10)
label3.grid(row=3, column=0)

# text-fields
website_field = Entry(width=50)
website_field.focus()
website_field.grid(row=1, column=1, columnspan=2)

email_field = Entry(width=50)
email_field.insert(0, "adithyasakaray@gmail.com")
email_field.grid(row=2, column=1, columnspan=2)

password_field = Entry(width=28)
password_field.grid(row=3, column=1)

# buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=30, command=save_info)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
