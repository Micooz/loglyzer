import unittest

from datetime import datetime
from loglyzer import Loglyzer


class TestLoglyzer(unittest.TestCase):
    def setUp(self):
        unittest.TestCase.__init__(self)
        self.log = Loglyzer()
        self.log.load("test/test.log")

    def test_single_line(self):
        fields = self.log.next()
        self.assertEqual(fields.remote_addr, "180.76.6.57")
        self.assertEqual(fields.delimeter, "-")
        self.assertEqual(fields.time_local, "11/Jan/2015:06:28:03 +0800")
        self.assertEqual(fields.method(), "GET")
        self.assertEqual(fields.uri().to_string(), "/robots.txt")
        self.assertEqual(fields.version(), "HTTP/1.1")
        self.assertEqual(fields.status, 200)
        self.assertEqual(fields.body_bytes_sent, 424)
        self.assertEqual(fields.http_referer, "-")
        self.assertEqual(fields.http_user_agent,
                         "Mozilla/5.0 (Windows NT 5.1; rv:6.0.2) Gecko/20100101 Firefox/6.0.2")
        self.assertEqual(str(fields.date()), "2015-01-11 06:28:03+08:00")
        self.assertEqual(str(self.log.at(10).uri()), "/%7B%7Blink.url%7D%7D")
        self.assertEqual(self.log.at(10).uri().to_string(), "/{{link.url}}")

    def test_statistics(self):
        log = self.log
        tl = log.duration(datetime.strptime("11/Jan/2015:06:28:03 +0800", "%d/%b/%Y:%H:%M:%S %z"),
                          datetime.strptime("11/Jan/2015:08:28:03 +0800", "%d/%b/%Y:%H:%M:%S %z"))
        self.assertEqual(tl.flow(), 58169)
        self.assertEqual(tl.methods()["GET"], 16)
        self.assertEqual(tl.status()[200], 12)
        # print(tl.agents())


if __name__ == '__main__':
    unittest.main()
