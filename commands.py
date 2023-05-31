from adafruit_hid.keycode import Keycode

#LIST OF COMMANDS

#Genral Commands
copy = [Keycode.CONTROL, Keycode.C]
paste = [Keycode.CONTROL, Keycode.V]
cancel = [Keycode.ESCAPE, Keycode.ESCAPE]
enter = [Keycode.ENTER]
save = [Keycode.CONTROL, Keycode.S]
delete = [Keycode.DELETE]

#AutoCAD Specific
arc = [Keycode.ESCAPE, Keycode.ESCAPE, "ARC", Keycode.ENTER]
spline = [Keycode.ESCAPE, Keycode.ESCAPE, "SPLINE", Keycode.ENTER]
pline = [Keycode.ESCAPE, Keycode.ESCAPE, "PLINE", Keycode.ENTER]
layer_make_current = [Keycode.ESCAPE, Keycode.ESCAPE, "LAYMCUR", Keycode.ENTER]
acad_copy = ["COPY", Keycode.ENTER]
acad_move = ["MOVE", Keycode.ENTER]
regen = [Keycode.ESCAPE, Keycode.ESCAPE, "REGEN", Keycode.ENTER]
osnap = [Keycode.F3]
ortho = [Keycode.F8]
match_properties = [Keycode.ESCAPE, Keycode.ESCAPE, "MATCHPROP", Keycode.ENTER]
extend = [Keycode.ESCAPE, Keycode.ESCAPE, "EXTEND", Keycode.ENTER]
trim = [Keycode.ESCAPE, Keycode.ESCAPE, "TRIM", Keycode.ENTER, Keycode.ENTER]
extend = [Keycode.ESCAPE, Keycode.ESCAPE, "EXTEND", Keycode.ENTER, Keycode.ENTER]
