class Timeline:
    def __init__(self, log, start, end):
        self.__data = list()
        while True:
            record = log.next()
            if record.empty():
                break
            date = record.date()
            if (start == 0 and end == 0) or start <= date <= end:
                self.__data.append(record)

    def flow(self):
        f = 0
        for r in self.__data:
            f += r.body_bytes_sent
        return f

    def methods(self):
        kinds = ["POST", "GET", "PUT", "DELETE",
                 "OPTIONS", "HEAD", "TRACE", "CONNECT"]
        m = {}
        for method in kinds:
            m[method] = 1

        for r in self.__data:
            m[r.method()] += 1
        return m

    def status(self):
        m = {}
        for r in self.__data:
            if m.get(r.status) is not None:
                m[r.status] += 1
            else:
                m[r.status] = 1
        return m

    def agents(self):
        m = {
            "browser": {},
            "os": {},
            "device": {}
        }
        for r in self.__data:
            ua = r.useragent()
            if m["browser"].get(ua.browser) is None:
                m["browser"][ua.browser] = 0

            if m["os"].get(ua.os) is None:
                m["os"][ua.os] = 0

            if m["device"].get(ua.device) is None:
                m["device"][ua.device] = 0

            m["browser"][ua.browser] += 1
            m["os"][ua.os] += 1
            m["device"][ua.device] += 1
        return m