from machine import UART, Pin, SPI
import time
import os
import sdcard

SDCARD_MOUNT_PATH = "/sd"
LED_PIN = 25

led = Pin(LED_PIN, Pin.OUT)
spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)

uart = UART(1, baudrate=460800, tx=Pin(4), rx=Pin(5))

os.mount(sd, SDCARD_MOUNT_PATH)

year, month, day, hour, mins, secs, weekday, yearday = time.localtime()
filepath = SDCARD_MOUNT_PATH + "/" + "{}-{:02d}-{:02d}-{:02d}-{:02d}-{:02d}.ubx".format(year, month, day, hour, mins, secs)

with open(filepath, "a") as file:
    while True:
        #led.value(0)
        data = uart.read()
        if data:
            file.write(data)
            #led.value(1)

