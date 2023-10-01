from operator import length_hint
from tkinter import *

win = Tk()

win.title("thinter test")
win.geometry("400x200+800+400")


def change(self):
    s_value = s.get()
    # -alpha, int (透明度)
    win.attributes("-alpha", s_value/100)
    print(s_value/100)


# orient(滑桿方向)=VERTICAL(垂直) or HORIZONTAL(水平)
# width(寬度)=int,length(長度)=int
# showvalue(滑桿數值是否顯示)=0or1
# from_= int ,to=int (數值從多少到多少)
# tickinterval=int (以多少為一等分)
# resolution=int (一次移動多少)
# digits=int (顯示幾位數)
s = Scale(orient=VERTICAL, width=100, length=200)
s.config(showvalue=1)
s.config(from_=10, to=100)
s.config(tickinterval=10)
s.config(resolution=10)
s.config(digits=4)
s.set(0.1)
s.config(command=change)
s.pack()

win.mainloop()
