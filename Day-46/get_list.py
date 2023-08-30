import requests
from bs4 import BeautifulSoup

def get_list_and_date():
    user_date = input("Enter the date you want to be transported in this format(YYYY-MM-DD):")
    url = f"https://www.billboard.com/charts/india-songs-hotw/{user_date}/"
    # Getting the top 25 songs from the given date
    billboard_website = requests.get(url=url)
    soup = BeautifulSoup(billboard_website.text, "html.parser")
    song_titles = soup.find_all(name="h3", id="title-of-a-story")
    song_titles_list = []
    for item in song_titles:
        song_titles_list.append(item.getText())
    song_titles_list = song_titles_list[2:27]
    for i in range(len(song_titles_list)):
        song_titles_list[i] = song_titles_list[i].strip()

    return song_titles_list,user_date
