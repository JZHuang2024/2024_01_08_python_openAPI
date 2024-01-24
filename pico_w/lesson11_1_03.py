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

#from machine import Pin
#
#red_led = Pin(15,mode=Pin.OUT)
#red_led.value(1)
#red_led.value(0)




#from machine import Pin
#import time

#red_led = Pin(15,mode=Pin.OUT)
#btn = Pin(14,mode=Pin.PULL_DOWN)

#while True:
#    if btn.value():
#        red_led.value(1)
#    else:
#        red_led.value(0)




from machine import Pin
import time

red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)
is_press = False

while True:
    if btn.value():
        is_press = True
        red_led.value(1)
    else:
        if is_press == True:
            print('release')
            is_press = False
        red_led.value(0)






