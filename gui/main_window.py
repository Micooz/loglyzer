from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *

from gui.ui.ui_main_window import Ui_MainWindow
from loglyzer import Loglyzer


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # setup ui.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # setup table
        columns = ["ip", "time", "method", "uri", "status"]
        self.ui.table.setColumnCount(len(columns))
        self.ui.table.setHorizontalHeaderLabels(columns)
        self.ui.table.horizontalHeader().setStretchLastSection(True)
        self.ui.table.setSortingEnabled(True)
        self.ui.table.verticalHeader().setVisible(False)
        self.ui.table.setAutoScroll(True)
        self.ui.table.itemClicked.connect(self.on_tableitem_selected)
        # setup datetime controls
        self.ui.datetime_start.dateTimeChanged.connect(self.on_datetime_changed)
        self.ui.datetime_end.dateTimeChanged.connect(self.on_datetime_changed)
        # setup frame_details
        self.ui.frame_details.setVisible(False)

        self.log = Loglyzer()
        self.log.load("../test/test.log")
        # load log file
        record = self.log.next()
        index = 0
        while not record.empty():
            self.ui.table.setRowCount(index + 1)
            self.ui.table.setItem(index, 0, QTableWidgetItem(record.remote_addr))
            self.ui.table.setItem(index, 1, QTableWidgetItem(str(record.date())))
            self.ui.table.setItem(index, 2, QTableWidgetItem(record.method()))
            self.ui.table.setItem(index, 3, QTableWidgetItem(record.uri().to_string()))
            self.ui.table.setItem(index, 4, QTableWidgetItem(str(record.status)))
            index += 1
            record = self.log.next()

        self.ui.label_count.setText("Total: %s" % index)
        dt_left = self.log.at(1).date()
        dt_right = self.log.at(index).date()
        self.ui.datetime_start.setDateTimeRange(dt_left, dt_right)
        self.ui.datetime_end.setDateTimeRange(dt_left, dt_right)

        self.summary()

    def summary(self, timeline=None):
        self.ui.text_summary.setPlainText("")
        # init summary
        if timeline is None:
            timeline = self.log.all()
        summary = "[Flow]\n%s bytes\n" % timeline.flow()
        summary += "\n"
        summary += "[Status]\n"
        status = timeline.status()
        for s in status:
            summary += "%s: %s\n" % (s, status[s])
        summary += "\n"
        agents = timeline.agents()
        os = "[OS]\n"
        browsers = "[Browsers]\n"
        for o in agents["os"]:
            family = o.family + " " + o.version_string
            os += "%s: %s\n" % (family, agents["os"][o])
        for o in agents["browser"]:
            family = o.family + " " + o.version_string
            browsers += "%s: %s\n" % (family, agents["browser"][o])
        summary += os
        summary += "\n"
        summary += browsers
        self.ui.text_summary.setPlainText(summary)

    @pyqtSlot(int)
    def on_tableitem_selected(self, item):
        grid = self.ui.table.item
        row = item.row()
        details = "%s@%s\n%s %s %s\n" % (grid(row, 0).text(),
                                         grid(row, 1).text(),
                                         grid(row, 2).text(),
                                         grid(row, 3).text(),
                                         grid(row, 4).text())
        self.ui.text_details.setPlainText(details)
        self.ui.frame_details.setVisible(True)

    @pyqtSlot(int)
    def on_datetime_changed(self, datetime):
        dt_start = self.ui.datetime_start.dateTime()
        dt_end = self.ui.datetime_end.dateTime()
        timeline = self.log.duration(dt_start.toUTC(), dt_end.toUTC())
        self.summary(timeline)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())