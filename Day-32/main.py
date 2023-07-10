import datetime as dt
import smtplib
import random as rand
import pandas


def send_mail(to, message):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to, msg=f"Subject:Happy Birthday!!\n\n{message}")
        print("Email sent successfully!!")


# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
my_name = "Adithya"
my_email = "guystrange656@gmail.com"
password = "aezdyhxnjfqphruj"
letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
now = dt.datetime.now()

with open("birthdays.csv", "r") as file:
    data = pandas.read_csv(file)
    data = pandas.DataFrame.to_dict(data, orient="records")

for person in data:
    name = person["name"]
    to_email = person["email"]
    if person["month"] == now.month and person["day"] == now.day:
        with open(rand.choice(letter_list), "r") as file:
            content = file.read().replace("[NAME]", f"{name}")
            content = content.replace("Angela", my_name)
        send_mail(to=to_email, message=content)

# 4. Send the letter generated in step 3 to that person's email address.




