import requests
import os
from datetime import datetime, timedelta
from dateutil import parser, tz
from pprint import pprint




class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    api_key = os.environ.get("TEQUILA_API_KEY")
    def getCode(self, airport):
        """
        Returns the code of the city mentioned
        :param airport: Name of the city
        :return: Code of the airport
        """

        endpoint = "https://api.tequila.kiwi.com/locations/query"
        header = {
            "apikey": self.api_key
        }
        params = {
            "term": airport
        }

        response = requests.get(url=endpoint, params=params, headers=header)
        response = response.json()["locations"][0]["code"]
        return str(response)

    def getPrice(self, fly_to):

        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()

        today = datetime.today().date().strftime("%d/%m/%Y")
        next_six_months = (datetime.today().date() + timedelta(days=180)).strftime("%d/%m/%Y")

        endpoint = "https://api.tequila.kiwi.com/v2/search"
        header = {
            "apikey": self.api_key
        }
        params = {
            "fly_from": "MAA",
            "fly_to": fly_to,
            "date_from": today,
            "date_to": next_six_months,
            "curr": "INR",
            "sort": "price"
        }

        response = requests.get(url=endpoint, headers=header, params=params)
        price = response.json()["data"][0]["price"]
        token = response.json()["data"][0]["booking_token"]
        arrival_utc = parser.parse(str(response.json()["data"][0]["utc_arrival"])).replace(tzinfo=from_zone)
        departure_utc = parser.parse(response.json()["data"][0]["utc_departure"]).replace(tzinfo=from_zone)
        arrival_ist = arrival_utc.astimezone(to_zone).strftime("%d/%m/%Y  %H:%M")
        departure_ist = departure_utc.astimezone(to_zone).strftime("%d/%m/%Y  %H:%M")
        return token, price, departure_ist, arrival_ist
