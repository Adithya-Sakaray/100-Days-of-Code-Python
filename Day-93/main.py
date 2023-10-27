import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.audible.in/search?node=21881795031&pageSize=50&sort=popularity-rank&ref_pageloadid=gY5SCQXESGv3r6qI&ref=a_search_c4_pageSize_3&pf_rd_p=b54fcd14-da4e-4eac-bb29-fbf84d0dd022&pf_rd_r=R4V8TERXRD7A70ZVXDC8&pageLoadId=kjXly5NJ03qM6tdU&ref_plink=not_applicable&creativeId=dde0429d-3138-4cb1-9b9a-df4c91c52b39"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br"
}
website = requests.get(url=url, headers=header)

soup = BeautifulSoup(website.text, "html.parser")

titles = soup.find_all(name="div", class_="bc-col-6")

all_books_list = []
all_books_list.append([
    "Book title", "Author", "Narrator", "Duration", "Release Date", "Rating"
])

for i, item in enumerate(titles):

    if 2 <= i:
        div = item.find(name="div", class_="bc-row-responsive")
        another_div = div.find(name="div", class_="bc-col-responsive")
        span = another_div.find(name="span")
        ul = span.find(name="ul", class_="bc-list")
        all_info = ul.find_all(name="li", class_="bc-list-item")
        book = []
        for i, info in enumerate(all_info):
            text = ""
            text = info.getText()
            text = ' '.join(text.split())
            if i == 0:
                book.append(text)
            elif i == 1:
                l = " ".join(text.split()[2:])
                book.append(l)
            elif i == 2:
                new_text = " ".join(text.split()[2:])
                book.append(new_text)
            elif i == 3:
                new_text = " ".join(text.split()[1:])
                book.append(new_text)
            elif i == 4:
                new_text = " ".join(text.split()[2:])
                book.append(new_text)
            elif i == 5:
                new_text = " ".join(text.split()[1:])
                book.append(new_text)
            else:
                book.append(text.split()[0])

        all_books_list.append(book)

for item in all_books_list:
    print(item)

with open('books.csv', 'w', newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in all_books_list:
        csv_writer.writerow(item)



