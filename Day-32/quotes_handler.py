import smtplib
import datetime as dt
import random as rand

my_email = "guystrange656@gmail.com"
password = "aezdyhxnjfqphruj"
to_email = "abhisakaray@gmail.com"

now = dt.datetime.now()
today = now.weekday()

with open("quotes.txt", "r") as file:
    quotes = file.read().split("\n")
    today_quote = rand.choice(quotes)


# send email
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Today's Quote\n\n{today_quote}")
