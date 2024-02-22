import datetime
import calendar
import tkinter as tk

window = tk.Tk()
window.geometry = ('1080x1080')
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


def calculateAge():

    textArea = tk.Text(master=window, height=10, width=25)
    textArea.grid(column=1, row=6, columnspan=2)
    today = datetime.date.today()

    age_list = {}
    age_list[0] = yearEntry.get()
    age_list[1] = monthEntry.get()
    age_list[2] = dateEntry.get()

    name = nameEntry.get()
    year = today.year - int(age_list[0])
    month = today.month - int(age_list[1])
    if month < 0:
        year = year - 1
        month = 12 + month
    day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if calendar.isleap(today.year):
        day_list[1] = 29
    day = today.day - int(age_list[2])
    if day < 0:
        month = month - 1
        if month < 0:
            year = year - 1
            month = 12 + month
        day = day_list[month] + day

    answer = (
        f' Hi {name}!! Your are {year} 歲 {month} 個月 {day} 天 years old now!!!')
    textArea.insert(tk.END, answer)


button = tk.Button(window, text='Calculate Age',
                   command=calculateAge, bg='pink')
button.grid(column=1, row=5)

window.mainloop()
