from machine import UART, Pin, SPI, RTC
import utime
import os
import sdcard
import _thread

# Config
## GPS
GPS_BAUD_RATE = 460800
GPS_TX = 4
GPS_RX = 5
## SDCARD
SDCARD_SCK = 10
SDCARD_MOSI = 11
SDCARD_MISO = 12
SDCARD_CS = 13
SDCARD_MOUNT_PATH = "/sd"
## Button/LED
BTN_PIN = 3
LED_PIN = 6

# Init
led = Pin(LED_PIN, Pin.OUT)
btn = Pin(BTN_PIN, Pin.IN, Pin.PULL_UP)

spi = SPI(1, sck=Pin(SDCARD_SCK), mosi=Pin(SDCARD_MOSI), miso=Pin(SDCARD_MISO))
sd = sdcard.SDCard(spi, Pin(SDCARD_CS))
os.mount(sd, SDCARD_MOUNT_PATH)

uart = UART(1, baudrate=GPS_BAUD_RATE, tx=Pin(GPS_TX), rx=Pin(GPS_RX))

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
    with open(filepath, "a") as file:
        while True:
            data = uart.read()
            if data:
                file.write(data)
            global running
            if running == False:
                break
            utime.sleep(0.0625)
    led.value(0)

btn.irq(trigger = Pin.IRQ_RISING, handler = toggleLogging)