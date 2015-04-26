# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loader.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FirstDialog(object):
    def setupUi(self, FirstDialog):
        FirstDialog.setObjectName("FirstDialog")
        FirstDialog.resize(450, 75)
        FirstDialog.setMaximumSize(QtCore.QSize(450, 75))
        self.gridLayout = QtWidgets.QGridLayout(FirstDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(FirstDialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(FirstDialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.button_select = QtWidgets.QPushButton(FirstDialog)
        self.button_select.setObjectName("button_select")
        self.horizontalLayout.addWidget(self.button_select)
        self.button_confirm = QtWidgets.QPushButton(FirstDialog)
        self.button_confirm.setObjectName("button_confirm")
        self.horizontalLayout.addWidget(self.button_confirm)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(FirstDialog)
        QtCore.QMetaObject.connectSlotsByName(FirstDialog)

    def retranslateUi(self, FirstDialog):
        _translate = QtCore.QCoreApplication.translate
        FirstDialog.setWindowTitle(_translate("FirstDialog", "Select a log file"))
        self.label.setText(_translate("FirstDialog", "The log file: "))
        self.button_select.setText(_translate("FirstDialog", "Select"))
        self.button_confirm.setText(_translate("FirstDialog", "Confirm"))

