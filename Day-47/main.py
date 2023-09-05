import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "guystrange656@gmail.com"
password = "aezdyhxnjfqphruj"
to = "adithyasakaray@gmail.com"

url = "https://www.amazon.in/2022-Apple-MacBook-Laptop-chip/dp/B0B3BLY13H/ref=sr_1_3?crid=28P3PF28FU7WE&keywords=macbook+m2&qid=1693907708&sprefix=macbook+m%2Caps%2C240&sr=8-3"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
}
response = requests.get(url=url, headers=header)
website = response.content

soup = BeautifulSoup(website, "lxml")

price = soup.find(name="span", class_="a-offscreen").getText()
price = price.split("₹")[1]
print(price)
price = float(price)

message = f"The product is available in amazon at Rs {price} hurry up!!"
print(message)

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=to, msg=f"Subject:Price Drop\n\n{message}")
    print("Email sent successfully!!")
