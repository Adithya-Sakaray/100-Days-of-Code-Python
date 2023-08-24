import data_manager
import flight_search
import notification_manager
import  user_manager

gsheet_manager = data_manager.DataManager()
flightManager = flight_search.FlightSearch()
notificationManager = notification_manager.NotificationManager()
userManager = user_manager.user_manager()


flight_sheet = gsheet_manager.get_details()
user_sheet = userManager.get_details_from_sheet()
all_email = []


def populate_codes():
    """
    Populates the Google sheet with the airport codes of the given airports
    :return: None
    """
    for data in flight_sheet:
        cityName = data["city"]
        row = data["id"]
        airportCode = flightManager.getCode(cityName)
        gsheet_manager.updateCodes(row, airportCode)

    print("Completed populating")


def send_message():

    for user in user_sheet:
        email = user["email"]
        all_email.append(email)

    for data in flight_sheet:
        city_name = data["city"]
        to_city_code = data["iataCode"]
        my_price = data["lowestPrice"]
        price, departure, arrival = flightManager.getPrice(to_city_code)
        if price < my_price:
            # notificationManager.sendMessage(price, city_name, departure, arrival)
            for email in all_email:
                notificationManager.sendMail(price, city_name, departure, arrival, email)


userManager.get_user_details_from_user()
populate_codes()
send_message()


