"""
Uri

provide Urldecoding
"""

from urllib import parse


class Uri:
    def __init__(self, uristr):
        self.origin = uristr
        self.uri = parse.unquote(uristr)
        pass

    def __str__(self):
        return self.origin

    def to_string(self):
        return self.uri