from twitter_handler import TwitterManager
import datetime

email = "your-email@gmail.com"
username = "your-username"
password = "your-password"

twitter_manager = TwitterManager()

time_now = datetime.datetime.now().time().strftime("%H")
morning = datetime.time(hour=10).strftime("%H")

if time_now < morning:
    print("It is morning")
    twitter_manager.login(username=username, password=password, email=email)
    twitter_manager.tweet(message="Good morning Twitter!!")

else:
    print("It is not morning")

