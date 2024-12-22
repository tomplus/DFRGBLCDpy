from dfrgblcdpy import DFRRGBLCDPY

# default addresses
lcd = DFRRGBLCDPY()

# set white backlight
lcd.set_color_white()

# first line
lcd.print_out("Hello!")

# second line
lcd.set_cursor(0, 1)
lcd.print_out("World!")

print("'Hello! World!' has been printed on LCD")
