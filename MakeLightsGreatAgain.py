import time
#import board
#import neopixel
maxLights = 50
#pixels = neopixel.NeoPixel(board.D18, maxLights, brightness=1,pixel_order=neopixel.RGB)
maxLoops = 2

def updateLights():
    #pixels.show()
    #pixels.write()
    print("Updating Lights")

def ledOn():
    #pixels.fill((255,255,255))
    updateLights()
    print("All LEDs On")

def ledOff():
    #pixels.fill((0,0,0))
    updateLights()
    print("All LEDs Off")

def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b)


def rainbowCycle(wait):
    for i in range(maxLights):
        pixelIndex = (i * 256 // maxLights) + i
        output = wheel(pixelIndex & 255)
        print("Light number", i, "is showing the colour", output)
        updateLights()
        time.sleep(wait)

for counter in range(maxLoops):
    ledOff()
    time.sleep(1)
    ledOn()
    time.sleep(1)
    ledOff()
    rainbowCycle(0.25)
ledOff()