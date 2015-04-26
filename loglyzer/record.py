"""
Record
"""

from datetime import datetime
from user_agents import parse
from loglyzer.uri import Uri


class Record:
    def __init__(self):
        self.__empty = False
        self.remote_addr = ""
        self.delimeter = '-'
        self.remote_user = ""
        self.time_local = ""
        self.request = ""
        self.status = 0
        self.body_bytes_sent = 0
        self.http_referer = ""
        self.http_user_agent = ""

    def __str__(self):
        return "%s %s %s %s %s %s %s %s" \
               % (self.remote_addr, self.remote_user, self.time_local,
                  self.request, self.status, self.body_bytes_sent,
                  self.http_referer, self.http_user_agent)

    def date(self):
        try:
            dt = datetime.strptime(self.time_local,
                                   "%d/%b/%Y:%H:%M:%S %z")
            return dt
        except ValueError:
            return datetime.now()

    def method(self):
        parts = self.request.split(' ')
        if len(parts) >= 1:
            return parts[0]
        return ""

    def uri(self):
        parts = self.request.split(' ')
        if len(parts) >= 2:
            return Uri(parts[1])
        return Uri("")

    def version(self):
        parts = self.request.split(' ')
        if len(parts) >= 3:
            return parts[2]
        return ""

    def useragent(self):
        return parse(self.http_user_agent)

    def empty(self):
        return self.__empty

    def set_empty(self):
        self.__empty = True