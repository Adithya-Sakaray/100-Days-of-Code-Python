import requests
import os
from pprint import pprint


class DataManager:

    sheety_auth = os.environ.get("SHEETY_AUTH_FLIGHT")
    # This class is responsible for talking to the Google Sheet.
    def get_details(self):
        """
        Returns the data in Google sheet as a list of dictionaries
        :return: data in Google sheet as a list of dictionaries
        """
        endpoint = "https://api.sheety.co/7dab9be838ede024177b121c807f8ec3/flightDeals/prices"
        header = {
            "Authorization": self.sheety_auth
        }

        response = requests.get(url=endpoint, headers=header)
        response.raise_for_status()
        response = response.json()["prices"]

        return response

    def updateCodes(self, row, code):
        """
        Updates the data in google sheet
        :param row: Row number
        :param code: Airport Code
        :return: None
        """
        endpoint = f"https://api.sheety.co/7dab9be838ede024177b121c807f8ec3/flightDeals/prices/{row}"
        header = {
            "Authorization": self.sheety_auth
        }
        data = {
            "price": {
                "iataCode": code
            }
        }

        response = requests.put(url=endpoint, headers=header,json=data)
        response.raise_for_status()
