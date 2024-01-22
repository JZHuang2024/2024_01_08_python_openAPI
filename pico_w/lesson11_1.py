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






