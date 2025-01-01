<a id="dfrgblcdpy"></a>

# dfrgblcdpy

<a id="dfrgblcdpy.DFRRGBLCDPY"></a>

## DFRRGBLCDPY Objects

```python
class DFRRGBLCDPY()
```

This class provides methods to control a DFRobot LCD with RGB backlight and
simlar. See example/ to more details.

<a id="dfrgblcdpy.DFRRGBLCDPY.__init__"></a>

#### \_\_init\_\_

```python
def __init__(i2c_line: int = 1,
             rgb_addr: int = 0x2D,
             lcd_addr: int = 0x3E,
             col: int = 16,
             row: int = 2,
             bus: Any | None = None) -> None
```

Creates an instance of the class.

**Arguments**:

- `i2c_line`: i2c line
- `rgb_addr`: i2c address of RGB backlight
- `lcd_addr`: ic2 address of LCD
- `col`: number of cols
- `row`: number of rows
- `bus`: smbus.SMBus or compatible, None means to create one for `i2c_line`

<a id="dfrgblcdpy.DFRRGBLCDPY.write"></a>

#### write

```python
def write(data: int) -> None
```

Writes one char.

**Arguments**:

- `data`: char to write

<a id="dfrgblcdpy.DFRRGBLCDPY.set_RGB"></a>

#### set\_RGB

```python
def set_RGB(r: int, g: int, b: int) -> None
```

Set backlight colour.

**Arguments**:

- `r`: red component (0-255)
- `g`: green component (0-255)
- `b`: blue component (0-255)

<a id="dfrgblcdpy.DFRRGBLCDPY.set_cursor"></a>

#### set\_cursor

```python
def set_cursor(col: int, row: int) -> None
```

Moves cursor to given position.

**Arguments**:

- `col`: column (0-begin)
- `row`: row (0-first line)

<a id="dfrgblcdpy.DFRRGBLCDPY.clear"></a>

#### clear

```python
def clear() -> None
```

Clears LCD

<a id="dfrgblcdpy.DFRRGBLCDPY.scroll_display_left"></a>

#### scroll\_display\_left

```python
def scroll_display_left() -> None
```

Scrolls left to display

<a id="dfrgblcdpy.DFRRGBLCDPY.scroll_display_right"></a>

#### scroll\_display\_right

```python
def scroll_display_right() -> None
```

Scrolls left to display

<a id="dfrgblcdpy.DFRRGBLCDPY.print_out"></a>

#### print\_out

```python
def print_out(value: Any) -> None
```

Prints values (string or any value which will be converted to string)

**Arguments**:

- `value`: value to print

<a id="dfrgblcdpy.DFRRGBLCDPY.home"></a>

#### home

```python
def home() -> None
```

Moves cursor to position 0,0.
(this _command takes a long time)

<a id="dfrgblcdpy.DFRRGBLCDPY.no_display"></a>

#### no\_display

```python
def no_display() -> None
```

Turns the display off

<a id="dfrgblcdpy.DFRRGBLCDPY.display"></a>

#### display

```python
def display() -> None
```

Turns the display on

<a id="dfrgblcdpy.DFRRGBLCDPY.stop_blink"></a>

#### stop\_blink

```python
def stop_blink() -> None
```

Stops the blinking cursor.

<a id="dfrgblcdpy.DFRRGBLCDPY.blink"></a>

#### blink

```python
def blink() -> None
```

Starts the blinking cursor.

<a id="dfrgblcdpy.DFRRGBLCDPY.no_cursor"></a>

#### no\_cursor

```python
def no_cursor() -> None
```

Hides the cursor.

<a id="dfrgblcdpy.DFRRGBLCDPY.cursor"></a>

#### cursor

```python
def cursor() -> None
```

Shows the cursor.

<a id="dfrgblcdpy.DFRRGBLCDPY.left_to_right"></a>

#### left\_to\_right

```python
def left_to_right() -> None
```

Changes text flow to go from left to right

<a id="dfrgblcdpy.DFRRGBLCDPY.right_to_left"></a>

#### right\_to\_left

```python
def right_to_left() -> None
```

Changes text flow to go from right to left

<a id="dfrgblcdpy.DFRRGBLCDPY.no_autoscroll"></a>

#### no\_autoscroll

```python
def no_autoscroll() -> None
```

Disables autoscroll mode

<a id="dfrgblcdpy.DFRRGBLCDPY.autoscroll"></a>

#### autoscroll

```python
def autoscroll() -> None
```

Enable autoscroll mode, right justify will be enforced

<a id="dfrgblcdpy.DFRRGBLCDPY.custom_symbol"></a>

#### custom\_symbol

```python
def custom_symbol(location: int, charmap: list[int]) -> None
```

Loads custom symbols, see example/symbol.py

**Arguments**:

- `location`: bank 0-7
- `charmap`: bitmaps for char

<a id="dfrgblcdpy.DFRRGBLCDPY.printstr"></a>

#### printstr

```python
def printstr(text: str) -> None
```

Prints string

**Arguments**:

- `text`: text to print

<a id="dfrgblcdpy.DFRRGBLCDPY.set_pwm"></a>

#### set\_pwm

```python
def set_pwm(color: int, pwm: int) -> None
```

Sets backlight colour using direct addresses.

**Arguments**:

- `color`: address of colour
- `pwm`: value of the colour

<a id="dfrgblcdpy.DFRRGBLCDPY.set_color_white"></a>

#### set\_color\_white

```python
def set_color_white() -> None
```

Sets whith backlight colour

<a id="dfrgblcdpy.DFRRGBLCDPY.close_backlight"></a>

#### close\_backlight

```python
def close_backlight() -> None
```

Turns off backlight / sets black backlight colour

