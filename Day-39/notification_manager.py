from twilio.rest import Client
import os

class NotificationManager:
    account_sid = os.environ.get("TWILIO_ACC_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    # This class is responsible for sending notifications with the deal flight details.
    def formatMessage(self, price, destination, departure, arrival):
        msg = f"The flight to {destination} is available at Rs.{price}.Book fast!!\nDeparture:{departure}\nArrival:{arrival}"
        return msg

    def sendMessage(self, price, destination, departure, arrival):
        msg = f"The flight to {destination} is available at Rs.{price}.Book fast!!\nDeparture:{departure}\nArrival:{arrival}"
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
          from_='+12059527340',
          to='+917010054699',
          body=msg
        )
        print(message.status)
