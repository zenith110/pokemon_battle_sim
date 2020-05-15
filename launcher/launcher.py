#!/usr/bin/env python
from ui import main_menu, create_trainer
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtMultimedia import QSound
from playsound import playsound
import json
import os
class trainer_creator(create_trainer.Ui_MainWindow, QtWidgets.QMainWindow):
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
        # Loops through the pokemon list to parse the contents
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
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
    def save_data(self):
        name = self.name.text()
        image, _blank = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open trainer sprite"), self.tr("../battle_system/battlecode/assets/graphics/trainer_sprite"), self.tr("Image (*.png)"))
        
        pokemon1_name = self.pokemon1_combo.currentText()
        pokemon1_move1 = self.pokemon1_move1.currentText()
        pokemon1_move2 = self.pokemon1_move2.currentText()
        pokemon1_move3 = self.pokemon1_move3.currentText()
        pokemon1_move4 = self.pokemon1_move4.currentText()
        pokemon1_level = self.pokemon1_level.value()
        pokemon1_item = self.pokemon1_item.currentText()

        pokemon2_name = self.pokemon2_combo.currentText()
        pokemon2_move1 = self.pokemon2_move1.currentText()
        pokemon2_move2 = self.pokemon2_move2.currentText()
        pokemon2_move3 = self.pokemon2_move3.currentText()
        pokemon2_move4 = self.pokemon2_move4.currentText()
        pokemon2_level = self.pokemon2_level.value()
        pokemon2_item = self.pokemon2_item.currentText()


        pokemon3_name = self.pokemon3_combo.currentText()
        pokemon3_move1 = self.pokemon3_move1.currentText()
        pokemon3_move2 = self.pokemon3_move2.currentText()
        pokemon3_move3 = self.pokemon3_move3.currentText()
        pokemon3_move4 = self.pokemon3_move4.currentText()
        pokemon3_level = self.pokemon3_level.value()
        pokemon3_item = self.pokemon3_item.currentText()

        pokemon4_name = self.pokemon4_combo.currentText()
        pokemon4_move1 = self.pokemon4_move1.currentText()
        pokemon4_move2 = self.pokemon4_move2.currentText()
        pokemon4_move3 = self.pokemon4_move3.currentText()
        pokemon4_move4 = self.pokemon4_move4.currentText()
        pokemon4_level = self.pokemon4_level.value()
        pokemon4_item = self.pokemon4_item.currentText()

        pokemon5_name = self.pokemon5_combo.currentText()
        pokemon5_move1 = self.pokemon5_move1.currentText()
        pokemon5_move2 = self.pokemon5_move2.currentText()
        pokemon5_move3 = self.pokemon5_move3.currentText()
        pokemon5_move4 = self.pokemon5_move4.currentText()
        pokemon5_level = self.pokemon5_level.value()
        pokemon5_item = self.pokemon5_item.currentText()

        pokemon6_name = self.pokemon6_combo.currentText()
        pokemon6_move1 = self.pokemon6_move1.currentText()
        pokemon6_move2 = self.pokemon6_move2.currentText()
        pokemon6_move3 = self.pokemon6_move3.currentText()
        pokemon6_move4 = self.pokemon6_move4.currentText()
        pokemon6_level = self.pokemon6_level.value()
        pokemon6_item = self.pokemon6_item.currentText()

        data = {}
        data["Name"] = name
        data["Image_url"] = image
        data["Time_Spent"] =  "0"
        data["Pokemon1"] = [pokemon1_name, pokemon1_move1, pokemon1_move2, pokemon1_move3, pokemon1_move4, pokemon1_level, pokemon1_item]
        data["Pokemon2"] = [pokemon2_name, pokemon2_move1, pokemon2_move2, pokemon2_move3, pokemon2_move4, pokemon2_level, pokemon2_item]
        data["Pokemon3"] = [pokemon3_name, pokemon3_move1, pokemon3_move2, pokemon3_move3, pokemon3_move4, pokemon3_level, pokemon3_item]
        data["Pokemon4"] = [pokemon4_name, pokemon4_move1, pokemon4_move2, pokemon4_move3, pokemon4_move4, pokemon4_level, pokemon4_item]
        data["Pokemon5"] = [pokemon5_name, pokemon5_move1, pokemon5_move2, pokemon5_move3, pokemon5_move4, pokemon5_level, pokemon5_item]
        data["Pokemon6"] = [pokemon6_name, pokemon6_move1, pokemon6_move2, pokemon6_move3, pokemon6_move4, pokemon6_level, pokemon6_item]
        
        
        file = open("/trainer_data/" + name + ".json", "w")

        # Dumps the data to the file
        json.dump(data, file, indent = 1)
        file.close()
       
        self.hide()
        main_window = main_menu()
        main_window.show()
        main_window.exec_()
        main_window.setWindowModality(QtCore.Qt.WindowModal)
        
    def add_moves_pokemon1(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("../battle_system/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

                    for j in mon_file["Moves"]:
                        self.pokemon1_move1.addItem(j)
                        self.pokemon1_move2.addItem(j)
                        self.pokemon1_move3.addItem(j)
                        self.pokemon1_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon1_item.addItem(k)
    def add_moves_pokemon2(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("../battle_system/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

                    for j in mon_file["Moves"]:
                        self.pokemon2_move1.addItem(j)
                        self.pokemon2_move2.addItem(j)
                        self.pokemon2_move3.addItem(j)
                        self.pokemon2_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon2_item.addItem(k)
    def add_moves_pokemon3(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("../battle_system/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

                    for j in mon_file["Moves"]:
                        self.pokemon3_move1.addItem(j)
                        self.pokemon3_move2.addItem(j)
                        self.pokemon3_move3.addItem(j)
                        self.pokemon3_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon3_item.addItem(k)
    def add_moves_pokemon4(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("../battle_system/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

                    for j in mon_file["Moves"]:
                        self.pokemon4_move1.addItem(j)
                        self.pokemon4_move2.addItem(j)
                        self.pokemon4_move3.addItem(j)
                        self.pokemon4_move4.addItem(j)
                    
                    for k in mon_file["Items"]:
                        self.pokemon4_item.addItem(k)
    def add_moves_pokemon5(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("../battle_system/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

                    for j in mon_file["Moves"]:
                        self.pokemon5_move1.addItem(j)
                        self.pokemon5_move2.addItem(j)
                        self.pokemon5_move3.addItem(j)
                        self.pokemon5_move4.addItem(j)

                    for k in mon_file["Items"]:
                        self.pokemon5_item.addItem(k)
    def add_moves_pokemon6(self, index):
        # Opens json file so we can match the pokemon name and parse that pokemon file
        with open("../battle_system/pokemon_data/list_of_pokemon.json", "r") as loop:
            dataBox = json.load(loop)
        for i in dataBox["Name"]:
            # Checks if index matches the name, then opens up the file
            if index == i:
                with open("../battle_system/pokemon_data/" + i + ".json", "r") as loop:
                    mon_file = json.load(loop)

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
        try:
            with open("trainer_data/aaa.json", "r") as loop:
                dataBox = json.load(loop)
        
            self.trainer_name.setText(dataBox["Name"])
            self.trainer_image.setPixmap(dataBox["Image_url"])
            
            pokemon1_data = dataBox["Pokemon1"][0]
            with open("../battle_system/pokemon_data/" + pokemon1_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon1_icon = mon_file["Graphics"]["Front_Sprite"]
            self.pokemon_1.setPixmap(pokemon1_icon)

            pokemon2_data = dataBox["Pokemon2"][0]
            with open("../battle_system/pokemon_data/" + pokemon2_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon2_icon = mon_file["Graphics"]["Front_Sprite"]
            self.pokemon_2.setPixmap(pokemon2_icon)

            pokemon3_data = dataBox["Pokemon3"][0]
            with open("../battle_system/pokemon_data/" + pokemon3_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon3_icon = mon_file["Graphics"]["Front_Sprite"]
            self.pokemon_3.setPixmap(pokemon3_icon)

            pokemon4_data = dataBox["Pokemon4"][0]
            with open("../battle_system/pokemon_data/" + pokemon4_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon4_icon = mon_file["Graphics"]["Front_Sprite"]
            self.pokemon_4.setPixmap(pokemon4_icon)

            pokemon5_data = dataBox["Pokemon5"][0]
            with open("../battle_system/pokemon_data/" + pokemon5_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon5_icon = mon_file["Graphics"]["Front_Sprite"]
            self.pokemon_5.setPixmap(pokemon5_icon)

            pokemon6_data = dataBox["Pokemon6"][0]
            with open("../battle_system/pokemon_data/" + pokemon6_data + ".json", "r") as loop:
                        mon_file = json.load(loop)
            pokemon6_icon = mon_file["Graphics"]["Front_Sprite"]
            self.pokemon_6.setPixmap(pokemon6_icon)
            print(dataBox["Time_Spent"])
            self.time_played.setText(dataBox["Time_Spent"])
        except:
            print("No trainer is available, go make one!")
    def new_trainer_creator(self, ):
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