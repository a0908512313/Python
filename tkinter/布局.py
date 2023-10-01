from tkinter import *

win = Tk()

win.title("")
win.geometry("200x200+800+400")

# pack和grid不可同時存在

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# pack布局(中心線)(縮放視窗大小位置不會變)
btn_pack = Button(text="pack")
btn_pack.pack  # .pack(side=TOP、BOTTOM、LEFT、RIGHT)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Place 布局(x,y座標布局)(縮放視窗大小位置會變)(可設定物件大小)
btn_place = Button(text="PLace")
# .place(anchor=NW、S、CENTER, x=int, y=int or , width=int, height=int)
btn_place.place(archor=CENTER, x=20, y=20, width=100, height=100)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# grid(網格布局) python需輸入0=我們說的1
# sth.grid(row=int ,column=int)(row:直的;column:橫的)
# 跨行sth.grid(row=int ,column=int, rowspan=int ,columnspan=int)

btn_grid = Button(text="grid")
btn_grid.grid(row=0, column=0)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

win.mainloop()
