from machine import Pin
import time

led = Pin(16, Pin.OUT)

while True:
	led.value(0)
	time.sleep(0.5)
	led.value(1)
	time.sleep(0.5)
