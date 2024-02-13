from tkinter import *


def save():
    save_window = Tk()
    save_window.title("Zapisywanie")
    save_window.configure(padx=25, pady=25)

    save_frame = Frame(master=save_window)
    save_frame.pack(fill=BOTH, expand=True)

    label = Label(save_frame, text="Zapisywanie danych")
    label.grid(column=0, row=0)

    save_window.mainloop()
