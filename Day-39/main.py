import data_manager
import flight_search
import notification_manager

gsheet_manager = data_manager.DataManager()
flightManager = flight_search.FlightSearch()
notificationManager = notification_manager.NotificationManager()

sheet_data = gsheet_manager.get_details()

def populateCodes():
    """
    Populates the google sheet with the aiport codes of the given airports
    :return: None
    """
    for data in sheet_data:
        cityName = data["city"]
        row = data["id"]
        airportCode = flightManager.getCode(cityName)
        gsheet_manager.updateCodes(row, airportCode)

    print("Completed populating")


populateCodes()
for data in sheet_data:
    city_name = data["city"]
    to_city_code = data["iataCode"]
    my_price = data["lowestPrice"]
    price, departure, arrival = flightManager.getPrice(to_city_code)
    if price < my_price:
        notificationManager.sendMessage(price, city_name, departure, arrival)


