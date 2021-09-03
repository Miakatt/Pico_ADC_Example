import machine
from machine import Pin
import utime
adc = machine.ADC(26)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    print(adc.read_u16())
    utime.sleep(0.02)
    
          
          