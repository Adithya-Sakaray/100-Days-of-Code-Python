import requests
import datetime as dt

MY_LAT = 13.082680
MY_LON = 80.270721

parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

if response.status_code == 200:
    content = response.json()
    sunrise_data = content["results"]["sunrise"].split("T")[1].split(":")
    sunset_data = content["results"]["sunset"].split("T")[1].split(":")
    sunset_hour = int(sunset_data[0])
    sunset_min = int(sunset_data[1])
    sunrise_hour = int(sunrise_data[0])
    sunrise_min = int(sunrise_data[1])
else:
    response.raise_for_status()

now_hour = int(dt.datetime.now().hour)
now_min = int(dt.datetime.now().minute)


def is_dark():
    if now_hour >= sunset_hour or now_hour < sunrise_hour:
        if now_min > sunset_min or now_min < sunrise_min:
            return True
        else:
            return False
    else:
        return False

