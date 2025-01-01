import colorsys
import time

from dfrgblcdpy import DFRRGBLCDPY
from EasyMCP2221 import SMBus

# Use EasyMCP2221 to access your LCD via MCP2221 device
lcd = DFRRGBLCDPY(bus=SMBus())
lcd.autoscroll()

text = "Backlight colour is changing... "
text_pos = 0
lcd.print_out(text)

h = 0
while True:
    color = colorsys.hsv_to_rgb(h / 360.0, 1, 1)
    color = [int(c * 255) for c in color]
    lcd.set_RGB(*color)

    if h % 5 == 0:
        lcd.print_out(text[text_pos % len(text)])
        text_pos += 1

    if h == 0:
        print("Backlight colour is changing, CTRL+C to break")

    try:
        time.sleep(0.1)
    except KeyboardInterrupt:
        break

    h += 1


lcd.close_backlight(0)
lcd.clear()
