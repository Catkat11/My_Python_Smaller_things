from tkinter import *
from data_download import data_downloading
from analizer import analysing
from saving import save
from searching import search
from werkzeug.security import generate_password_hash, check_password_hash


def menu():
    login_frame.destroy()

    menu_frame = Frame(master=window)
    menu_frame.pack(fill=BOTH, expand=True)

    title_label = Label(menu_frame, text=f"Witaj")
    title_label.grid(column=0, row=0, pady=5)

    button2 = Button(menu_frame, text="Przeglądaj Dane", highlightthickness=0, command=lambda: search(menu_frame, window, menu), width=15)
    button2.grid(column=0, row=2, pady=5)


    button4 = Button(menu_frame, text="Analizuj Dane", highlightthickness=0, command=analysing, width=15)
    button4.grid(column=0, row=4, pady=5)

    button5 = Button(menu_frame, text="Zmień Hasło", highlightthickness=0, command=lambda: change_password(menu_frame, window, menu), width=15)
    button5.grid(column=0, row=5, pady=5)

    button5 = Button(menu_frame, text="Wyjdź", highlightthickness=0, command=quit, width=15)
    button5.grid(column=0, row=6, pady=5)

    window.mainloop()


def checking_password(login_var, password_var):
    login = login_var.get()
    user_password = password_var.get()
    with open("password.txt", "r") as file:
        password = file.read()

    if check_password_hash(password, user_password):
        menu()
    else:
        pass


def back(changing_password_frame, menu):
    changing_password_frame.destroy()

    menu()


def updating_password(old_var, new_var, new_var_again, changing_password_frame, menu):
    old_pass = old_var.get()
    new_pass = new_var.get()
    new_pass_again = new_var_again.get()

    if new_pass == new_pass_again:

        with open("password.txt", "r") as file:
            password = file.read()

        if check_password_hash(password, old_pass):
            hash_password = generate_password_hash(
                new_pass,
                method='pbkdf2:sha256',
                salt_length=8
            )
            with open("password.txt", "w") as file:
                file.write(hash_password)

    changing_password_frame.pack_forget()
    menu()


def change_password(menu_frame, window, menu):

    menu_frame.destroy()

    changing_password_frame = Frame(master=window)
    changing_password_frame.pack(fill=BOTH, expand=True)

    old_label = Label(changing_password_frame, text="Wpisz stare hasło: ")
    old_label.grid(column=0, row=0, pady=5)

    old_var = StringVar()
    old_entry = Entry(changing_password_frame, textvariable=old_var, show="*")
    old_entry.grid(column=1, row=0, pady=5)

    new_label = Label(changing_password_frame, text="Wpisz nowe hasło: ")
    new_label.grid(column=0, row=1, pady=5)

    new_var = StringVar()
    new_entry = Entry(changing_password_frame, textvariable=new_var, show="*")
    new_entry.grid(column=1, row=1, pady=5)

    new_label_again = Label(changing_password_frame, text="Wpisz ponownie nowe hasło: ")
    new_label_again.grid(column=0, row=2, pady=5)

    new_var_again = StringVar()
    new_entry_again = Entry(changing_password_frame, textvariable=new_var_again, show="*")
    new_entry_again.grid(column=1, row=2, pady=5)

    continue_button = Button(changing_password_frame, text="Dalej",
                             command=lambda: updating_password(old_var, new_var,
                                                               new_var_again, changing_password_frame, menu), width=15)
    continue_button.grid(column=0, row=3, pady=5, columnspan=2)

    back_button = Button(changing_password_frame, text="Cofnij", command=lambda: back(changing_password_frame, menu),
                         width=15)
    back_button.grid(column=0, row=4, pady=5, columnspan=2)


window = Tk()
window.title("Fajne IO")

login_frame = Frame(master=window)
login_frame.pack(fill=BOTH, expand=True)

window.configure(pady=100, padx=100)

login_var = StringVar()
login_label = Label(login_frame, text="login")
login_label.grid(column=0, row=0)

login_input = Entry(login_frame, textvariable=login_var)
login_input.grid(column=1, row=0)

password_label = Label(login_frame, text="password")
password_label.grid(column=0, row=1)

password_var = StringVar()
password_input = Entry(login_frame, show="*", textvariable=password_var)
password_input.grid(column=1, row=1)

button = Button(login_frame, text="Login", command=lambda: checking_password(login_var, password_var))
button.grid(columnspan=2, column=0, row=2)

window.mainloop()
