import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
account_sid = "AC9237e3c5b844ead669f24a93eeb80797"
api_key = "api_key"
auth_token = "auth_token"

weather_params = {
    "lat": 50.128250,
    "lon": 18.988600,
    "appid": api_key
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="+15737495194",
        to="+48666666666"
    )
    print(message.status)
