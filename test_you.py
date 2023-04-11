#import RPi.GPIO as GPIO
import requests as re
line="dXrCowN5BX4xNngixA0aLHxMvkSLfubDQALakkaiH1N" #linenotify連結
message = 'test'    
# water =GPIO.input
# if water(17, GPIO,HIGH)
#     print("高水位") 
      # HTTP 標頭參數與資料
headers = { "Authorization": "Bearer " + line }
data = { 'message': message }

# 以 requests 發送 POST 請求
re.post("https://notify-api.line.me/api/notify", 
    headers = headers, data = data)  



