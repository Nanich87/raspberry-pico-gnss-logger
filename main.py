from machine import UART, Pin, SPI, RTC
import utime
import os
import sdcard
import _thread

# Config
SDCARD_MOUNT_PATH = "/sd"
LED_PIN = 6
BTN_PIN = 3

# Init
led = Pin(LED_PIN, Pin.OUT)
btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)

#spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
#cs = Pin(13)
#sd = sdcard.SDCard(spi, cs)
#os.mount(sd, SDCARD_MOUNT_PATH)
uart = UART(1, baudrate=38400, tx=Pin(4), rx=Pin(5))

tm2 = bytearray(b'\xB5\x62\x06\x01\x03\x00\x0D\x03\x01\x1B\x6D')
uart.write(tm2)

rawx = bytearray(b'\xB5\x62\x06\x01\x03\x00\x02\x15\x01\x22\x70')
uart.write(rawx)

sfrbx = bytearray(b'\xB5\x62\x06\x01\x03\x00\x02\x13\x01\x20\x6C')
uart.write(sfrbx)

rate = bytearray(b'\xB5\x62\x06\x08\x06\x00\x7D\x00\x01\x00\x01\x00\x93\xA8')
uart.write(rate)

prt = bytearray(b'\xB5\x62\x06\x00\x14\x00\x01\x00\x00\x00\xD0\x08\x00\x00\x00\x08\x07\x00\x23\x00\x23\x00\x00\x00\x00\x00\x48\x5C')
uart.write(prt)

uart = UART(1, baudrate=460800, tx=Pin(4), rx=Pin(5))

lastPressedTime = utime.ticks_ms()
running = False

def toggleLogging(pin):
    global running, lastPressedTime
    if utime.ticks_diff(utime.ticks_ms(), lastPressedTime) > 500:
        lastPressedTime = utime.ticks_ms()
        if running == True:
            running = False
        else:
            running = True
            _thread.start_new_thread(log, ())

def log():
    led.value(1)
    year, month, day, hour, mins, secs, weekday, yearday = utime.localtime()
    filepath = SDCARD_MOUNT_PATH + "/" + "{}-{:02d}-{:02d}-{:02d}-{:02d}-{:02d}.ubx".format(year, month, day, hour, mins, secs)
    #with open(filepath, "a") as file:
    while True:
        data = uart.read()
        if data:
            #file.write(data)
            print(data)
            #utime.sleep(0.125)
        global running
        if running == False:
            break;
    led.value(0)

btn.irq(trigger = Pin.IRQ_RISING, handler = toggleLogging)