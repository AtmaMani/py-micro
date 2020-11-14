import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.01

while True:
    # animate first 3 led
    for i in range(4):
        pixels[i] = (255,255,255)
        time.sleep(0.15)

    # animate 4 - 10 led faster
    for i in range(4,10):
        pixels[i] = (255,255,255)
        time.sleep(0.1)

    # blank out
    pixels.fill((255,255,255))

    # animate first 3 led
    for i in range(4):
        pixels[i] = (0,0,0)
        time.sleep(0.1)
        pixels.fill((255,255,255))

    # animate 4 - 10 led faster
    for i in range(4,10):
        pixels[i] = (0,0,0)
        time.sleep(0.05)
        pixels.fill((255,255,255))

    for i in range(len(pixels)):
        pixels[i] = (0,0,0)
        time.sleep(0.01)
        pixels.fill((255,255,255))

    for i in range(len(pixels)):
        pixels[i] = (0,0,0)
        time.sleep(0.01)
        pixels.fill((255,255,255))

    for i in range(len(pixels)):
        pixels[i] = (0,0,0)
        time.sleep(0.01)
        pixels.fill((255,255,255))

    for i in range(len(pixels)):
        pixels[i] = (0,0,0)
        time.sleep(0.01)
        pixels.fill((255,255,255))

    for i in range(len(pixels)):
        pixels[i] = (0,0,0)
        time.sleep(0.01)
        pixels.fill((255,255,255))

    pixels.fill((0,0,0))
    time.sleep(0.1)
    pixels.fill((255,0,0))
    time.sleep(0.1)
    pixels.fill((0,0,0))
    time.sleep(0.1)
    pixels.fill((0,255,0))
    time.sleep(0.1)
    pixels.fill((0,0,0))
    time.sleep(0.1)
    pixels.fill((0,0,255))
    time.sleep(0.1)