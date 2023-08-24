import requests


class user_manager:

    def __init__(self):
        self.email = None
        self.last_name = None
        self.first_name = None

    def get_user_details_from_user(self):
        print("Welcome to Adithya's flight agency!!!")
        print("We find the best deals and email you")
        self.first_name = input("Please enter your first name: ")
        self.last_name = input("Please enter your last name: ")
        self.email = input("Please enter your email: ")

        endpoint = "https://api.sheety.co/7dab9be838ede024177b121c807f8ec3/users/sheet1"
        data = {
            "sheet1": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }

        response = requests.post(url=endpoint, json=data)
        if response.status_code == 200:
            print("We have received your details!!!")

    def get_details_from_sheet(self):
        endpoint = "https://api.sheety.co/7dab9be838ede024177b121c807f8ec3/users/sheet1"

        response = requests.get(url=endpoint)
        response = response.json()["sheet1"]

        return response


