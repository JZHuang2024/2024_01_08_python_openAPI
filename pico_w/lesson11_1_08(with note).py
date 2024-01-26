#2024.01.24_WED_AM11:59
#上一個步驟接 C:\Users\user\Documents\GitHub\2024_01_08_python_openAPI\main2.py


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





#程式寫完丟到Thonny,樹莓派必須連上電腦
################################################光敏電阻################################################
#老師線上筆記
#https://github.com/roberthsu2003/pico_W/tree/main/%E4%B8%80%E8%88%AC%E6%93%8D%E4%BD%9C/2_6%E5%85%89%E6%95%8F%E9%9B%BB%E9%98%BB
#官方線上筆記
#https://docs.micropython.org/en/latest/rp2/quickref.html#adc-analog-to-digital-conversion


from machine import Pin, ADC
from tools import connect,reconnect
import time
import urequests

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False
connect()  #改改改:解封

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

def getLightValue():
    adc_light = ADC(Pin(28))
    light_value = adc_light.read_u16()
    return light_value

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
                currentTime = getCurrentTime()  #改改改
                temperature= getTemperature()   #改改改
                light=getLightValue()           #改改改
                
                is_press = False
                #⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇改改改:解封⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇⬇
                url_str = f'https://openapi-test-ukni.onrender.com/pico_w/{currentTime}?address=chicken_KFC&celsius={temperature}&light={light}'
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
                # ⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆改改改:解封⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆⬆
            
        
            red_led.value(0)



#下一個步驟接 在Thonny執行這個檔案11_1_08.py
#成功在Thonny下面出現
#MPY: soft reboot
#            等待連線
#            等待連線
#            等待連線
#            等待連線
#            連線成功
#            ip=172.16.12.101
#            
#            按下樹莓派按鍵
#        
#            release
#            
#            等20~30sec傳render server
#                    
#           
#            傳送訊息成功
#
#下一個步驟進入render server / 先前建立德 Web Service -->_openAPI_test_ /Logs成功y下面出現
#            https://dashboard.render.com/
#           
#            日期:2024-1-24 13:26:7
#            位置:chicken_KFC
#            攝氏:28.91698
#            光線:16211.0
#            INFO:     223.136.175.57:0 - "GET /pico_w/2024-1-24%2013%3A26%3A7?address=chicken_KFC&celsius=28.91698&light=16211 HTTP/1.1" 200 OK
#           
#
#           