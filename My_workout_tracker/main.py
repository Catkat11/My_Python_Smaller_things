import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
import os


APP_ID = os.environ["NT_APP_ID"]
API_KEY = os.environ["NT_API_KEY"]

USER = os.environ["NT_USER"]
PASSWORD = os.environ["NT_PASSWORD"]


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise = input("What exercise you did: ")

sheety_endpoint = os.environ["SHEET_ENDPOINT"]



headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 78,
    "height_cm": 175,
    "age": 21
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

basic = HTTPBasicAuth(USER, PASSWORD)

sheety_response = requests.post(sheety_endpoint, json=sheety_inputs, auth=basic)
print(sheety_response.text)

