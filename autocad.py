#THIS IS THE AUTOCAD LAYOUT
from adafruit_hid.keycode import Keycode
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import commands


kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)

button1 = commands.arc
button2 = commands.spline
button3 = commands.pline
button4 = commands.enter
button5 = commands.acad_copy
button6 = commands.acad_move
button7 = commands.regen
#button8 =
#button9 =
#button10 =
#button11 =
#button12 =
#button13 =
#button14 =
#button15 =
#button16 =

def button_1():
    for i in button1:
        if isinstance(i, str):
            keyboard_layout.write(i)
        else:
            kbd.press(i)
        kbd.release_all()


layout = [button1, button2, button3, button4, button5, button6, button7]#, button8, button9, button10, button11, button12, button13, button14, button15, button16]