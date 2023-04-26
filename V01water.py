#!/usr/bin/python3
import requests as re
from gpiozero import Button
from signal import pause
import tkinter as tk
import time
line="dXrCowN5BX4xNngixA0aLHxMvkSLfubDQALakkaiH1N" #linenotify連結
button = Button(21)
def user_press():
    message = 'V01汙水坑高水位訊號!!'  
    print(message)  
    # HTTP 標頭參數與資料
    headers = { "Authorization": "Bearer " + line }
    data = { 'message': message }
# 以 requests 發送 POST 請求
    re.post("https://notify-api.line.me/api/notify", 
        headers = headers, data = data)
    time.sleep(30)
def user_released():
    message2 = 'V01汙水坑高水位訊號解除'  
    print(message2)  
    # HTTP 標頭參數與資料
    headers = { "Authorization": "Bearer " + line }
    data = { 'message': message2 }
# 以 requests 發送 POST 請求
    re.post("https://notify-api.line.me/api/notify", 
        headers = headers, data = data)
window = tk.Tk()
window.title("汙水坑水位")
label = tk.Label( text="程式正常執行")
label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)
window.geometry("380x400")
button.when_pressed = user_press
button.when_released = user_released
window.mainloop()
pause()
