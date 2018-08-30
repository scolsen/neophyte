import codeset, menu, curses
from position import *

class screen: 
    def __init__(self, f):
        self.curse = self.wrapper(f)

    def wait(self, codes):
        while True:
            ch = self.curse.getch()
            match = codes.match(ch)
            if match[0]:
                break
        return match[1]

    def display(self, curse_strs):
        for curse_str in curse_strs:
            self.curse.addstr(*curse_str)
            self.curse.refresh()

    def select(self, m):
        self.display(m.strings())
        return self.wait(m.codes())
   
    def wrapper(self, func, *args, **kwds):
        res = None
        try:
            self.curse=curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.curse.keypad(1)
            try:
                curses.start_color()
            except:
                pass

            return func(self, *args, **kwds)
        
        finally:
            self.curse.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin() 
