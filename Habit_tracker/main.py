import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

USERNAME = "lukaszz"
TOKEN = "jdkasnvijrniauovnakjdsvn"

ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    'agreeTermsofService': "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Coding graph",
    "unit": "Hours",
    "type": "float",
    "color": "momiji",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()

post_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?"),
}

response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)

put_endpoint = f"{post_endpoint}/{today.strftime('%Y%m%d')}"

put_config = {
    "quantity": "2.5",
}

# response = requests.put(url=put_endpoint, json=put_config, headers=headers)
# print(response.text)

# response = requests.delete(url=put_endpoint, headers=headers)
# print(response.text)
