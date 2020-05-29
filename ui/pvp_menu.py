# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pvp_menu.ui',
# licensing of 'pvp_menu.ui' applies.
#
# Created: Mon May 25 18:38:04 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(376, 127)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.ip = QtWidgets.QLineEdit(self.centralwidget)
        self.ip.setGeometry(QtCore.QRect(70, 20, 271, 20))
        self.ip.setObjectName("ip")
        self.data = QtWidgets.QPushButton(self.centralwidget)
        self.data.setGeometry(QtCore.QRect(140, 60, 75, 23))
        self.data.setObjectName("data")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 376, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Pvp menu", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "IP address", None, -1))
        self.data.setText(QtWidgets.QApplication.translate("MainWindow", "Connect", None, -1))

