import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 50.128250
MY_LONG = 18.988600
MY_EMAIL = "mail"
MY_PASSWORD = "password"


def positioning():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (MY_LONG - 5) <= iss_longitude <= (MY_LONG + 5) and (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5):
        return True
    else:
        return False


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    time_now = datetime.now().hour
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


while True:
    time.sleep(60)
    if positioning() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:ISS OVER YOUR HEAD!!!\n\n"
                                f"Hi!\nISS is now over your head and you can see it!")
