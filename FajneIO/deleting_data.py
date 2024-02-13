import requests
from tkinter import *

sheety_ENDPOINT = "https://api.sheety.co/fe7000b6f03cfe7edc4aa95b68641cbc/io/arkusz1"

def back(delete_frame, menu):
    delete_frame.destroy()

    menu()


def delete_data_from_sheet(delete_var):
    delete_data = delete_var.get()

    endpoint = f"{sheety_ENDPOINT}/{delete_data}"
    response = requests.delete(endpoint)


def delete_data(menu_frame, window, menu):

    menu_frame.destroy()

    delete_frame = Frame(master=window)
    delete_frame.pack(fill=BOTH, expand=True)

    delete_label = Label(delete_frame, text="Usuń pacjenta po ID")
    delete_label.grid(row=0, column=0)

    delete_var = StringVar()
    delete_input = Entry(delete_frame, textvariable=delete_var)
    delete_input.grid(row=1, column=0)

    delete_button = Button(delete_frame, text="Usuń", command=lambda: delete_data_from_sheet(delete_var))
    delete_button.grid(row=2, column=0)

    back_button = Button(delete_frame, text="Wróc", command=lambda: back(delete_frame, menu))
    back_button.grid(row=3, column=0, pady=5)
