from dfrgblcdpy import DFRRGBLCDPY


heart = [0b00000, 0b01010, 0b11111, 0b11111, 0b11111, 0b01110, 0b00100, 0b00000]

smiley = [0b00000, 0b00000, 0b01010, 0b00000, 0b00000, 0b10001, 0b01110, 0b00000]

lcd = DFRRGBLCDPY()
lcd.custom_symbol(0, heart)
lcd.custom_symbol(1, smiley)
lcd.set_color_white()
lcd.clear()

# lcd.set_cursor(0, 0)
lcd.print_out("I ")
lcd.write(0)
lcd.print_out(" raspberry ")
lcd.write(1)
