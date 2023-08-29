from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
movies_webite = response.text

soup = BeautifulSoup(movies_webite, "html.parser")

movie_titles = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

for i in range(len(movie_titles)):
    movie_titles[i] = movie_titles[i].getText()

movie_titles.reverse()

with open("movie_list.txt", "w") as file:
    for item in movie_titles:
        file.write(f"{item}\n")



