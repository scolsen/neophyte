from codeset import *
from visible import *

class menu(visible):
    def __init__(self, name, options, separator=") "):
        self.name = name
        self.options = {enum[0]:enum[1] for enum in enumerate(options)}
        self.separator = separator
        self.optiter = iter(self.options.items()) 
        self.strings = [str(k) + self.separator + v + "\n" for k, v in self]
    
    def __iter__(self):
        return self

    def __next__(self):
        try:
            return next(self.optiter)
        except StopIteration:
            raise StopIteration
    
    def prefixes(self):
        pass # will need roman-range.
    
    def codes(self):
        return codeset([k for k, v in self])
