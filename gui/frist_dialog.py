from PyQt5.QtWidgets import *
from gui.ui.ui_loader import Ui_FirstDialog


class FirstDialog(QDialog):
    def __init__(self, parent=None):
        super(FirstDialog, self).__init__(parent)

        self.__log_path = ""

        self.ui = Ui_FirstDialog()
        self.ui.setupUi(self)
        self.ui.button_confirm.clicked.connect(self.on_submit)
        self.ui.button_select.clicked.connect(self.on_select)

    def get_log_path(self):
        return self.__log_path

    def on_select(self):
        selector = QFileDialog()
        file, f = selector.getOpenFileName(self, 'select a log file')
        self.ui.lineEdit.setText(file)

    def on_submit(self):
        self.__log_path = self.ui.lineEdit.text()
        self.accept()