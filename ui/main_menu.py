# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui',
# licensing of 'main_menu.ui' applies.
#
# Created: Sun May 24 13:06:38 2020
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 187)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../graphics/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.new_trainer = QtWidgets.QPushButton(self.centralwidget)
        self.new_trainer.setGeometry(QtCore.QRect(0, 0, 111, 23))
        self.new_trainer.setObjectName("new_trainer")
        self.localhost = QtWidgets.QPushButton(self.centralwidget)
        self.localhost.setGeometry(QtCore.QRect(220, 0, 111, 23))
        self.localhost.setObjectName("localhost")
        self.pvp = QtWidgets.QPushButton(self.centralwidget)
        self.pvp.setGeometry(QtCore.QRect(330, 0, 111, 23))
        self.pvp.setObjectName("pvp")
        self.options = QtWidgets.QPushButton(self.centralwidget)
        self.options.setGeometry(QtCore.QRect(440, 0, 111, 23))
        self.options.setObjectName("options")
        self.credits = QtWidgets.QPushButton(self.centralwidget)
        self.credits.setGeometry(QtCore.QRect(550, 0, 111, 23))
        self.credits.setObjectName("credits")
        self.trainer_name = QtWidgets.QLabel(self.centralwidget)
        self.trainer_name.setGeometry(QtCore.QRect(0, 20, 91, 16))
        self.trainer_name.setText("")
        self.trainer_name.setObjectName("trainer_name")
        self.pokemon_1 = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_1.setGeometry(QtCore.QRect(330, 30, 91, 61))
        self.pokemon_1.setText("")
        self.pokemon_1.setObjectName("pokemon_1")
        self.pokemon_2 = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_2.setGeometry(QtCore.QRect(430, 30, 91, 61))
        self.pokemon_2.setText("")
        self.pokemon_2.setObjectName("pokemon_2")
        self.pokemon_4 = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_4.setGeometry(QtCore.QRect(330, 90, 91, 61))
        self.pokemon_4.setText("")
        self.pokemon_4.setObjectName("pokemon_4")
        self.pokemon_5 = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_5.setGeometry(QtCore.QRect(430, 90, 91, 61))
        self.pokemon_5.setText("")
        self.pokemon_5.setObjectName("pokemon_5")
        self.pokemon_3 = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_3.setGeometry(QtCore.QRect(550, 30, 91, 61))
        self.pokemon_3.setText("")
        self.pokemon_3.setObjectName("pokemon_3")
        self.pokemon_6 = QtWidgets.QLabel(self.centralwidget)
        self.pokemon_6.setGeometry(QtCore.QRect(550, 90, 91, 61))
        self.pokemon_6.setText("")
        self.pokemon_6.setObjectName("pokemon_6")
        self.trainer_image = QtWidgets.QLabel(self.centralwidget)
        self.trainer_image.setGeometry(QtCore.QRect(0, 40, 121, 81))
        self.trainer_image.setText("")
        self.trainer_image.setObjectName("trainer_image")
        self.load_trainer = QtWidgets.QPushButton(self.centralwidget)
        self.load_trainer.setGeometry(QtCore.QRect(110, 0, 111, 23))
        self.load_trainer.setObjectName("load_trainer")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Main Menu", None, -1))
        self.new_trainer.setText(QtWidgets.QApplication.translate("MainWindow", "New Trainer", None, -1))
        self.localhost.setText(QtWidgets.QApplication.translate("MainWindow", "Localhost", None, -1))
        self.pvp.setText(QtWidgets.QApplication.translate("MainWindow", "Player Vs Player", None, -1))
        self.options.setText(QtWidgets.QApplication.translate("MainWindow", "Options", None, -1))
        self.credits.setText(QtWidgets.QApplication.translate("MainWindow", "Credits", None, -1))
        self.load_trainer.setText(QtWidgets.QApplication.translate("MainWindow", "Load Trainer", None, -1))

