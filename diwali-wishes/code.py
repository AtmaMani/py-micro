import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10)
pixels.brightness = 0.01

for i in range(len(pixels)):
    pixels[i] = (255,255,255)
    time.sleep(0.5)

# blank out
pixels.fill((0,0,0))