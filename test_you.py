import requests as re
from gpiozero import Button
from signal import pause

def user_press():
      line="dXrCowN5BX4xNngixA0aLHxMvkSLfubDQALakkaiH1N" #linenotify連結
      message = 'V01汙水坑高水位訊號!!'  
      print(message)  
    # HTTP 標頭參數與資料
      headers = { "Authorization": "Bearer " + line }
      data = { 'message': message }

# 以 requests 發送 POST 請求
      re.post("https://notify-api.line.me/api/notify", 
            headers = headers, data = data)  
    
button = Button(18)
button.when_pressed = user_press
pause()

