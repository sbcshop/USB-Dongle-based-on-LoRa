#Transmiter code
import time
from machine import Pin


button1 = Pin(2, Pin.IN, Pin.PULL_UP) # assign button to GP2Pin
button2 = Pin(3, Pin.IN, Pin.PULL_UP)

        
while 1:
    val1 = button1.value()
    val2 = button2.value()
    print("val1 = ",val1)
    print("val2 = ",val2)
    time.sleep(0.2)


