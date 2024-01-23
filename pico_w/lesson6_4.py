from machine import Pin,Timer

led25 = Pin("LED",Pin.OUT)

def second1(t):
    print("過1秒")
    led25.toggle()
    
tim1 = Timer()
tim1.init(period=1000, callback=second1)