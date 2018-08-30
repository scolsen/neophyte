import curses

def default_color():
    curses.use_default_colors()

class host:
  
    def __init__(self, f):
        self.wrapper(f)

    def wrapper(self, func, *args, **kwds):
        res = None
        try:
            self.master=curses.initscr()
            curses.noecho()
            curses.cbreak()
            self.master.keypad(1)
            try:
                curses.start_color()
            except:
                pass

            return func(self, *args, **kwds)
        
        finally:
            self.master.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin() 

