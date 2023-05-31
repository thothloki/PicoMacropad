import board
import digitalio
import time
import adafruit_matrixkeypad
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import commands
import autocad

#SET UP GPIO FOR KEYPAD
cols = [digitalio.DigitalInOut(x) for x in (board.GP18, board.GP19, board.GP10, board.GP11)]
rows = [digitalio.DigitalInOut(x) for x in (board.GP13, board.GP12, board.GP20, board.GP21)]
keys = ((1, 2, 3, 4),
        (5, 6, 7, 8),
        (9, 10, 11, 12),
        (13, 14, 15, 16))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

#SET UP GPIO FOR MODE SWITCH

mode1 = autocad

# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)

while True:
    keys = keypad.pressed_keys
    mode = 1
    
    if mode == 1:
        if str(keys) == '[1]':
            mode1.button_1()
        elif str(keys) == '[2]':
            mode1.button_2()
    time.sleep(0.2)
    