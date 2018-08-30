"""
Functions for dealing with key code sets.
Iterable.
"""
from typing import Dict, List

class codeset:
    def __init__(self, chs):
        self.codes = {ord(str(ch)) for ch in chs}
    
    def __iter__(self):
        self._codes = iter(self.codes)
        return self

    def __next__(self):
        try:
            return next(self._codes)
        except StopIteration:
            raise StopIteration

    def match(self, code):
        if code in self.codes:
            return (True, chr(code))
        else:
            return (False, chr(code))
