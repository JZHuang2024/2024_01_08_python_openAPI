#2024.01.22.Monday.In-class.Writthen by 徐國堂
#底下的式碼是必須在Thonny上執行樹莓派
#       使用Thonny Python IDE編寫MicroPython程式
#       Thonny（thonny.org）是專門為Python初學者打造的IDE（整合開發環境），
#       有Windows, Mac和Linux版本，也是樹莓派作業系統（Raspberry Pi OS）內建的Python程式開發工具
#           Raspberry Pi Pico W是一款樹莓派官方設計美觀但靈活的RP2040開發平台，其是Raspberry Pi Pico的無線升級版，
#           具有Pico所有功能外還有2.4GHz無線介面。
#
#
#⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇this one run under Thonny⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
#how to find the manual :
#       MicroPython documentation /Quick reference for the RP2 / Pins and GPIO
#       https://docs.micropython.org/en/latest/rp2/quickref.html#pins-and-gpio
#⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆

from machine import Pin
from tools import connect,reconnect
import time
import urequests

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
connect()

while True:         #while 是循環結構(while一定要小寫)，while 後面搭配布林值(boolean)並用，False則終止循環，True是表示為真，while True即一直進行loop（但循环是死的）。
    if btn.value():         #條件式&迴圈整理:if-else跟while loop不同的是，while會執行很多次，不斷地詢問，直到跳出loop，移到No區間為止，而if-else只會執行一次。
        is_press = True
        red_led.value(1)
    else:
        if is_press == True:
            print('release')
            is_press = False
            url_str = 'https://openapi-test-ukni.onrender.com/pico_w/2024-01-22 16:02:10?address=chicken_KFC&celsius=15.386'
            try:
                response = urequests.get(url_str)            
            except:
                print("ap出現問題")            
                reconnect()
            else:
                if response.status_code == 200:            
                    print("傳送訊息成功")
                else:
                    print("傳送失敗(server出現錯誤)")
                response.close()
            
        
        red_led.value(0)