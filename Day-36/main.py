import requests
from datetime import date, timedelta
import os
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "TeslaInc"
today = str(date.today())
yesterday = str(date.today() - timedelta(days=1))
day_before = str(date.today() - timedelta(days=2))
yesterday_price = ""
day_before_price = ""
news_list = []


def get_arrows():
    if difference > 0:
        return "increase"
    return "decrease"

def get_news():
    """
    It gets the top 5 news related to Tesla Inc
    :return: None
    """
    news_url = "https://newsapi.org/v2/everything"
    news_params = {
        "q": COMPANY_NAME,
        "from": day_before,
        "to": yesterday,
        "apiKey": os.environ.get("NEWS_API")
    }

    news_response = requests.get(url=news_url, params=news_params)
    if news_response.status_code == 200:
        news_data = news_response.json()["articles"][:5]
        for i in range(5):
            news_dict = {"title": news_data[i]["title"], "description": news_data[i]["description"]}
            news_list.append(news_dict)
    else:
        news_response.raise_for_status()


# get the stck prices of previous 2 days
url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": os.environ.get("STOCK_API")
}
response = requests.get(url=url, params=params)
if response.status_code == 200:
    total_data = response.json()["Time Series (Daily)"]
    yesterday_price = total_data[yesterday]["4. close"]
    day_before_price = total_data[day_before]["4. close"]
else:
    response.raise_for_status()

day_before_price_float = float(day_before_price)
yesterday_price_float = float(yesterday_price)
difference = day_before_price_float - yesterday_price_float
percent = round((abs(difference) / day_before_price_float) * 100)

if difference < 0 and percent >= 2:
    get_news()
elif difference > 0 and percent >= 2:
    get_news()
else:
    get_news()

message_to_be_sent = f"""
{STOCK}: {percent} % {get_arrows()}\n
Headline: {news_list[0]["title"]}\n\nBrief: {news_list[0]["description"]}
"""

print(message_to_be_sent)


# sending the message
account_sid = os.environ.get("TWILIO_ACC_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)
message = client.messages \
    .create(
        body=message_to_be_sent,
        from_="+12059527340",
        to="+917010054699",
    )

print(message.status)


