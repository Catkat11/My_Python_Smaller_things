from tkinter import *
import requests

import adding_data
from adding_data import add_data
from deleting_data import delete_data
from updating_data import update_data

sheety_ENDPOINT = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/io/arkusz1"


def back(search_frame, menu):
    search_frame.destroy()

    menu()


def search(menu_frame, window, menu):

    try:
        response = requests.get(sheety_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        print(data)

    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania danych: {e}")
        return None

    sheet_name = list(data.keys())[0]
    rows = data[sheet_name]

    label_text = f"{'ID': <5} {'Pacjent': <15}\n"

    for row in rows:
        label_text += f"{row['id']: <5} {row['pacjent']: <15}\n"

    menu_frame.destroy()

    search_frame = Frame(master=window)
    search_frame.pack(fill=BOTH, expand=True)

    add_button = Button(search_frame, text="Dodaj dane", width=15, command=lambda: adding_data.add_data(search_frame, window, menu))
    add_button.grid(column=0, row=0, pady=5)

    delete_button = Button(search_frame, text="Usuń dane", width=15, command=lambda: delete_data(search_frame, window, menu))
    delete_button.grid(column=0, row=1, pady=5)

    update_button = Button(search_frame, text="Zaaktualizuj dane", width=15, command=lambda: update_data(search_frame, window, menu))
    update_button.grid(column=0, row=2, pady=5)

    back_button = Button(search_frame, text="Wróć", width=15, command=lambda: back(search_frame, menu))
    back_button.grid(column=0, row=3, pady=5)

    label = Label(search_frame)
    label.grid(column=0, row=4)
    label.config(text=label_text)
