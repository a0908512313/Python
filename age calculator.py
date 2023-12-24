import datetime
import tkinter as tk

window = tk.Tk()
window.geometry = ('1080x960')
window.title(' Age Calculator App ')
name = tk.Label(text='name')
year = tk.Label(text='year')
month = tk.Label(text='month')
date = tk.Label(text='day')

name.grid(column=0, row=1)
year.grid(column=0, row=2)
month.grid(column=0, row=3)
date.grid(column=0, row=4)

nameEntry = tk.Entry()
yearEntry = tk.Entry()
monthEntry = tk.Entry()
dateEntry = tk.Entry()

nameEntry.grid(column=1, row=1)
yearEntry.grid(column=1, row=2)
monthEntry.grid(column=1, row=3)
dateEntry.grid(column=1, row=4)


def getInput():
    name = nameEntry.get()
    monkey = Person(name, datetime.date(int(yearEntry.get())),
                    int(monthEntry.get()), int(dateEntry.get()))

    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6)
    answer = ' Heyy {monkey}!!!. You are {age} year old!!!'.format(
        monkey=monkey.name(), age=monkey.age())

    textArea.insert(tk.END, answer)


button = tk.Button(window, text='Calculate Age', command=getInput, bg='pink')
button.grid(column=1, row=5)


class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age


window.mainloop()
