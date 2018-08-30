import neophyte
from menu import *

def main(scr):
    neophyte.default_color()
    m = menu("menu1", ["Yes", "No"])
    y = menu("menu2" ,["Either", "Or"])
    m.display(scr)
    y.display(scr)
    scr.curse.getkey() 
    m.hide(scr) 
    scr.curse.getkey()

neophyte.host(main)
