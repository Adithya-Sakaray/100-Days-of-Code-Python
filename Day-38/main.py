import requests
import os
from datetime import datetime

APP_ID = os.environ.get("NUTRITIONIX_APPID")
API_KEY = os.environ.get("NUTRITIONIX_APPKEY")
data = datetime.now()
date = data.strftime("%d/%m/%Y")
time = data.strftime("%H:%M:%S")


def get_minutes_calories(exercise_text):
    exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": API_KEY,
    }

    parameters = {
        "query": exercise_text,
    }

    response = requests.post(exercise_endpoint, json=parameters, headers=headers)
    result = response.json()
    minutes = result["exercises"][0]["duration_min"]
    calories = result["exercises"][0]["nf_calories"]
    exercise = str(result["exercises"][0]["name"]).capitalize()
    return exercise, minutes, calories


def get_details():
    endpoint = "https://api.sheety.co/7dab9be838ede024177b121c807f8ec3/workoutTracking/workouts"
    header = {
        "Authorization": "Basic YWRpdGh5YXNha2FyYXlAZ21haWwuY29tOlNvcGFkYTEyMw=="
    }
    response = requests.get(url=endpoint, headers=header)
    response.raise_for_status()
    result = response.json()
    print(result)

def add_row():
    endpoint = "https://api.sheety.co/7dab9be838ede024177b121c807f8ec3/workoutTracking/workouts"
    header = {
        "Authorization": "Basic YWRpdGh5YXNha2FyYXlAZ21haWwuY29tOlNvcGFkYTEyMw=="
    }
    data = {
        "workout": {
                "date": date,
                "time": time,
                "exercise": exercise,
                "duration": minutes,
                "calories": calories,
                }
    }
    result = requests.post(url=endpoint, json=data, headers=header)
    result.raise_for_status()
    print(result.json())


user_input = input("What exercise did you do today? ")
exercise, minutes, calories = get_minutes_calories(user_input)
print(f"Exercise: {exercise}")
print(f"Duration: {minutes} mins")
print(f"Calories: {calories}")
add_row()