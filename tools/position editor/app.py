# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui',
# licensing of 'app.ui' applies.
#
# Created: Sat Jul 18 13:02:06 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pokemon = QtWidgets.QComboBox(self.centralwidget)
        self.pokemon.setGeometry(QtCore.QRect(0, 0, 141, 22))
        self.pokemon.setObjectName("pokemon")
        self.background_selection = QtWidgets.QComboBox(self.centralwidget)
        self.background_selection.setGeometry(QtCore.QRect(140, 0, 141, 22))
        self.background_selection.setObjectName("background_selection")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 20, 471, 221))
        self.background.setText("")
        self.background.setObjectName("background")
        self.front = QtWidgets.QLabel(self.centralwidget)
        self.front.setGeometry(QtCore.QRect(160, 50, 101, 91))
        self.front.setText("")
        self.front.setObjectName("front")
        self.back = QtWidgets.QLabel(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(0, 140, 101, 61))
        self.back.setText("")
        self.back.setObjectName("back")
        self.front_x = QtWidgets.QLineEdit(self.centralwidget)
        self.front_x.setGeometry(QtCore.QRect(40, 240, 113, 20))
        self.front_x.setObjectName("front_x")
        self.front_y = QtWidgets.QLineEdit(self.centralwidget)
        self.front_y.setGeometry(QtCore.QRect(40, 260, 113, 20))
        self.front_y.setObjectName("front_y")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 240, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 260, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 240, 47, 13))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 260, 47, 13))
        self.label_4.setObjectName("label_4")
        self.back_x = QtWidgets.QLineEdit(self.centralwidget)
        self.back_x.setGeometry(QtCore.QRect(200, 240, 113, 20))
        self.back_x.setObjectName("back_x")
        self.back_y = QtWidgets.QLineEdit(self.centralwidget)
        self.back_y.setGeometry(QtCore.QRect(200, 260, 113, 20))
        self.back_y.setObjectName("back_y")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(120, 280, 75, 23))
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "Front_X", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Front_Y", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Back_X", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Back_Y", None, -1))
        self.save.setText(QtWidgets.QApplication.translate("MainWindow", "Save", None, -1))

