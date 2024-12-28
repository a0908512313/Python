from tkinter import *
import random


fg = "skyblue"
bg = "#323232"
content_font = "微軟正黑體15"

win = Tk()
win.title("猜數字遊戲")
win.geometry("+800+400")
win.config(bg=bg)

title_text = Label(text="猜數字遊戲", fg=fg, bg=bg, font="微軟正黑體 25")
title_text.grid(row=0)

min_num_title = Label(text="請輸入最小值", fg=fg, bg=bg, font=content_font)
min_num_title.grid(row=1)

min_num_entry = Entry(text="")
min_num_entry.grid(row=2)

max_num_title = Label(text="請輸入最大值", fg=fg, bg=bg, font=content_font)
max_num_title.grid(row=3)

max_num_entry = Entry(text="")
max_num_entry.grid(row=4)

# command

def num_get():
    max_num = int(max_num_entry.get())
    min_num = int(min_num_entry.get())
    true_num = random.randint(min_num, max_num)
    print(true_num)
    return true_num

true_num = num_get()

def check_num(true_num):
    guess_num = int(guess_num_entry.get())
    if guess_num == true_num:
        state.config(text="恭喜答對了")
    if guess_num >= true_num:
        state.config(text="小一點")
    if guess_num <= true_num:
        state.config(text="大一點")

# button
btn_getnum = Button(text="按下更新正確數字", command=num_get)
btn_getnum.grid(row=5)

guess_num_title = Label(text="請輸入您猜的數字:", fg=fg, bg=bg, font=content_font)
guess_num_title.grid(row=6)

guess_num_entry = Entry(text="")
guess_num_entry.grid(row=7)


btn_chack_num = Button(text="按下看結果", command=check_num)
btn_chack_num.grid(row=8)

state = Label(text="", fg=fg, bg=bg, font=content_font)
state.grid(row=9)


win.mainloop()
