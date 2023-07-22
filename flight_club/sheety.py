import requests

sheety_endpoint = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/flightDealsUsers/users"


def post_new_row(first_name, last_name, email):

    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=sheety_endpoint, json=body)
    response.raise_for_status()
    print(response.text)
