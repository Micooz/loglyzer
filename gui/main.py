#! /bin/python

from PyQt5.QtWidgets import *
from gui.frist_dialog import FirstDialog
from gui.main_window import MainWindow


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    dialog = FirstDialog()
    dialog.setModal(True)
    if dialog.exec() == QDialog.Accepted:
        main_window = MainWindow(file=dialog.get_log_path())
        main_window.show()
    else:
        sys.exit(0)
    sys.exit(app.exec_())