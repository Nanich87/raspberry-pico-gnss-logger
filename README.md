# Raspberry Pico GNSS Logger

[ESP32-CAM GNSS Logger](https://github.com/Nanich87/esp32-cam-gnss-logger)

## Parts

### Raspberry Pi Pico without Headers

![Raspberry Pi Pico without Headers](https://github.com/Nanich87/raspberry-pico-gnss-logger/blob/main/raspberry-pico.jpg "Raspberry Pi Pico without Headers")

![Raspberry Pi Pico Pinout](https://github.com/Nanich87/raspberry-pico-gnss-logger/blob/main/Pico-R3-SDK11-Pinout.svg"Raspberry Pi Pico Pinout")

### ZED-F9P RTK InCase PIN GNSS receiver board with UF.L (IPEX) Base or Rover

![u-blox ZED-F9P](https://github.com/Nanich87/raspberry-pico-gnss-logger/blob/main/u-blox-zed-f9p.jpg "ZED-F9P RTK InCase PIN GNSS receiver board with UF.L (IPEX) Base or Rover")

### High Performance Multi band GNSS Active Quad Helix Antenna FOR RTK

![Quad Helix Antenna](https://github.com/Nanich87/raspberry-pico-gnss-logger/blob/main/antenna.jpg "High Performance Multi band GNSS Active Quad Helix Antenna FOR RTK")

### IPEX (UF.L) to SMA cable

![IPEX (UF.L) to SMA cable](https://github.com/Nanich87/raspberry-pico-gnss-logger/blob/main/ipex-to-sma-cable.jpg "IPEX (UF.L) to SMA cable")

### MicroSD Card Adapter

![MicroSD Card Adapter](https://github.com/Nanich87/raspberry-pico-gnss-logger/blob/main/micro-sd-card-adapter.webp "MicroSD Card Adapter")

### MicroSD Card

## Wiring

### ZED-F9P to Raspberry Pi Pico

* RX -> GP4 (optional)
* TX -> GP5

### MicroSD Card Adapter to Raspberry Pi Pico

* CS -> GP13
* SCK -> GP10
* MOSI -> GP11
* MISO -> GP12
* VCC -> VBUS
* GND -> GND

### Button to Raspberry Pi Pico

* GP3
* GND
