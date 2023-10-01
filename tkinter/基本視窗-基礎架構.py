import tkinter as tk

win = tk.Tk()

# 標題:win.title("")
win.title("thinter test")

# 字體、顏色、大小
# ~.config(font="字體 大小")

# 大小:win.geomeetry("intXint+int(1)+int(2)") int(1、2視窗固定位置
# 固定大小:win.resizeable(False, False)or(0, 0)   (0 = False ; 1 = True)
#最大win.maxsize(width=(int), height=(int))
#最小win.minsize(width=(int), height=(int))
win.geometry("400x200")
win.minsize(width=400, height=200)
win.maxsize(width=960, height=1080)

# ICON:win.iconbitmap(圖檔路徑)
win.iconbitmap()

# 顏色:win.config(background="") or (bg="")
win.config(bg="white")

# 透明度:win.attributes("-alpha", int) (int)>>1~0 1=100% 0=0%
win.attributes("-alpha", 0.5)

# 置頂(最上層):win.attributes("-topmost", int)
# or ("-topmost", True、Flase)
win.attributes("-topmost", 0)

# 按鈕圖片
#img = tk.PhotoImage("")

# 按鈕連結
# def hi():
# print("hi")

# Button
# btn = tk.Button(text="", bg="", width=int, height=int,command=連結)
# or btn.config(bg="")
# or btn.congif(width=int, height=int)
# btn.pack()
btn = tk.Button(text="Hi",  bg="skyblue", width=10, height=5)
btn.pack()

# label標籤
# lb = tk.Label(bg="", fg="" ,text="")
lb = tk.Label(bg="white", fg="white", text="This is lable")
lb.config(text="change")
lb.pack()

# entry輸入
en = tk.Entry()
en.pack

win.mainloop()
