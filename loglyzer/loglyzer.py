import gzip
import linecache

from loglyzer.record import Record
from loglyzer.timeline import Timeline


class Loglyzer:
    def __init__(self):
        self.__nextcur = 0
        self.file_handler_ = None
        self.file_name = ""

    def __del__(self):
        if self.file_handler_ is not None:
            self.file_handler_.close()

    @staticmethod
    def __parse(line):
        line = line[:-1]
        block = ""
        protected = False
        fields = list()

        for char in line:
            if char in ['[', ']', '"']:
                protected = not protected
            elif char == ' ' and not protected:
                fields.append(block)
                block = ""
            else:
                block += char
        fields.append(block)

        r = Record()
        if len(fields) >= 8:
            r.remote_addr = fields[0]
            r.delimeter = fields[1]
            r.remote_user = fields[2]
            r.time_local = fields[3]
            r.request = fields[4]
            r.status = int(fields[5])
            r.body_bytes_sent = int(fields[6])
            r.http_referer = fields[7]
            r.http_user_agent = fields[8].strip()
        else:
            r.set_empty()

        fields.clear()
        return r

    def load(self, file):
        if file.endswith("gz"):
            self.file_handler_ = gzip.open(file, mode='rt')
        else:
            self.file_handler_ = open(file, mode='rt')
        self.file_name = file

    def next(self):
        self.file_handler_.seek(self.__nextcur)
        line = self.file_handler_.readline()
        self.__nextcur = self.file_handler_.tell()
        return self.__parse(line)

    def at(self, lineno):
        line = linecache.getline(self.file_name, lineno)
        return self.__parse(line)

    def duration(self, start, end):
        self.file_handler_.seek(0)
        return Timeline(self, start, end)

    def all(self):
        self.file_handler_.seek(0)
        return Timeline(self, 0, 0)