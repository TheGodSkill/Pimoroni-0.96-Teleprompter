# Teleprompter with the 0.96" Display Breakout from Pimoroni
This project is about building a teleprompter using a Pimoroni 0.96" display. With this teleprompter, you can easily read your scripts while recording videos or giving speeches without having to memorize everything.
The Teleprompter.py is a normal Teleprompter and the telepromptermirror.py is simliar but it mirrors the image for the use for smart glasses.

Requirements
- Raspberry Pi (any model (this was designed for the Raspberry Pi Zero W)
- Pimoroni 0.96" display
- Jumper wires (female to female)
- Power supply (USB power bank or wall adapter)
- USB keyboard and mouse


Installation
Connect the Pimoroni display to the Raspberry Pi using the jumper wires. Refer to the Pimoroni website for instructions on how to connect the display.


## Here's which pins to connect between your 0.96" LCD Breakout and your Pi's GPIO (note that it's BCM pin numbering):

- 3-5V to any 5V or 3V pin
- CS to BCM 7
- SCK to BCM 11
- MOSI to BCM 10
- DC to BCM 9
- BL to BCM 19
- GND to any ground pin

Turn on the Raspberry Pi and log in using the USB keyboard and mouse.

## Open the terminal and enter the following commands:
```sudo apt-get update```
```pip install Pillow```
```sudo apt install python3-rpi.gpio python3-spidev python3-pip python3-pil python3-numpy```
```sudo apt install ST7735```

## Run the program 
```python telepromptermirror.py```
```python teleprompter.py```
