from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
titles = soup.find_all(name="span", class_="titleline")
scores = soup.find_all(name="span", class_="score")
links = []
full = []

for i in range(len(titles)):
    item = titles[i]
    a_tag = item.find(name="a")
    titles[i] = a_tag.getText()
    links.append(a_tag.get("href"))

del titles[23]
del links[23]

for i in range(len(scores)):
    score_str = scores[i].getText()
    splitted = score_str.split()
    scores[i] = int(splitted[0])

for i in range(len(titles)):
    dic = {"title": titles[i], "link": links[i], "upvote": scores[i]}
    full.append(dic)

for i in range(len(links)):
    for j in range(i+1,len(links)):
        if full[i]["upvote"] < full[j]["upvote"]:
            t = full[i]
            full[i] = full[j]
            full[j] = t

print(full[0]["title"], full[0]["link"], full[0]["upvote"])



