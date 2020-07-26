#!/usr/bin/env python
from ui import main_menu, create_trainer, pvp_menu
from PySide2 import QtWidgets, QtCore, QtGui
import json
import os
import filecmp
from PySide2.QtWidgets import QMessageBox
from battle_system import engine, trainer_data
import time
from pypresence import Presence
import glob
import socket
import math

class pvp_setup(pvp_menu.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(pvp_setup, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.data.clicked.connect(self.data_to_be_sent)
        
    def data_to_be_sent(self):
        HOST = self.ip.text()  # The server's hostname or IP address
        PORT = 65432        # The port used by the server
        player, _blank = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open first json file"), self.tr("trainer_data"), self.tr("json (*.json)"))
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Hello, the ip is: " + HOST)
            print("Now loading game...")
            data = s.recv(1024)
            # Hides the window
            self.hide()
            engine.server_host_play(player)
            
class trainer_creator(create_trainer.Ui_mainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(trainer_creator, self).__init__()
        self.setupUi(self)
        self.save.clicked.connect(self.save_data)
        self.pokemon1_combo.setCurrentIndex(-1)
        self.pokemon2_combo.setCurrentIndex(-1)
        self.pokemon3_combo.setCurrentIndex(-1)
        self.pokemon4_combo.setCurrentIndex(-1)
        self.pokemon5_combo.setCurrentIndex(-1)
        self.pokemon6_combo.setCurrentIndex(-1)
        self.setWindowIcon(QtGui.QIcon('graphics/icon.png'))
        
        # Loops through the pokemon list to parse the contents
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
            # Loops to grab the data from the JSON objects
            for i in dataBox["Name"]:
                self.pokemon1_combo.addItem(i)
                self.pokemon2_combo.addItem(i)
                self.pokemon3_combo.addItem(i)
                self.pokemon4_combo.addItem(i)
                self.pokemon5_combo.addItem(i)
                self.pokemon6_combo.addItem(i)
           
        self.pokemon1_combo.currentTextChanged.connect(self.add_moves_pokemon1)
        self.pokemon2_combo.currentTextChanged.connect(self.add_moves_pokemon2)
        self.pokemon3_combo.currentTextChanged.connect(self.add_moves_pokemon3)
        self.pokemon4_combo.currentTextChanged.connect(self.add_moves_pokemon4)
        self.pokemon5_combo.currentTextChanged.connect(self.add_moves_pokemon5)
        self.pokemon6_combo.currentTextChanged.connect(self.add_moves_pokemon6)

    # Saves data based upon user's input into a json file
    def save_data(self):
        trainer_data.pokemon_json_data(self)
        self.hide()
        main_window = main_menu()
        main_window.show()
        main_window.exec_()
        main_window.setWindowModality(QtCore.Qt.WindowModal)
        
    def add_moves_pokemon1(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("assets/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

                    pokemon1_image_file = mon_file["Resource_data"]["Image_dir"]
                    pokemon1_image_path = os.path.dirname(pokemon1_image_file)
                    self.pokemon1_image.setPixmap(os.path.join(pokemon1_image_path, i + "_front.png"))
                    for j in mon_file["Moves"]:
                        self.pokemon1_move1.addItem(j)
                        self.pokemon1_move2.addItem(j)
                        self.pokemon1_move3.addItem(j)
                        self.pokemon1_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon1_item.addItem(k)
    
    def add_moves_pokemon2(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("assets/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)
                    pokemon2_image_file = mon_file["Resource_data"]["Image_dir"]
                    pokemon2_image_path = os.path.dirname(pokemon2_image_file)
                    self.pokemon2_image.setPixmap(os.path.join(pokemon2_image_path, i + "_front.png"))
                    for j in mon_file["Moves"]:
                        self.pokemon2_move1.addItem(j)
                        self.pokemon2_move2.addItem(j)
                        self.pokemon2_move3.addItem(j)
                        self.pokemon2_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon2_item.addItem(k)

    def add_moves_pokemon3(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("assets/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)
                    pokemon3_image_file = mon_file["Resource_data"]["Image_dir"]
                    pokemon3_image_path = os.path.dirname(pokemon3_image_file)
                    self.pokemon3_image.setPixmap(os.path.join(pokemon3_image_path, i + "_front.png"))
                    for j in mon_file["Moves"]:
                        self.pokemon3_move1.addItem(j)
                        self.pokemon3_move2.addItem(j)
                        self.pokemon3_move3.addItem(j)
                        self.pokemon3_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon3_item.addItem(k)

    def add_moves_pokemon4(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("assets/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)
                    pokemon4_image_file = mon_file["Resource_data"]["Image_dir"]
                    pokemon4_image_path = os.path.dirname(pokemon4_image_file)
                    self.pokemon4_image.setPixmap(os.path.join(pokemon4_image_path, i + "_front.png"))
                    for j in mon_file["Moves"]:
                        self.pokemon4_move1.addItem(j)
                        self.pokemon4_move2.addItem(j)
                        self.pokemon4_move3.addItem(j)
                        self.pokemon4_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon4_item.addItem(k)

    def add_moves_pokemon5(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("assets/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)
                    pokemon5_image_file = mon_file["Resource_data"]["Image_dir"]
                    pokemon5_image_path = os.path.dirname(pokemon5_image_file)
                    self.pokemon5_image.setPixmap(os.path.join(pokemon5_image_path, i + "_front.png"))
                    for j in mon_file["Moves"]:
                        self.pokemon5_move1.addItem(j)
                        self.pokemon5_move2.addItem(j)
                        self.pokemon5_move3.addItem(j)
                        self.pokemon5_move4.addItem(j)

                    for k in mon_file["Items"]:
                        self.pokemon5_item.addItem(k)

    def add_moves_pokemon6(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("assets/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)
                    pokemon6_image_file = mon_file["Resource_data"]["Image_dir"]
                    pokemon6_image_path = os.path.dirname(pokemon6_image_file)
                    self.pokemon6_image.setPixmap(os.path.join(pokemon6_image_path, i + "_front.png"))
                    for j in mon_file["Moves"]:
                        self.pokemon6_move1.addItem(j)
                        self.pokemon6_move2.addItem(j)
                        self.pokemon6_move3.addItem(j)
                        self.pokemon6_move4.addItem(j)

                    for k in mon_file["Items"]:
                        self.pokemon6_item.addItem(k)

class main_menu(main_menu.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(main_menu, self).__init__()
        self.setupUi(self)
        self.new_trainer.clicked.connect(self.new_trainer_creator)
        self.setWindowIcon(QtGui.QIcon('graphics/icon.png'))
        self.localhost.clicked.connect(self.localhost_option)
        self.load_trainer.clicked.connect(self.load_trainer_data)
        self.pvp.clicked.connect(self.player_vs_player)
        # Grabs all the files that are in trainer_data that are json files
        list_of_files = glob.glob('trainer_data/*.json') 
        # Grabs the one with the latest updates and saves it to the launcher
        try:
            newest = max(list_of_files, key = os.path.getctime)
            with open(newest, "r") as loop:
                dataBox = json.load(loop)

            self.trainer_name.setText(dataBox["Name"])
            self.trainer_image.setPixmap(dataBox["Image_url"])
            pokemon1_data = dataBox["Pokemon1_Stats"][0]
            with open("assets/pokemon_data/" + pokemon1_data + ".json", "r") as loop:
                        mon_file = json.load(loop)

            pokemon1_icon = mon_file["Resource_data"]["Image_dir"]
            pokemon1_icon_path = os.path.dirname(pokemon1_icon)
            self.pokemon_1.setPixmap(os.path.join(pokemon1_icon_path, 'icon.png'))

            pokemon2_data = dataBox["Pokemon2_Stats"][0]
            with open("assets/pokemon_data/" + pokemon2_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon2_icon = mon_file["Resource_data"]["Image_dir"]
            pokemon2_icon_path = os.path.dirname(pokemon2_icon)
            self.pokemon_2.setPixmap(os.path.join(pokemon2_icon_path, 'icon.png'))

            pokemon3_data = dataBox["Pokemon3_Stats"][0]
            with open("assets/pokemon_data/" + pokemon3_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon3_icon = mon_file["Resource_data"]["Image_dir"]
            pokemon3_icon_path = os.path.dirname(pokemon3_icon)
            self.pokemon_3.setPixmap(os.path.join(pokemon3_icon_path, 'icon.png'))

            pokemon4_data = dataBox["Pokemon4_Stats"][0]
            with open("assets/pokemon_data/" + pokemon4_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon4_icon = mon_file["Resource_data"]["Image_dir"]
            pokemon4_icon_path = os.path.dirname(pokemon4_icon)
            self.pokemon_4.setPixmap(os.path.join(pokemon4_icon_path, 'icon.png'))

            pokemon5_data = dataBox["Pokemon5_Stats"][0]
            with open("assets/pokemon_data/" + pokemon5_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon5_icon = mon_file["Resource_data"]["Image_dir"]
            pokemon5_icon_path = os.path.dirname(pokemon5_icon)
            self.pokemon_5.setPixmap(os.path.join(pokemon5_icon_path, 'icon.png'))

            pokemon6_data = dataBox["Pokemon6_Stats"][0]
            with open("assets/pokemon_data/" + pokemon6_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            # Allows our icon to be found and displayed
            pokemon6_icon = mon_file["Resource_data"]["Image_dir"]
            pokemon6_icon_path = os.path.dirname(pokemon6_icon)
            self.pokemon_6.setPixmap(os.path.join(pokemon6_icon_path, 'icon.png'))

        except:
            print("No data available...please create a trainer!")
    
    def load_trainer_data(self):
        trainer_file, _blank = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open trainer profile"), self.tr("trainer_data"), self.tr("json (*.json)"))
        with open(trainer_file, "r") as loop:
                dataBox = json.load(loop)
    
        self.trainer_name.setText(dataBox["Name"])
        self.trainer_image.setPixmap(dataBox["Image_url"])
            
        pokemon1_data = dataBox["Pokemon1_Stats"][0]
    
        with open("assets/pokemon_data/" + pokemon1_data + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon1_icon = mon_file["Resource_data"]["Image_dir"]
        pokemon1_icon_path = os.path.dirname(pokemon1_icon)
        self.pokemon_1.setPixmap(os.path.join(pokemon1_icon_path, 'icon.png'))

        pokemon2_data = dataBox["Pokemon2_Stats"][0]
        with open("assets/pokemon_data/" + pokemon2_data + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon2_icon = mon_file["Resource_data"]["Image_dir"]
        pokemon2_icon_path = os.path.dirname(pokemon2_icon)
        self.pokemon_2.setPixmap(os.path.join(pokemon2_icon_path, 'icon.png'))

        pokemon3_data = dataBox["Pokemon3_Stats"][0]
        with open("assets/pokemon_data/" + pokemon3_data + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon3_icon = mon_file["Resource_data"]["Image_dir"]
        pokemon3_icon_path = os.path.dirname(pokemon3_icon)
        self.pokemon_3.setPixmap(os.path.join(pokemon3_icon_path, 'icon.png'))

        pokemon4_data = dataBox["Pokemon4_Stats"][0]
        with open("assets/pokemon_data/" + pokemon4_data + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon4_icon = mon_file["Resource_data"]["Image_dir"]
        pokemon4_icon_path = os.path.dirname(pokemon4_icon)
        self.pokemon_4.setPixmap(os.path.join(pokemon4_icon_path, 'icon.png'))

        pokemon5_data = dataBox["Pokemon5_Stats"][0]
        with open("assets/pokemon_data/" + pokemon5_data + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon5_icon = mon_file["Resource_data"]["Image_dir"]
        pokemon5_icon_path = os.path.dirname(pokemon5_icon)
        self.pokemon_5.setPixmap(os.path.join(pokemon5_icon_path, 'icon.png'))
        
        pokemon6_data = dataBox["Pokemon6_Stats"][0]
        with open("assets/pokemon_data/" + pokemon6_data + ".json", "r") as loop:
                    mon_file = json.load(loop)
        # Allows our icon to be found and displayed
        pokemon6_icon = mon_file["Resource_data"]["Image_dir"]
        pokemon6_icon_path = os.path.dirname(pokemon6_icon)
        self.pokemon_6.setPixmap(os.path.join(pokemon6_icon_path, 'icon.png'))

    # Pops open the window for PVP via networking
    def player_vs_player(self):
        # Hides the window
        self.hide()
        # Opens the window
        trainer = pvp_setup()
        trainer.show()
        trainer.exec_()
        trainer.setWindowModality(QtCore.Qt.WindowModal)

    # Launches local host options
    def localhost_option(self):
        file1, _blank = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open first json file"), self.tr("trainer_data"), self.tr("json (*.json)"))
        file2, _blank = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open second json file"), self.tr("trainer_data"), self.tr("json (*.json)"))
        if filecmp.cmp(file1, file2) == True:
            print("These files are the same, we cannot use them in the battle system unfortuantely.")
        else:
            self.hide()
            engine.local_host_play(file1, file2)
                
    def new_trainer_creator(self):
        # Hides the window
        self.hide()
        # Opens the window
        trainer = trainer_creator()
        trainer.show()
        trainer.exec_()
        trainer.setWindowModality(QtCore.Qt.WindowModal)

if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = main_menu()
    qt_app.show()
    app.exec_()
