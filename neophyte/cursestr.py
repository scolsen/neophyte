import curses
from operator import is_not
from functools import partial

def cursestr(string, style=None):
    return (string, style)

#print(cursestr("test", 0, 0, curses.A_BOLD))

def main(scr):
    curses.use_default_colors()
    scr.clear()
    scr.addstr(10, 10, "Hey\n")
    scr.addstr("Ho")
    scr.refresh()
    scr.getkey()

curses.wrapper(main)
