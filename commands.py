from adafruit_hid.keycode import Keycode

#LIST OF COMMANDS

#Genral Commands
copy = [Keycode.CONTROL, Keycode.C]
paste = [Keycode.CONTROL, Keycode.V]
cancel = [Keycode.ESCAPE, Keycode.ESCAPE]
enter = [Keycode.ENTER]

#AutoCAD Specific
arc = [Keycode.ESCAPE, Keycode.ESCAPE, "ARC", Keycode.ENTER]
spline = [Keycode.ESCAPE, Keycode.ESCAPE, "SPLINE", Keycode.ENTER]
pline = [Keycode.ESCAPE, Keycode.ESCAPE, "PLINE", Keycode.ENTER]
layer_make_current = [Keycode.ESCAPE, Keycode.ESCAPE, "SPLINE", Keycode.ENTER]
acad_copy = ["COPY", Keycode.ENTER]
acad_move = ["MOVE", Keycode.ENTER]
regen = ["REGEN", Keycode.ENTER]