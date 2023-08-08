import requests
from twilio.rest import Client
import  os

url = "http://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": 13.0827,
    "lon": 80.2707,
    "appid": "XXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "units": "metric"
}
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
auth_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

response = requests.get(url=url, params=params)
weather_codes = []
will_rain = False

if response.status_code == 200:
    first_12 = response.json()["list"][:12]
    for i in range(len(first_12)):
        weather_codes.append(first_12[i]["weather"][0]["id"])
else:
    response.raise_for_status()

for item in weather_codes:
    if item < 700:
        will_rain = True


if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Take an Umbrella it is gonna rain",
            from_="+12059527340",
            to="+917010054699"
        )

    print(message.status)


