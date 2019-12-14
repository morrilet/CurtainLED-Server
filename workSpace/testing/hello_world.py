import time
from machine import Pin

pin = Pin(2, Pin.OUT)
pin.off()

time.sleep(5)

pin.on()
