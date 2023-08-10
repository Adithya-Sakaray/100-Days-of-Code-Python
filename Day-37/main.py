import requests
import os
from datetime import date

USERNAME = "adithyasakaray"
TOKEN = os.environ.get("PIXELA_API_KEY")
GRAPH_ID = "graph1"

# creating a account
# url = "https://pixe.la/v1/users"
# params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=url, json=params)

# creating a graph
# graph_url = f"https://pixe.la/v1/users/{USERNAME}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Coding Graph",
#     "unit": "times coded",
#     "type": "int",
#     "color": "shibafu"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# requests.post(url=graph_url, json=graph_params, headers=headers)


# recording the task

graph_url = "https://pixe.la/v1/users/adithyasakaray/graphs/graph1.html"

today = str(date.today())
today = today.replace("-", "")


def record_task(coded: str):
    record_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
    record_header = {
        "X-USER-TOKEN": TOKEN,
    }
    record_params = {
        "date": today,
        "quantity": coded
    }

    response = requests.post(headers=record_header, url=record_url, json=record_params)

    print(response.text)
    print(f"You can view your graph in: {graph_url}")



def update_task():
    update_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    update_header = {
        "X-USER-TOKEN": TOKEN
    }
    update_params = {
        "quantity": "5"
    }

    response = requests.put(headers=update_header, url=update_url, json=update_params)

    print(response.text)
    print(f"You can view your graph in: {graph_url}")



def delete_task():
    delete_url = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{today}"
    delete_header = {
        "X-USER-TOKEN": TOKEN,
    }

    response = requests.delete(headers=delete_header, url=delete_url)

    print(response.text)
    print(f"You can view your graph in: {graph_url}")


times_coded = input("How many times did you code today?")
record_task(times_coded)
