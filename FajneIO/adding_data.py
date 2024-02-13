from tkinter import *
import requests

sheety_ENDPOINT = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/io/arkusz1"


def back(add_frame, menu):
    add_frame.destroy()

    menu()


def add_data_to_sheet(add_var):
    new_data = add_var.get()

    data_to_add = {
        'arkusz1': {'pacjent': new_data}
    }
    response = requests.post(sheety_ENDPOINT, json=data_to_add)
    print(response.json())


def add_data(search_frame, window, menu):

    search_frame.destroy()

    add_frame = Frame(master=window)
    add_frame.pack(fill=BOTH, expand=True)

    add_label = Label(add_frame, text="Dodaj pacjenta")
    add_label.grid(row=0, column=0)

    add_var = StringVar()
    add_input = Entry(add_frame, textvariable=add_var)
    add_input.grid(row=1, column=0)

    add_button = Button(add_frame, text="Dodaj", command=lambda: add_data_to_sheet(add_var))
    add_button.grid(row=2, column=0)

    back_button = Button(add_frame, text="Wróć", command=lambda: back(add_frame, menu))
    back_button.grid(row=3, column=0, pady=5)

