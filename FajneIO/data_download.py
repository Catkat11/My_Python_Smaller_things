import requests

sheety_ENDPOINT = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/io/arkusz1"


def data_downloading():
    try:
        response = requests.get(sheety_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        print(data)
        return data

    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania danych: {e}")
        return None
