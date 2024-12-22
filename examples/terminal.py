import sys
import tty
import termios

from dfrgblcdpy import DFRRGBLCDPY


def getc() -> str:
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


lcd = DFRRGBLCDPY()
lcd.set_color_white()
lcd.cursor()
row = 0

print("Type text which will appear on your LCD... (CTRL+C to exit)")
while 1:
    ch = getc()
    if ord(ch) == 3:
        break
    if ord(ch) == 13:
        print()
        row += 1
        lcd.set_cursor(0, row % 2)
    else:
        print(ch, end="", flush=True)
        lcd.print_out(ch)

lcd.no_display()
