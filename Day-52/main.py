from instagram_handler import InstaManager

INSTA_USERNAME = "guystrange646@gmail.com"
INSTA_PASSWORD = "Sopada123"

bot = InstaManager()

bot.login(username=INSTA_USERNAME, password=INSTA_PASSWORD)
bot.find_followers(query="chefsteps")
