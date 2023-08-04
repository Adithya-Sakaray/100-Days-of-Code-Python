import smtplib
from sunrise_sunset import MY_LAT, MY_LON, is_dark
import requests
from time import sleep

my_name = "Adithya"
my_email = "guystrange656@gmail.com"
password = "aezdyhxnjfqphruj"
to_email = "adithyasakaray@gmail.com"


def get_iss_location():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    if response.status_code == 200:
        content = response.json()
        longitude = content["iss_position"]["longitude"]
        latitude = content["iss_position"]["latitude"]
        location = (latitude, longitude)
        # print(f"Latitude: {latitude}")
        # print(f"Longitude: {longitude}")
        return location
    else:
        response.raise_for_status()
        return None


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg="Subject:ISS is above you\n\nHello Adithya,\n The International space station is above you check it out man\nWith regards,\n Your python bot")


while True:
    if is_dark():
        iss_location = get_iss_location()
        if ((MY_LAT - 5) < iss_location[0] < (MY_LAT + 5)) and ((MY_LON - 5) < iss_location[1] < (MY_LON + 5)):
            send_email()
    sleep(60)
