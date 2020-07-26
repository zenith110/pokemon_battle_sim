from PySide2 import QtWidgets, QtCore, QtGui
import json
import app
import os
"""
Basic Pokemon class that lets us keep the data consistent across the program
"""
class pokemon():
    def __init__(self):
        self.name = "NONE"
        self.background = "NONE"

data = pokemon()
class tool(app.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(tool, self).__init__()
        self.setupUi(self)
        with open("backgrounds.json", "r") as loop:
                background = json.load(loop)
        with open("assets/pokemon_data/list_of_pokemon.json", "r") as loop:
            pokemon = json.load(loop)
        for i in pokemon["Name"]:
            self.pokemon.addItem(i)
        for j in background["Name"]:
            self.background_selection.addItem(j)
        self.background_selection.currentTextChanged.connect(self.background_change)
        self.pokemon.currentTextChanged.connect(self.pokemon_change)
        self.save.clicked.connect(self.save_data)
    """
    Saves all data used so far into the respective pokemon json file
    """
    def save_data(self):
        with open("assets/pokemon_data/" + data.name + ".json", "r") as loop:
                        mon_file = json.load(loop)
        
        mon_file["Front_Position"][data.background + "_X_Pos"] = int(self.front_x.text())
        mon_file["Front_Position"][data.background + "_Y_Pos"] = int(self.front_y.text())
        mon_file["Back_Position"][data.background + "_X_Pos"] = int(self.back_x.text())
        mon_file["Back_Position"][data.background + "_Y_Pos"] = int(self.back_y.text())
        

        file = open("assets/pokemon_data/" + data.name + ".json", "w")
        # Dumps the data to the file
        json.dump(mon_file, file, indent = 1)
        print("Dumping data now...")
        file.close()
        
    """
    Updates the pokemon position, sprites based on selected pokemon
    """
    def pokemon_change(self, index):
        with open("assets/pokemon_data/" + index + ".json", "r") as loop:
                        mon_file = json.load(loop)
        front_path = "assets/resources/graphics/pokemon_sprites" + "/" + index + "/"
        front = os.path.dirname(front_path)
        self.front.setPixmap(os.path.join(front, index + "_front.png"))
        try:
            self.front.setGeometry(int(self.front_x.text()), int(self.front_y.text()), 64, 64)
        except:
            self.front_x.setText("61")
            self.front_y.setText("101")
            self.front.setGeometry(64, 64, 61, 101)
            
        back_path = "assets/resources/graphics/pokemon_sprites" + "/" + index + "/"
        back = os.path.dirname(back_path)
        self.back.setPixmap(os.path.join(front, index + "_back.png"))
        try:
            self.back.setGeometry(int(self.back_x.text()), int(self.back_y.text()), 64, 64)
        except:
            print("No coordinates has been set, defaulting...")
            self.back_x.setText("61")
            self.back_y.setText("101")
            self.back.setGeometry(64, 64, 61, 101)
        data.name = index
    """
    Updates the background depending on the index selected in the combobox
    """
    def background_change(self, index):
        background_dir = os.path.dirname("assets/resources/graphics/battle_backgrounds/")
        self.background.setPixmap(os.path.join(background_dir, index + ".png"))
        data.background = index
        
if __name__ == "__main__":
    app = QtWidgets.QApplication()
    qt_app = tool()
    qt_app.show()
    app.exec_()