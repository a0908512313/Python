import tkinter as tk
import random
import pyperclip

# 視窗參數設定
win = tk.Tk()
win.title("隨機XY座標生產器")
win.geometry("400x220+800+400")
win.config(bg="#323232")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

title_text = tk.Label(text="隨機XY座標生產器", fg="skyblue", bg="#323232")
title_text.config(font="微軟正黑體 15")
title_text.pack()

min_range = tk.Label(text="Min Range", fg="white", bg="#323232")
min_range.pack()
min_entry = tk.Entry()
min_entry.pack()

max_range = tk.Label(text="Max Range", fg="white", bg="#323232")
max_range.pack()
max_entry = tk.Entry()
max_entry.pack()

x_show = tk.Label(text="", fg="white", bg="#323232")
x_show.pack()

y_show = tk.Label(text="", fg="white", bg="#323232")
y_show.pack()


def gen_xy():
    min_val = int(min_entry.get())
    max_val = int(max_entry.get())
    # random.randint(最小值,最大值)
    x = str(random.randint(min_val, max_val))
    y = str(random.randint(min_val, max_val))
    x_show.config(text="X: " + x)
    y_show.config(text="Y: " + y)


def copy():
    xy = x_show.cget("text") + "\n" + y_show.cget("text")
    pyperclip.copy(xy)


genarate_button = tk.Button(text="Generate", command=gen_xy)
genarate_button.pack()

copy_button = tk.Button(text="  Copy", command=copy)
copy_button.pack()

win.mainloop()
