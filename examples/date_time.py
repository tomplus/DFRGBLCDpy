from datetime import datetime
import time
from dfrgblcdpy import DFRRGBLCDPY

# default addresses
lcd = DFRRGBLCDPY()

# set green backlight
lcd.set_RGB(0, 255, 0)

baner = False

while 1:
    now = datetime.now()
    lcd.print_out("Date: " + now.strftime("%Y.%m.%d"))
    lcd.set_cursor(0, 1)
    lcd.print_out("Time: " + now.strftime("%H:%M:%S.%f"))

    if not baner:
        print("Current date and time is shown on the LCD, CTRL+C to break")
        baner = True

    try:
        time.sleep(0.05)
    except KeyboardInterrupt:
        break

# black backlight / turn off
lcd.close_backlight(0)
