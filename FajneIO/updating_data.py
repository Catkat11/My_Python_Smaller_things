import requests
from tkinter import *

sheety_ENDPOINT = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/io/arkusz1"


def back(update_frame, menu):
    update_frame.destroy()

    menu()


def update_data_from_sheet(update_var, update_id_var):
    update_data = update_var.get()
    update_id = update_id_var.get()

    data = {
        'arkusz1': {'pacjent': update_data}
    }

    endpoint = f"{sheety_ENDPOINT}/{update_id}"

    response = requests.put(endpoint, json=data)
    print(response.json())


def update_data(menu_frame, window, menu):

    menu_frame.destroy()

    update_frame = Frame(master=window)
    update_frame.pack(fill=BOTH, expand=True)

    update_label = Label(update_frame, text="Zaaktualizuj imię pacjenta: ")
    update_label.grid(row=0, column=0)

    update_var = StringVar()
    update_input = Entry(update_frame, textvariable=update_var)
    update_input.grid(row=1, column=0)

    update_label_id = Label(update_frame, text="ID pacjenta do zmiany: ")
    update_label_id.grid(row=2, column=0)

    update_id_var = StringVar()
    update_id_input = Entry(update_frame, textvariable=update_id_var)
    update_id_input.grid(row=3, column=0)

    update_button = Button(update_frame, text="Zaaktualizuj", command=lambda: update_data_from_sheet(update_var, update_id_var))
    update_button.grid(row=4, column=0)

    back_button = Button(update_frame, text="Wróć", command=lambda: back(update_frame, menu))
    back_button.grid(row=5, column=0, pady=5)
