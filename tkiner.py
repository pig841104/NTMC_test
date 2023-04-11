import tkinter as tk
from tkinter.constants import *
win = tk.Tk()
win.title("hello")  #視窗標題
win.geometry("200x200")  #視窗大小
bt =tk.Button(text="click",command=exit,padx=30,pady=30)  #按鈕標籤
bt.pack()    #位置布局
menu =tk.Menu(win)      #建立上排開啟檔案
win.config(menu=menu)
menu.add_command(label ="open") #新增選項

win.mainloop()  #視窗開啟迴圈，須在最後一行
#win.iconbitmap()  #視窗圖示
