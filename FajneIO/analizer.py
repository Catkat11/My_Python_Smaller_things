from tkinter import *


def analysing():
    analyse_window = Tk()
    analyse_window.title("Analizowanie")
    analyse_window.configure(pady=25, padx=25)

    analyse_frame = Frame(master=analyse_window)
    analyse_frame.pack(fill=BOTH, expand=True)

    label = Label(analyse_frame, text="Analizowanie danych")
    label.grid(column=0, row=0)

    analyse_window.mainloop()
