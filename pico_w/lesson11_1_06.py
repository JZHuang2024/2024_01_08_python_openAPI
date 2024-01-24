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




#修改2024.01.24.Wed.In-class.Writthen by 徐國堂
from machine import Pin
from tools import connect,reconnect
import time
import urequests

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
#connect()

def getCurrentTime():
    times_tuple = time.localtime()
    currentTime = f'{times_tuple[0]}-{times_tuple[1]}-{times_tuple[2]} {times_tuple[3]}:{times_tuple[4]}:{times_tuple[5]}'
    return currentTime

def getTemperature():
    sensor_temp = machine.ADC(4)
    conversion_factor = 3.3 / (65535)
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    return temperature

while True:
    if btn.value():
        #解決按下彈跳
        time.sleep_ms(50)
        if btn.value():
            is_press = True
            red_led.value(1)
    else:
        #解決放開彈跳
        time.sleep_ms(50)
        if btn.value() == False:
            if is_press == True:     
                print('release')                
                print(getCurrentTime())
                print(getTemperature())
                is_press = False
                '''     #'''點三點區間變文字不執行
                url_str = 'https://openapi-test-ukni.onrender.com/pico_w/2024-01-22 16:02:10?address=chicken_KFC&celsius=15.386'
                try:
                    response = urequests.get(url_str)
                    pass
                except:
                    print("ap出現問題")            
                    reconnect()
                else:
                    if response.status_code == 200:            
                        print("傳送訊息成功")
                    else:
                        print("傳送失敗(server出現錯誤)")
                    response.close()
                '''     #'''點三點區間變文字不執行
            
        
            red_led.value(0)

