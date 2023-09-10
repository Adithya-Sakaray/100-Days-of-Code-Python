from selenium import webdriver
from twitterBot import TwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 50
TWITTER_EMAIL = "your email"
TWITTER_PASSWORD = "your password"



bot = TwitterBot()

bot.get_internet_speed()

if bot.up < PROMISED_UP or bot.down < PROMISED_DOWN:
    print(f"Up:{bot.up}\nDown:{bot.down}")
    print("We are getting less than promised")

    msg = f"Hey, ISP why is my internet speed {bot.down} down/{bot.up} up when I pay for 150 down/ 50 up"
    bot.tweet_about_speed(email=TWITTER_EMAIL, password=TWITTER_PASSWORD, message=msg)

else:
    print("We are getting what we have been promised")
