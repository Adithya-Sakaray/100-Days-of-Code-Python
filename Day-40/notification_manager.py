from twilio.rest import Client
import os
import smtplib

my_email = "guystrange656@gmail.com"
password = "aezdyhxnjfqphruj"


class NotificationManager:
    account_sid = os.environ.get("TWILIO_ACC_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

    # This class is responsible for sending notifications with the deal flight details.
    def formatMessage(self, token, price, destination, departure, arrival):
        msg = f"The flight to {destination} is available at Rs.{price}.Book fast!!\nDeparture:{departure}\nArrival:{arrival}"
        return msg

    def sendMessage(self, token, price, destination, departure, arrival):
        msg = f"The flight to {destination} is available at Rs.{price}.Book fast!!\nDeparture:{departure}\nArrival:{arrival}"
        client = Client(self.account_sid, self.auth_token)

        message = client.messages.create(
            from_='+12059527340',
            to='+917010054699',
            body=msg
        )
        print(message.status)

    def sendMail(self, token, price, destination, departure, arrival, to):
        msg = f"The flight to {destination} is available at Rs.{price}.Book fast!!\nDeparture:{departure}\nArrival:{arrival}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=to, msg=f"Subject:Flight Deal\n\n{msg}")
            print("Email sent successfully!!")

    def printMessage(self, token, price, destination, departure, arrival):
        msg = f"The flight to {destination} is available at Rs.{price}.Book fast!!\nDeparture:{departure}\nArrival:{arrival}"
        print(msg)

