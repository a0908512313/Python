from distutils.cmd import Command
from tkinter import *

win = Tk()

win.title("Login")
win.geometry("+800+400")

# Label
user = Label(text="User")
user.grid(row=0, column=0)

password = Label(text="Password")
password.grid(row=1, column=0)

state = Label(text="state: ")
state.grid(row=2, column=1)

# Entry
entry_user = Entry(bg="#323232", font="微軟正黑體")
entry_user.grid(row=0, column=1)
entry_password = Entry(bg="#323232", font="微軟正黑體")
entry_password.grid(row=1, column=1)

# Data
true_user = "1234"
true_password = "123"

# command


def login_com():
    # input.get
    user_input = str(entry_user.get())
    password_input = str(entry_password.get())

    if user_input == true_user and password_input == true_password:
        state.config(text="Login success!")
    else:
        state.config(text="user or password wrong")


# Botton
btn_login = Button(text="Login", command=login_com)
btn_login.grid(row=3, column=1)

win.mainloop()
