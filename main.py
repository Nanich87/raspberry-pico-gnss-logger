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

spi = SPI(1, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
cs = Pin(13)
sd = sdcard.SDCard(spi, cs)
os.mount(sd, SDCARD_MOUNT_PATH)

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