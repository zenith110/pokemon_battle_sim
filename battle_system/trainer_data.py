from PySide2 import QtWidgets, QtCore, QtGui
import json
import math
def pokemon_json_data(self):
        name = self.name.text()
        profile_image, _blank = QtWidgets.QFileDialog.getOpenFileName(self, self.tr("Open trainer sprite"), self.tr("graphics/trainer_sprite/"), self.tr("Image (*.png)"))
        
        pokemon1_name = self.pokemon1_combo.currentText()
        pokemon1_move1 = self.pokemon1_move1.currentText()
        pokemon1_move2 = self.pokemon1_move2.currentText()
        pokemon1_move3 = self.pokemon1_move3.currentText()
        pokemon1_move4 = self.pokemon1_move4.currentText()
        pokemon1_level = self.pokemon1_level.value()
        pokemon1_item = self.pokemon1_item.currentText()
        with open("battle_system/pokemon_data/" + pokemon1_name + ".json", "r") as loop:
                    mon_file = json.load(loop)
        # Formula = BaseStat × 2 + 204
        pokemon1_base_hp = mon_file["Stats"]["HP"]
        pokemon1_base_attack = mon_file["Stats"]["Attack"]
        pokemon1_base_defense = mon_file["Stats"]["Defense"]
        pokemon1_base_sp_atk = mon_file["Stats"]["Sp. Atk"]
        pokemon1_base_sp_def = mon_file["Stats"]["Sp. Def"]
        pokemon1_base_speed = mon_file["Stats"]["Speed"]
        pokemon1_icon = mon_file["Resource_data"]["Image_dir"] + "icon.png"
        pokemon1_front = mon_file["Resource_data"]["Image_dir"] + pokemon1_name + "_front.png"
        pokemon1_back = mon_file["Resource_data"]["Image_dir"] + pokemon1_name + "_back.png"

        pokemon1_max_hp = math.floor(((2 * pokemon1_base_hp + 28 + 1) * (pokemon1_level / 100) + pokemon1_level + 10))
        pokemon1_max_attack = math.floor((2 * pokemon1_base_attack + 4 + 0) * ((pokemon1_base_attack / 100) + 5) * 0.9)
        pokemon1_max_defense = math.floor((2 * pokemon1_base_defense + 4 + 0) * ((pokemon1_base_defense / 100) + 5) * 0.9)
        pokemon1_max_sp_atk = math.floor((2 * pokemon1_base_sp_atk + 4 + 0) * ((pokemon1_base_sp_atk / 100) + 5) * 0.9)
        pokemon1_max_sp_def = math.floor((2 * pokemon1_base_sp_def + 4 + 0) * ((pokemon1_base_sp_def / 100) + 5) * 0.9)
        pokemon1_max_speed = math.floor((2 * pokemon1_base_speed + 4 + 0) * ((pokemon1_base_speed / 100) + 5) * 0.9)

        # Hard code the values for the backgrounds
        pokemon1_front_x_Morning_1 = mon_file["Front_Position"]["Morning_1_X_Pos"]
        pokemon1_front_y_Morning_1 = mon_file["Front_Position"]["Morning_1_Y_Pos"]
        pokemon1_front_x_Morning_2 = mon_file["Front_Position"]["Morning_2_X_Pos"]
        pokemon1_front_y_Morning_2 = mon_file["Front_Position"]["Morning_2_Y_Pos"]
        pokemon1_front_x_Morning_3 = mon_file["Front_Position"]["Morning_3_X_Pos"]
        pokemon1_front_y_Morning_3 = mon_file["Front_Position"]["Morning_3_Y_Pos"]
        pokemon1_front_x_Morning_4 = mon_file["Front_Position"]["Morning_4_X_Pos"]
        pokemon1_front_y_Morning_4 = mon_file["Front_Position"]["Morning_4_Y_Pos"]
        pokemon1_front_x_Morning_5 = mon_file["Front_Position"]["Morning_5_X_Pos"]
        pokemon1_front_y_Morning_5 = mon_file["Front_Position"]["Morning_5_Y_Pos"]
        pokemon1_front_x_Morning_6 = mon_file["Front_Position"]["Morning_6_X_Pos"]
        pokemon1_front_y_Morning_6 = mon_file["Front_Position"]["Morning_6_Y_Pos"]
        pokemon1_front_x_Morning_7 = mon_file["Front_Position"]["Morning_7_X_Pos"]
        pokemon1_front_y_Morning_7 = mon_file["Front_Position"]["Morning_7_Y_Pos"]
        pokemon1_front_x_Morning_8 = mon_file["Front_Position"]["Morning_8_X_Pos"]
        pokemon1_front_y_Morning_8 = mon_file["Front_Position"]["Morning_8_Y_Pos"]


        pokemon1_back_x_Morning_1 = mon_file["Back_Position"]["Morning_1_X_Pos"]
        pokemon1_back_y_Morning_1 = mon_file["Back_Position"]["Morning_1_Y_Pos"]
        pokemon1_back_x_Morning_2 = mon_file["Back_Position"]["Morning_2_X_Pos"]
        pokemon1_back_y_Morning_2 = mon_file["Back_Position"]["Morning_2_Y_Pos"]
        pokemon1_back_x_Morning_3 = mon_file["Back_Position"]["Morning_3_X_Pos"]
        pokemon1_back_y_Morning_3 = mon_file["Back_Position"]["Morning_3_Y_Pos"]
        pokemon1_back_x_Morning_4 = mon_file["Back_Position"]["Morning_4_X_Pos"]
        pokemon1_back_y_Morning_4 = mon_file["Back_Position"]["Morning_4_Y_Pos"]
        pokemon1_back_x_Morning_5 = mon_file["Back_Position"]["Morning_5_X_Pos"]
        pokemon1_back_y_Morning_5 = mon_file["Back_Position"]["Morning_5_Y_Pos"]
        pokemon1_back_x_Morning_6 = mon_file["Back_Position"]["Morning_6_X_Pos"]
        pokemon1_back_y_Morning_6 = mon_file["Back_Position"]["Morning_6_Y_Pos"]
        pokemon1_back_x_Morning_7 = mon_file["Back_Position"]["Morning_7_X_Pos"]
        pokemon1_back_y_Morning_7 = mon_file["Back_Position"]["Morning_7_Y_Pos"]
        pokemon1_back_x_Morning_8 = mon_file["Back_Position"]["Morning_8_X_Pos"]
        pokemon1_back_y_Morning_8 = mon_file["Back_Position"]["Morning_8_Y_Pos"]


        pokemon1_front_x_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_X_Pos"]
        pokemon1_front_y_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_Y_Pos"]
        pokemon1_front_x_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_X_Pos"]
        pokemon1_front_y_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_Y_Pos"]
        pokemon1_front_x_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_X_Pos"]
        pokemon1_front_y_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_Y_Pos"]
        pokemon1_front_x_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_X_Pos"]
        pokemon1_front_y_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_Y_Pos"]
        pokemon1_front_x_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_X_Pos"]
        pokemon1_front_y_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_Y_Pos"]
        pokemon1_front_x_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_X_Pos"]
        pokemon1_front_y_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_Y_Pos"]
        pokemon1_front_x_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_X_Pos"]
        pokemon1_front_y_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_Y_Pos"]
        pokemon1_front_x_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_X_Pos"]
        pokemon1_front_y_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_Y_Pos"]


        pokemon1_back_x_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_X_Pos"]
        pokemon1_back_y_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_Y_Pos"]
        pokemon1_back_x_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_X_Pos"]
        pokemon1_back_y_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_Y_Pos"]
        pokemon1_back_x_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_X_Pos"]
        pokemon1_back_y_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_Y_Pos"]
        pokemon1_back_x_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_X_Pos"]
        pokemon1_back_y_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_Y_Pos"]
        pokemon1_back_x_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_X_Pos"]
        pokemon1_back_y_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_Y_Pos"]
        pokemon1_back_x_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_X_Pos"]
        pokemon1_back_y_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_Y_Pos"]
        pokemon1_back_x_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_X_Pos"]
        pokemon1_back_y_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_Y_Pos"]
        pokemon1_back_x_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_X_Pos"]
        pokemon1_back_y_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_Y_Pos"]


        pokemon1_front_x_Night_1 = mon_file["Front_Position"]["Night_1_X_Pos"]
        pokemon1_front_y_Night_1 = mon_file["Front_Position"]["Night_1_Y_Pos"]
        pokemon1_front_x_Night_2 = mon_file["Front_Position"]["Night_2_X_Pos"]
        pokemon1_front_y_Night_2 = mon_file["Front_Position"]["Night_2_Y_Pos"]
        pokemon1_front_x_Night_3 = mon_file["Front_Position"]["Night_3_X_Pos"]
        pokemon1_front_y_Night_3 = mon_file["Front_Position"]["Night_3_Y_Pos"]
        pokemon1_front_x_Night_4 = mon_file["Front_Position"]["Night_4_X_Pos"]
        pokemon1_front_y_Night_4 = mon_file["Front_Position"]["Night_4_Y_Pos"]
        pokemon1_front_x_Night_5 = mon_file["Front_Position"]["Night_5_X_Pos"]
        pokemon1_front_y_Night_5 = mon_file["Front_Position"]["Night_5_Y_Pos"]
        pokemon1_front_x_Night_6 = mon_file["Front_Position"]["Night_6_X_Pos"]
        pokemon1_front_y_Night_6 = mon_file["Front_Position"]["Night_6_Y_Pos"]
        pokemon1_front_x_Night_7 = mon_file["Front_Position"]["Night_7_X_Pos"]
        pokemon1_front_y_Night_7 = mon_file["Front_Position"]["Night_7_Y_Pos"]
        pokemon1_front_x_Night_8 = mon_file["Front_Position"]["Night_8_X_Pos"]
        pokemon1_front_y_Night_8 = mon_file["Front_Position"]["Night_8_Y_Pos"]

        pokemon1_back_x_Night_1 = mon_file["Back_Position"]["Night_1_X_Pos"]
        pokemon1_back_y_Night_1 = mon_file["Back_Position"]["Night_1_Y_Pos"]
        pokemon1_back_x_Night_2 = mon_file["Back_Position"]["Night_2_X_Pos"]
        pokemon1_back_y_Night_2 = mon_file["Back_Position"]["Night_2_Y_Pos"]
        pokemon1_back_x_Night_3 = mon_file["Back_Position"]["Night_3_X_Pos"]
        pokemon1_back_y_Night_3 = mon_file["Back_Position"]["Night_3_Y_Pos"]
        pokemon1_back_x_Night_4 = mon_file["Back_Position"]["Night_4_X_Pos"]
        pokemon1_back_y_Night_4 = mon_file["Back_Position"]["Night_4_Y_Pos"]
        pokemon1_back_x_Night_5 = mon_file["Back_Position"]["Night_5_X_Pos"]
        pokemon1_back_y_Night_5 = mon_file["Back_Position"]["Night_5_Y_Pos"]
        pokemon1_back_x_Night_6 = mon_file["Back_Position"]["Night_6_X_Pos"]
        pokemon1_back_y_Night_6 = mon_file["Back_Position"]["Night_6_Y_Pos"]
        pokemon1_back_x_Night_7 = mon_file["Back_Position"]["Night_7_X_Pos"]
        pokemon1_back_y_Night_7 = mon_file["Back_Position"]["Night_7_Y_Pos"]
        pokemon1_back_x_Night_8 = mon_file["Back_Position"]["Night_8_X_Pos"]
        pokemon1_back_y_Night_8 = mon_file["Back_Position"]["Night_8_Y_Pos"]


        pokemon2_name = self.pokemon2_combo.currentText()
        pokemon2_move1 = self.pokemon2_move1.currentText()
        pokemon2_move2 = self.pokemon2_move2.currentText()
        pokemon2_move3 = self.pokemon2_move3.currentText()
        pokemon2_move4 = self.pokemon2_move4.currentText()
        pokemon2_level = self.pokemon2_level.value()
        pokemon2_item = self.pokemon2_item.currentText()
        with open("battle_system/pokemon_data/" + pokemon2_name + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon2_base_hp = mon_file["Stats"]["HP"]
        pokemon2_base_attack = mon_file["Stats"]["Attack"]
        pokemon2_base_defense = mon_file["Stats"]["Defense"]
        pokemon2_base_sp_atk = mon_file["Stats"]["Sp. Atk"]
        pokemon2_base_sp_def = mon_file["Stats"]["Sp. Def"]
        pokemon2_base_speed = mon_file["Stats"]["Speed"]
        pokemon2_icon = mon_file["Resource_data"]["Image_dir"] + "icon.png"
        pokemon2_front = mon_file["Resource_data"]["Image_dir"] + pokemon2_name + "_front.png"
        pokemon2_back = mon_file["Resource_data"]["Image_dir"] + pokemon2_name + "_back.png"

        pokemon2_max_hp = math.floor(((2 * pokemon2_base_hp + 28 + 1) * (pokemon2_level / 100) + pokemon2_level + 10))
        pokemon2_max_attack = math.floor((2 * pokemon2_base_attack + 4 + 0) * ((pokemon2_base_attack / 100) + 5) * 0.9)
        pokemon2_max_defense = math.floor((2 * pokemon2_base_defense + 4 + 0) * ((pokemon2_base_defense / 100) + 5) * 0.9)
        pokemon2_max_sp_atk = math.floor((2 * pokemon2_base_sp_atk + 4 + 0) * ((pokemon2_base_sp_atk / 100) + 5) * 0.9)
        pokemon2_max_sp_def = math.floor((2 * pokemon2_base_sp_def + 4 + 0) * ((pokemon2_base_sp_def / 100) + 5) * 0.9)
        pokemon2_max_speed = math.floor((2 * pokemon2_base_speed + 4 + 0) * ((pokemon2_base_speed / 100) + 5) * 0.9)
        

        # Hard code the values for the backgrounds
        pokemon2_front_x_Morning_1 = mon_file["Front_Position"]["Morning_1_X_Pos"]
        pokemon2_front_y_Morning_1 = mon_file["Front_Position"]["Morning_1_Y_Pos"]
        pokemon2_front_x_Morning_2 = mon_file["Front_Position"]["Morning_2_X_Pos"]
        pokemon2_front_y_Morning_2 = mon_file["Front_Position"]["Morning_2_Y_Pos"]
        pokemon2_front_x_Morning_3 = mon_file["Front_Position"]["Morning_3_X_Pos"]
        pokemon2_front_y_Morning_3 = mon_file["Front_Position"]["Morning_3_Y_Pos"]
        pokemon2_front_x_Morning_4 = mon_file["Front_Position"]["Morning_4_X_Pos"]
        pokemon2_front_y_Morning_4 = mon_file["Front_Position"]["Morning_4_Y_Pos"]
        pokemon2_front_x_Morning_5 = mon_file["Front_Position"]["Morning_5_X_Pos"]
        pokemon2_front_y_Morning_5 = mon_file["Front_Position"]["Morning_5_Y_Pos"]
        pokemon2_front_x_Morning_6 = mon_file["Front_Position"]["Morning_6_X_Pos"]
        pokemon2_front_y_Morning_6 = mon_file["Front_Position"]["Morning_6_Y_Pos"]
        pokemon2_front_x_Morning_7 = mon_file["Front_Position"]["Morning_7_X_Pos"]
        pokemon2_front_y_Morning_7 = mon_file["Front_Position"]["Morning_7_Y_Pos"]
        pokemon2_front_x_Morning_8 = mon_file["Front_Position"]["Morning_8_X_Pos"]
        pokemon2_front_y_Morning_8 = mon_file["Front_Position"]["Morning_8_Y_Pos"]

        pokemon2_back_x_Morning_1 = mon_file["Back_Position"]["Morning_1_X_Pos"]
        pokemon2_back_y_Morning_1 = mon_file["Back_Position"]["Morning_1_Y_Pos"]
        pokemon2_back_x_Morning_2 = mon_file["Back_Position"]["Morning_2_X_Pos"]
        pokemon2_back_y_Morning_2 = mon_file["Back_Position"]["Morning_2_Y_Pos"]
        pokemon2_back_x_Morning_3 = mon_file["Back_Position"]["Morning_3_X_Pos"]
        pokemon2_back_y_Morning_3 = mon_file["Back_Position"]["Morning_3_Y_Pos"]
        pokemon2_back_x_Morning_4 = mon_file["Back_Position"]["Morning_4_X_Pos"]
        pokemon2_back_y_Morning_4 = mon_file["Back_Position"]["Morning_4_Y_Pos"]
        pokemon2_back_x_Morning_5 = mon_file["Back_Position"]["Morning_5_X_Pos"]
        pokemon2_back_y_Morning_5 = mon_file["Back_Position"]["Morning_5_Y_Pos"]
        pokemon2_back_x_Morning_6 = mon_file["Back_Position"]["Morning_6_X_Pos"]
        pokemon2_back_y_Morning_6 = mon_file["Back_Position"]["Morning_6_Y_Pos"]
        pokemon2_back_x_Morning_7 = mon_file["Back_Position"]["Morning_7_X_Pos"]
        pokemon2_back_y_Morning_7 = mon_file["Back_Position"]["Morning_7_Y_Pos"]
        pokemon2_back_x_Morning_8 = mon_file["Back_Position"]["Morning_8_X_Pos"]
        pokemon2_back_y_Morning_8 = mon_file["Back_Position"]["Morning_8_Y_Pos"]

        pokemon2_front_x_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_X_Pos"]
        pokemon2_front_y_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_Y_Pos"]
        pokemon2_front_x_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_X_Pos"]
        pokemon2_front_y_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_Y_Pos"]
        pokemon2_front_x_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_X_Pos"]
        pokemon2_front_y_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_Y_Pos"]
        pokemon2_front_x_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_X_Pos"]
        pokemon2_front_y_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_Y_Pos"]
        pokemon2_front_x_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_X_Pos"]
        pokemon2_front_y_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_Y_Pos"]
        pokemon2_front_x_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_X_Pos"]
        pokemon2_front_y_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_Y_Pos"]
        pokemon2_front_x_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_X_Pos"]
        pokemon2_front_y_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_Y_Pos"]
        pokemon2_front_x_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_X_Pos"]
        pokemon2_front_y_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_Y_Pos"]


        pokemon2_back_x_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_X_Pos"]
        pokemon2_back_y_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_Y_Pos"]
        pokemon2_back_x_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_X_Pos"]
        pokemon2_back_y_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_Y_Pos"]
        pokemon2_back_x_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_X_Pos"]
        pokemon2_back_y_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_Y_Pos"]
        pokemon2_back_x_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_X_Pos"]
        pokemon2_back_y_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_Y_Pos"]
        pokemon2_back_x_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_X_Pos"]
        pokemon2_back_y_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_Y_Pos"]
        pokemon2_back_x_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_X_Pos"]
        pokemon2_back_y_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_Y_Pos"]
        pokemon2_back_x_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_X_Pos"]
        pokemon2_back_y_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_Y_Pos"]
        pokemon2_back_x_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_X_Pos"]
        pokemon2_back_y_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_Y_Pos"]

        pokemon2_front_x_Night_1 = mon_file["Front_Position"]["Night_1_X_Pos"]
        pokemon2_front_y_Night_1 = mon_file["Front_Position"]["Night_1_Y_Pos"]
        pokemon2_front_x_Night_2 = mon_file["Front_Position"]["Night_2_X_Pos"]
        pokemon2_front_y_Night_2 = mon_file["Front_Position"]["Night_2_Y_Pos"]
        pokemon2_front_x_Night_3 = mon_file["Front_Position"]["Night_3_X_Pos"]
        pokemon2_front_y_Night_3 = mon_file["Front_Position"]["Night_3_Y_Pos"]
        pokemon2_front_x_Night_4 = mon_file["Front_Position"]["Night_4_X_Pos"]
        pokemon2_front_y_Night_4 = mon_file["Front_Position"]["Night_4_Y_Pos"]
        pokemon2_front_x_Night_5 = mon_file["Front_Position"]["Night_5_X_Pos"]
        pokemon2_front_y_Night_5 = mon_file["Front_Position"]["Night_5_Y_Pos"]
        pokemon2_front_x_Night_6 = mon_file["Front_Position"]["Night_6_X_Pos"]
        pokemon2_front_y_Night_6 = mon_file["Front_Position"]["Night_6_Y_Pos"]
        pokemon2_front_x_Night_7 = mon_file["Front_Position"]["Night_7_X_Pos"]
        pokemon2_front_y_Night_7 = mon_file["Front_Position"]["Night_7_Y_Pos"]
        pokemon2_front_x_Night_8 = mon_file["Front_Position"]["Night_8_X_Pos"]
        pokemon2_front_y_Night_8 = mon_file["Front_Position"]["Night_8_Y_Pos"]


        pokemon2_back_x_Night_1 = mon_file["Back_Position"]["Night_1_X_Pos"]
        pokemon2_back_y_Night_1 = mon_file["Back_Position"]["Night_1_Y_Pos"]
        pokemon2_back_x_Night_2 = mon_file["Back_Position"]["Night_2_X_Pos"]
        pokemon2_back_y_Night_2 = mon_file["Back_Position"]["Night_2_Y_Pos"]
        pokemon2_back_x_Night_3 = mon_file["Back_Position"]["Night_3_X_Pos"]
        pokemon2_back_y_Night_3 = mon_file["Back_Position"]["Night_3_Y_Pos"]
        pokemon2_back_x_Night_4 = mon_file["Back_Position"]["Night_4_X_Pos"]
        pokemon2_back_y_Night_4 = mon_file["Back_Position"]["Night_4_Y_Pos"]
        pokemon2_back_x_Night_5 = mon_file["Back_Position"]["Night_5_X_Pos"]
        pokemon2_back_y_Night_5 = mon_file["Back_Position"]["Night_5_Y_Pos"]
        pokemon2_back_x_Night_6 = mon_file["Back_Position"]["Night_6_X_Pos"]
        pokemon2_back_y_Night_6 = mon_file["Back_Position"]["Night_6_Y_Pos"]
        pokemon2_back_x_Night_7 = mon_file["Back_Position"]["Night_7_X_Pos"]
        pokemon2_back_y_Night_7 = mon_file["Back_Position"]["Night_7_Y_Pos"]
        pokemon2_back_x_Night_8 = mon_file["Back_Position"]["Night_8_X_Pos"]
        pokemon2_back_y_Night_8 = mon_file["Back_Position"]["Night_8_Y_Pos"]

        pokemon3_name = self.pokemon3_combo.currentText()
        pokemon3_move1 = self.pokemon3_move1.currentText()
        pokemon3_move2 = self.pokemon3_move2.currentText()
        pokemon3_move3 = self.pokemon3_move3.currentText()
        pokemon3_move4 = self.pokemon3_move4.currentText()
        pokemon3_level = self.pokemon3_level.value()
        pokemon3_item = self.pokemon3_item.currentText()
        with open("battle_system/pokemon_data/" + pokemon3_name + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon3_base_hp = mon_file["Stats"]["HP"]
        pokemon3_base_attack = mon_file["Stats"]["Attack"]
        pokemon3_base_defense = mon_file["Stats"]["Defense"]
        pokemon3_base_sp_atk = mon_file["Stats"]["Sp. Atk"]
        pokemon3_base_sp_def = mon_file["Stats"]["Sp. Def"]
        pokemon3_base_speed = mon_file["Stats"]["Speed"]
        pokemon3_icon = mon_file["Resource_data"]["Image_dir"] + "icon.png"
        pokemon3_front = mon_file["Resource_data"]["Image_dir"] + pokemon3_name + "_front.png"
        pokemon3_back = mon_file["Resource_data"]["Image_dir"] + pokemon3_name + "_back.png"

        pokemon3_max_hp = math.floor(((2 * pokemon3_base_hp + 28 + 1) * (pokemon3_level / 100) + pokemon3_level + 10))
        pokemon3_max_attack = math.floor((2 * pokemon3_base_attack + 4 + 0) * ((pokemon3_base_attack / 100) + 5) * 0.9)
        pokemon3_max_defense = math.floor((2 * pokemon3_base_defense + 4 + 0) * ((pokemon3_base_defense / 100) + 5) * 0.9)
        pokemon3_max_sp_atk = math.floor((2 * pokemon3_base_sp_atk + 4 + 0) * ((pokemon3_base_sp_atk / 100) + 5) * 0.9)
        pokemon3_max_sp_def = math.floor((2 * pokemon3_base_sp_def + 4 + 0) * ((pokemon3_base_sp_def / 100) + 5) * 0.9)
        pokemon3_max_speed = math.floor((2 * pokemon3_base_speed + 4 + 0) * ((pokemon3_base_speed / 100) + 5) * 0.9)
        
        
        
        pokemon3_front_x_Morning_1 = mon_file["Front_Position"]["Morning_1_X_Pos"]
        pokemon3_front_y_Morning_1 = mon_file["Front_Position"]["Morning_1_Y_Pos"]
        pokemon3_front_x_Morning_2 = mon_file["Front_Position"]["Morning_2_X_Pos"]
        pokemon3_front_y_Morning_2 = mon_file["Front_Position"]["Morning_2_Y_Pos"]
        pokemon3_front_x_Morning_3 = mon_file["Front_Position"]["Morning_3_X_Pos"]
        pokemon3_front_y_Morning_3 = mon_file["Front_Position"]["Morning_3_Y_Pos"]
        pokemon3_front_x_Morning_4 = mon_file["Front_Position"]["Morning_4_X_Pos"]
        pokemon3_front_y_Morning_4 = mon_file["Front_Position"]["Morning_4_Y_Pos"]
        pokemon3_front_x_Morning_5 = mon_file["Front_Position"]["Morning_5_X_Pos"]
        pokemon3_front_y_Morning_5 = mon_file["Front_Position"]["Morning_5_Y_Pos"]
        pokemon3_front_x_Morning_6 = mon_file["Front_Position"]["Morning_6_X_Pos"]
        pokemon3_front_y_Morning_6 = mon_file["Front_Position"]["Morning_6_Y_Pos"]
        pokemon3_front_x_Morning_7 = mon_file["Front_Position"]["Morning_7_X_Pos"]
        pokemon3_front_y_Morning_7 = mon_file["Front_Position"]["Morning_7_Y_Pos"]
        pokemon3_front_x_Morning_8 = mon_file["Front_Position"]["Morning_8_X_Pos"]
        pokemon3_front_y_Morning_8 = mon_file["Front_Position"]["Morning_8_Y_Pos"]

        pokemon3_back_x_Morning_1 = mon_file["Back_Position"]["Morning_1_X_Pos"]
        pokemon3_back_y_Morning_1 = mon_file["Back_Position"]["Morning_1_Y_Pos"]
        pokemon3_back_x_Morning_2 = mon_file["Back_Position"]["Morning_2_X_Pos"]
        pokemon3_back_y_Morning_2 = mon_file["Back_Position"]["Morning_2_Y_Pos"]
        pokemon3_back_x_Morning_3 = mon_file["Back_Position"]["Morning_3_X_Pos"]
        pokemon3_back_y_Morning_3 = mon_file["Back_Position"]["Morning_3_Y_Pos"]
        pokemon3_back_x_Morning_4 = mon_file["Back_Position"]["Morning_4_X_Pos"]
        pokemon3_back_y_Morning_4 = mon_file["Back_Position"]["Morning_4_Y_Pos"]
        pokemon3_back_x_Morning_5 = mon_file["Back_Position"]["Morning_5_X_Pos"]
        pokemon3_back_y_Morning_5 = mon_file["Back_Position"]["Morning_5_Y_Pos"]
        pokemon3_back_x_Morning_6 = mon_file["Back_Position"]["Morning_6_X_Pos"]
        pokemon3_back_y_Morning_6 = mon_file["Back_Position"]["Morning_6_Y_Pos"]
        pokemon3_back_x_Morning_7 = mon_file["Back_Position"]["Morning_7_X_Pos"]
        pokemon3_back_y_Morning_7 = mon_file["Back_Position"]["Morning_7_Y_Pos"]
        pokemon3_back_x_Morning_8 = mon_file["Back_Position"]["Morning_8_X_Pos"]
        pokemon3_back_y_Morning_8 = mon_file["Back_Position"]["Morning_8_Y_Pos"]

        pokemon3_front_x_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_X_Pos"]
        pokemon3_front_y_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_Y_Pos"]
        pokemon3_front_x_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_X_Pos"]
        pokemon3_front_y_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_Y_Pos"]
        pokemon3_front_x_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_X_Pos"]
        pokemon3_front_y_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_Y_Pos"]
        pokemon3_front_x_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_X_Pos"]
        pokemon3_front_y_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_Y_Pos"]
        pokemon3_front_x_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_X_Pos"]
        pokemon3_front_y_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_Y_Pos"]
        pokemon3_front_x_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_X_Pos"]
        pokemon3_front_y_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_Y_Pos"]
        pokemon3_front_x_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_X_Pos"]
        pokemon3_front_y_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_Y_Pos"]
        pokemon3_front_x_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_X_Pos"]
        pokemon3_front_y_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_Y_Pos"]


        pokemon3_back_x_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_X_Pos"]
        pokemon3_back_y_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_Y_Pos"]
        pokemon3_back_x_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_X_Pos"]
        pokemon3_back_y_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_Y_Pos"]
        pokemon3_back_x_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_X_Pos"]
        pokemon3_back_y_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_Y_Pos"]
        pokemon3_back_x_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_X_Pos"]
        pokemon3_back_y_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_Y_Pos"]
        pokemon3_back_x_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_X_Pos"]
        pokemon3_back_y_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_Y_Pos"]
        pokemon3_back_x_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_X_Pos"]
        pokemon3_back_y_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_Y_Pos"]
        pokemon3_back_x_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_X_Pos"]
        pokemon3_back_y_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_Y_Pos"]
        pokemon3_back_x_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_X_Pos"]
        pokemon3_back_y_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_Y_Pos"]

        pokemon3_front_x_Night_1 = mon_file["Front_Position"]["Night_1_X_Pos"]
        pokemon3_front_y_Night_1 = mon_file["Front_Position"]["Night_1_Y_Pos"]
        pokemon3_front_x_Night_2 = mon_file["Front_Position"]["Night_2_X_Pos"]
        pokemon3_front_y_Night_2 = mon_file["Front_Position"]["Night_2_Y_Pos"]
        pokemon3_front_x_Night_3 = mon_file["Front_Position"]["Night_3_X_Pos"]
        pokemon3_front_y_Night_3 = mon_file["Front_Position"]["Night_3_Y_Pos"]
        pokemon3_front_x_Night_4 = mon_file["Front_Position"]["Night_4_X_Pos"]
        pokemon3_front_y_Night_4 = mon_file["Front_Position"]["Night_4_Y_Pos"]
        pokemon3_front_x_Night_5 = mon_file["Front_Position"]["Night_5_X_Pos"]
        pokemon3_front_y_Night_5 = mon_file["Front_Position"]["Night_5_Y_Pos"]
        pokemon3_front_x_Night_6 = mon_file["Front_Position"]["Night_6_X_Pos"]
        pokemon3_front_y_Night_6 = mon_file["Front_Position"]["Night_6_Y_Pos"]
        pokemon3_front_x_Night_7 = mon_file["Front_Position"]["Night_7_X_Pos"]
        pokemon3_front_y_Night_7 = mon_file["Front_Position"]["Night_7_Y_Pos"]
        pokemon3_front_x_Night_8 = mon_file["Front_Position"]["Night_8_X_Pos"]
        pokemon3_front_y_Night_8 = mon_file["Front_Position"]["Night_8_Y_Pos"]


        pokemon3_back_x_Night_1 = mon_file["Back_Position"]["Night_1_X_Pos"]
        pokemon3_back_y_Night_1 = mon_file["Back_Position"]["Night_1_Y_Pos"]
        pokemon3_back_x_Night_2 = mon_file["Back_Position"]["Night_2_X_Pos"]
        pokemon3_back_y_Night_2 = mon_file["Back_Position"]["Night_2_Y_Pos"]
        pokemon3_back_x_Night_3 = mon_file["Back_Position"]["Night_3_X_Pos"]
        pokemon3_back_y_Night_3 = mon_file["Back_Position"]["Night_3_Y_Pos"]
        pokemon3_back_x_Night_4 = mon_file["Back_Position"]["Night_4_X_Pos"]
        pokemon3_back_y_Night_4 = mon_file["Back_Position"]["Night_4_Y_Pos"]
        pokemon3_back_x_Night_5 = mon_file["Back_Position"]["Night_5_X_Pos"]
        pokemon3_back_y_Night_5 = mon_file["Back_Position"]["Night_5_Y_Pos"]
        pokemon3_back_x_Night_6 = mon_file["Back_Position"]["Night_6_X_Pos"]
        pokemon3_back_y_Night_6 = mon_file["Back_Position"]["Night_6_Y_Pos"]
        pokemon3_back_x_Night_7 = mon_file["Back_Position"]["Night_7_X_Pos"]
        pokemon3_back_y_Night_7 = mon_file["Back_Position"]["Night_7_Y_Pos"]
        pokemon3_back_x_Night_8 = mon_file["Back_Position"]["Night_8_X_Pos"]
        pokemon3_back_y_Night_8 = mon_file["Back_Position"]["Night_8_Y_Pos"]

        pokemon4_name = self.pokemon4_combo.currentText()
        pokemon4_move1 = self.pokemon4_move1.currentText()
        pokemon4_move2 = self.pokemon4_move2.currentText()
        pokemon4_move3 = self.pokemon4_move3.currentText()
        pokemon4_move4 = self.pokemon4_move4.currentText()
        pokemon4_level = self.pokemon4_level.value()
        pokemon4_item = self.pokemon4_item.currentText()
        with open("battle_system/pokemon_data/" + pokemon4_name + ".json", "r") as loop:
                    mon_file = json.load(loop)

        pokemon4_base_hp = mon_file["Stats"]["HP"]
        pokemon4_base_attack = mon_file["Stats"]["Attack"]
        pokemon4_base_defense = mon_file["Stats"]["Defense"]
        pokemon4_base_sp_atk = mon_file["Stats"]["Sp. Atk"]
        pokemon4_base_sp_def = mon_file["Stats"]["Sp. Def"]
        pokemon4_base_speed = mon_file["Stats"]["Speed"]
        pokemon4_icon = mon_file["Resource_data"]["Image_dir"] + "icon.png"
        pokemon4_front = mon_file["Resource_data"]["Image_dir"] + pokemon4_name + "_front.png"
        pokemon4_back = mon_file["Resource_data"]["Image_dir"] + pokemon4_name + "_back.png"

        pokemon4_max_hp = math.floor(((2 * pokemon4_base_hp + 28 + 1) * (pokemon4_level / 100) + pokemon4_level + 10))
        pokemon4_max_attack = math.floor((2 * pokemon4_base_attack + 4 + 0) * ((pokemon4_base_attack / 100) + 5) * 0.9)
        pokemon4_max_defense = math.floor((2 * pokemon4_base_defense + 4 + 0) * ((pokemon4_base_defense / 100) + 5) * 0.9)
        pokemon4_max_sp_atk = math.floor((2 * pokemon4_base_sp_atk + 4 + 0) * ((pokemon4_base_sp_atk / 100) + 5) * 0.9)
        pokemon4_max_sp_def = math.floor((2 * pokemon4_base_sp_def + 4 + 0) * ((pokemon4_base_sp_def / 100) + 5) * 0.9)
        pokemon4_max_speed = math.floor((2 * pokemon4_base_speed + 4 + 0) * ((pokemon4_base_speed / 100) + 5) * 0.9)
    
        # Hard code the values for the backgrounds
        pokemon4_front_x_Morning_1 = mon_file["Front_Position"]["Morning_1_X_Pos"]
        pokemon4_front_y_Morning_1 = mon_file["Front_Position"]["Morning_1_Y_Pos"]
        pokemon4_front_x_Morning_2 = mon_file["Front_Position"]["Morning_2_X_Pos"]
        pokemon4_front_y_Morning_2 = mon_file["Front_Position"]["Morning_2_Y_Pos"]
        pokemon4_front_x_Morning_3 = mon_file["Front_Position"]["Morning_3_X_Pos"]
        pokemon4_front_y_Morning_3 = mon_file["Front_Position"]["Morning_3_Y_Pos"]
        pokemon4_front_x_Morning_4 = mon_file["Front_Position"]["Morning_4_X_Pos"]
        pokemon4_front_y_Morning_4 = mon_file["Front_Position"]["Morning_4_Y_Pos"]
        pokemon4_front_x_Morning_5 = mon_file["Front_Position"]["Morning_5_X_Pos"]
        pokemon4_front_y_Morning_5 = mon_file["Front_Position"]["Morning_5_Y_Pos"]
        pokemon4_front_x_Morning_6 = mon_file["Front_Position"]["Morning_6_X_Pos"]
        pokemon4_front_y_Morning_6 = mon_file["Front_Position"]["Morning_6_Y_Pos"]
        pokemon4_front_x_Morning_7 = mon_file["Front_Position"]["Morning_7_X_Pos"]
        pokemon4_front_y_Morning_7 = mon_file["Front_Position"]["Morning_7_Y_Pos"]
        pokemon4_front_x_Morning_8 = mon_file["Front_Position"]["Morning_8_X_Pos"]
        pokemon4_front_y_Morning_8 = mon_file["Front_Position"]["Morning_8_Y_Pos"]
        
        pokemon4_back_x_Morning_1 = mon_file["Back_Position"]["Morning_1_X_Pos"]
        pokemon4_back_y_Morning_1 = mon_file["Back_Position"]["Morning_1_Y_Pos"]
        pokemon4_back_x_Morning_2 = mon_file["Back_Position"]["Morning_2_X_Pos"]
        pokemon4_back_y_Morning_2 = mon_file["Back_Position"]["Morning_2_Y_Pos"]
        pokemon4_back_x_Morning_3 = mon_file["Back_Position"]["Morning_3_X_Pos"]
        pokemon4_back_y_Morning_3 = mon_file["Back_Position"]["Morning_3_Y_Pos"]
        pokemon4_back_x_Morning_4 = mon_file["Back_Position"]["Morning_4_X_Pos"]
        pokemon4_back_y_Morning_4 = mon_file["Back_Position"]["Morning_4_Y_Pos"]
        pokemon4_back_x_Morning_5 = mon_file["Back_Position"]["Morning_5_X_Pos"]
        pokemon4_back_y_Morning_5 = mon_file["Back_Position"]["Morning_5_Y_Pos"]
        pokemon4_back_x_Morning_6 = mon_file["Back_Position"]["Morning_6_X_Pos"]
        pokemon4_back_y_Morning_6 = mon_file["Back_Position"]["Morning_6_Y_Pos"]
        pokemon4_back_x_Morning_7 = mon_file["Back_Position"]["Morning_7_X_Pos"]
        pokemon4_back_y_Morning_7 = mon_file["Back_Position"]["Morning_7_Y_Pos"]
        pokemon4_back_x_Morning_8 = mon_file["Back_Position"]["Morning_8_X_Pos"]
        pokemon4_back_y_Morning_8 = mon_file["Back_Position"]["Morning_8_Y_Pos"]

        pokemon4_front_x_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_X_Pos"]
        pokemon4_front_y_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_Y_Pos"]
        pokemon4_front_x_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_X_Pos"]
        pokemon4_front_y_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_Y_Pos"]
        pokemon4_front_x_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_X_Pos"]
        pokemon4_front_y_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_Y_Pos"]
        pokemon4_front_x_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_X_Pos"]
        pokemon4_front_y_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_Y_Pos"]
        pokemon4_front_x_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_X_Pos"]
        pokemon4_front_y_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_Y_Pos"]
        pokemon4_front_x_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_X_Pos"]
        pokemon4_front_y_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_Y_Pos"]
        pokemon4_front_x_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_X_Pos"]
        pokemon4_front_y_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_Y_Pos"]
        pokemon4_front_x_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_X_Pos"]
        pokemon4_front_y_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_Y_Pos"]


        pokemon4_back_x_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_X_Pos"]
        pokemon4_back_y_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_Y_Pos"]
        pokemon4_back_x_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_X_Pos"]
        pokemon4_back_y_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_Y_Pos"]
        pokemon4_back_x_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_X_Pos"]
        pokemon4_back_y_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_Y_Pos"]
        pokemon4_back_x_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_X_Pos"]
        pokemon4_back_y_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_Y_Pos"]
        pokemon4_back_x_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_X_Pos"]
        pokemon4_back_y_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_Y_Pos"]
        pokemon4_back_x_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_X_Pos"]
        pokemon4_back_y_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_Y_Pos"]
        pokemon4_back_x_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_X_Pos"]
        pokemon4_back_y_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_Y_Pos"]
        pokemon4_back_x_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_X_Pos"]
        pokemon4_back_y_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_Y_Pos"]

        pokemon4_front_x_Night_1 = mon_file["Front_Position"]["Night_1_X_Pos"]
        pokemon4_front_y_Night_1 = mon_file["Front_Position"]["Night_1_Y_Pos"]
        pokemon4_front_x_Night_2 = mon_file["Front_Position"]["Night_2_X_Pos"]
        pokemon4_front_y_Night_2 = mon_file["Front_Position"]["Night_2_Y_Pos"]
        pokemon4_front_x_Night_3 = mon_file["Front_Position"]["Night_3_X_Pos"]
        pokemon4_front_y_Night_3 = mon_file["Front_Position"]["Night_3_Y_Pos"]
        pokemon4_front_x_Night_4 = mon_file["Front_Position"]["Night_4_X_Pos"]
        pokemon4_front_y_Night_4 = mon_file["Front_Position"]["Night_4_Y_Pos"]
        pokemon4_front_x_Night_5 = mon_file["Front_Position"]["Night_5_X_Pos"]
        pokemon4_front_y_Night_5 = mon_file["Front_Position"]["Night_5_Y_Pos"]
        pokemon4_front_x_Night_6 = mon_file["Front_Position"]["Night_6_X_Pos"]
        pokemon4_front_y_Night_6 = mon_file["Front_Position"]["Night_6_Y_Pos"]
        pokemon4_front_x_Night_7 = mon_file["Front_Position"]["Night_7_X_Pos"]
        pokemon4_front_y_Night_7 = mon_file["Front_Position"]["Night_7_Y_Pos"]
        pokemon4_front_x_Night_8 = mon_file["Front_Position"]["Night_8_X_Pos"]
        pokemon4_front_y_Night_8 = mon_file["Front_Position"]["Night_8_Y_Pos"]

        pokemon4_back_x_Night_1 = mon_file["Back_Position"]["Night_1_X_Pos"]
        pokemon4_back_y_Night_1 = mon_file["Back_Position"]["Night_1_Y_Pos"]
        pokemon4_back_x_Night_2 = mon_file["Back_Position"]["Night_2_X_Pos"]
        pokemon4_back_y_Night_2 = mon_file["Back_Position"]["Night_2_Y_Pos"]
        pokemon4_back_x_Night_3 = mon_file["Back_Position"]["Night_3_X_Pos"]
        pokemon4_back_y_Night_3 = mon_file["Back_Position"]["Night_3_Y_Pos"]
        pokemon4_back_x_Night_4 = mon_file["Back_Position"]["Night_4_X_Pos"]
        pokemon4_back_y_Night_4 = mon_file["Back_Position"]["Night_4_Y_Pos"]
        pokemon4_back_x_Night_5 = mon_file["Back_Position"]["Night_5_X_Pos"]
        pokemon4_back_y_Night_5 = mon_file["Back_Position"]["Night_5_Y_Pos"]
        pokemon4_back_x_Night_6 = mon_file["Back_Position"]["Night_6_X_Pos"]
        pokemon4_back_y_Night_6 = mon_file["Back_Position"]["Night_6_Y_Pos"]
        pokemon4_back_x_Night_7 = mon_file["Back_Position"]["Night_7_X_Pos"]
        pokemon4_back_y_Night_7 = mon_file["Back_Position"]["Night_7_Y_Pos"]
        pokemon4_back_x_Night_8 = mon_file["Back_Position"]["Night_8_X_Pos"]
        pokemon4_back_y_Night_8 = mon_file["Back_Position"]["Night_8_Y_Pos"]


        pokemon5_name = self.pokemon5_combo.currentText()
        pokemon5_move1 = self.pokemon5_move1.currentText()
        pokemon5_move2 = self.pokemon5_move2.currentText()
        pokemon5_move3 = self.pokemon5_move3.currentText()
        pokemon5_move4 = self.pokemon5_move4.currentText()
        pokemon5_level = self.pokemon5_level.value()
        pokemon5_item = self.pokemon5_item.currentText()
        with open("battle_system/pokemon_data/" + pokemon5_name + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon5_base_hp = mon_file["Stats"]["HP"]
        pokemon5_base_attack = mon_file["Stats"]["Attack"]
        pokemon5_base_defense = mon_file["Stats"]["Defense"]
        pokemon5_base_sp_atk = mon_file["Stats"]["Sp. Atk"]
        pokemon5_base_sp_def = mon_file["Stats"]["Sp. Def"]
        pokemon5_base_speed = mon_file["Stats"]["Speed"]
        pokemon5_icon = mon_file["Resource_data"]["Image_dir"] + "icon.png"
        pokemon5_front = mon_file["Resource_data"]["Image_dir"] + pokemon5_name + "_front.png"
        pokemon5_back = mon_file["Resource_data"]["Image_dir"] + pokemon5_name + "_back.png"

        pokemon5_max_hp = math.floor(((2 * pokemon5_base_hp + 28 + 1) * (pokemon1_level / 100) + pokemon1_level + 10))
        pokemon5_max_attack = math.floor((2 * pokemon5_base_attack + 4 + 0) * ((pokemon1_base_attack / 100) + 5) * 0.9)
        pokemon5_max_defense = math.floor((2 * pokemon5_base_defense + 4 + 0) * ((pokemon5_base_defense / 100) + 5) * 0.9)
        pokemon5_max_sp_atk = math.floor((2 * pokemon5_base_sp_atk + 4 + 0) * ((pokemon5_base_sp_atk / 100) + 5) * 0.9)
        pokemon5_max_sp_def = math.floor((2 * pokemon5_base_sp_def + 4 + 0) * ((pokemon5_base_sp_def / 100) + 5) * 0.9)
        pokemon5_max_speed = math.floor((2 * pokemon5_base_speed + 4 + 0) * ((pokemon5_base_speed / 100) + 5) * 0.9)
        # Hard code the values for the backgrounds
        pokemon5_front_x_Morning_1 = mon_file["Front_Position"]["Morning_1_X_Pos"]
        pokemon5_front_y_Morning_1 = mon_file["Front_Position"]["Morning_1_Y_Pos"]
        pokemon5_front_x_Morning_2 = mon_file["Front_Position"]["Morning_2_X_Pos"]
        pokemon5_front_y_Morning_2 = mon_file["Front_Position"]["Morning_2_Y_Pos"]
        pokemon5_front_x_Morning_3 = mon_file["Front_Position"]["Morning_3_X_Pos"]
        pokemon5_front_y_Morning_3 = mon_file["Front_Position"]["Morning_3_Y_Pos"]
        pokemon5_front_x_Morning_4 = mon_file["Front_Position"]["Morning_4_X_Pos"]
        pokemon5_front_y_Morning_4 = mon_file["Front_Position"]["Morning_4_Y_Pos"]
        pokemon5_front_x_Morning_5 = mon_file["Front_Position"]["Morning_5_X_Pos"]
        pokemon5_front_y_Morning_5 = mon_file["Front_Position"]["Morning_5_Y_Pos"]
        pokemon5_front_x_Morning_6 = mon_file["Front_Position"]["Morning_6_X_Pos"]
        pokemon5_front_y_Morning_6 = mon_file["Front_Position"]["Morning_6_Y_Pos"]
        pokemon5_front_x_Morning_7 = mon_file["Front_Position"]["Morning_7_X_Pos"]
        pokemon5_front_y_Morning_7 = mon_file["Front_Position"]["Morning_7_Y_Pos"]
        pokemon5_front_x_Morning_8 = mon_file["Front_Position"]["Morning_8_X_Pos"]
        pokemon5_front_y_Morning_8 = mon_file["Front_Position"]["Morning_8_Y_Pos"]


        pokemon5_back_x_Morning_1 = mon_file["Back_Position"]["Morning_1_X_Pos"]
        pokemon5_back_y_Morning_1 = mon_file["Back_Position"]["Morning_1_Y_Pos"]
        pokemon5_back_x_Morning_2 = mon_file["Back_Position"]["Morning_2_X_Pos"]
        pokemon5_back_y_Morning_2 = mon_file["Back_Position"]["Morning_2_Y_Pos"]
        pokemon5_back_x_Morning_3 = mon_file["Back_Position"]["Morning_3_X_Pos"]
        pokemon5_back_y_Morning_3 = mon_file["Back_Position"]["Morning_3_Y_Pos"]
        pokemon5_back_x_Morning_4 = mon_file["Back_Position"]["Morning_4_X_Pos"]
        pokemon5_back_y_Morning_4 = mon_file["Back_Position"]["Morning_4_Y_Pos"]
        pokemon5_back_x_Morning_5 = mon_file["Back_Position"]["Morning_5_X_Pos"]
        pokemon5_back_y_Morning_5 = mon_file["Back_Position"]["Morning_5_Y_Pos"]
        pokemon5_back_x_Morning_6 = mon_file["Back_Position"]["Morning_6_X_Pos"]
        pokemon5_back_y_Morning_6 = mon_file["Back_Position"]["Morning_6_Y_Pos"]
        pokemon5_back_x_Morning_7 = mon_file["Back_Position"]["Morning_7_X_Pos"]
        pokemon5_back_y_Morning_7 = mon_file["Back_Position"]["Morning_7_Y_Pos"]
        pokemon5_back_x_Morning_8 = mon_file["Back_Position"]["Morning_8_X_Pos"]
        pokemon5_back_y_Morning_8 = mon_file["Back_Position"]["Morning_8_Y_Pos"]


        pokemon5_front_x_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_X_Pos"]
        pokemon5_front_y_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_Y_Pos"]
        pokemon5_front_x_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_X_Pos"]
        pokemon5_front_y_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_Y_Pos"]
        pokemon5_front_x_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_X_Pos"]
        pokemon5_front_y_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_Y_Pos"]
        pokemon5_front_x_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_X_Pos"]
        pokemon5_front_y_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_Y_Pos"]
        pokemon5_front_x_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_X_Pos"]
        pokemon5_front_y_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_Y_Pos"]
        pokemon5_front_x_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_X_Pos"]
        pokemon5_front_y_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_Y_Pos"]
        pokemon5_front_x_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_X_Pos"]
        pokemon5_front_y_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_Y_Pos"]
        pokemon5_front_x_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_X_Pos"]
        pokemon5_front_y_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_Y_Pos"]


        pokemon5_back_x_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_X_Pos"]
        pokemon5_back_y_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_Y_Pos"]
        pokemon5_back_x_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_X_Pos"]
        pokemon5_back_y_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_Y_Pos"]
        pokemon5_back_x_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_X_Pos"]
        pokemon5_back_y_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_Y_Pos"]
        pokemon5_back_x_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_X_Pos"]
        pokemon5_back_y_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_Y_Pos"]
        pokemon5_back_x_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_X_Pos"]
        pokemon5_back_y_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_Y_Pos"]
        pokemon5_back_x_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_X_Pos"]
        pokemon5_back_y_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_Y_Pos"]
        pokemon5_back_x_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_X_Pos"]
        pokemon5_back_y_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_Y_Pos"]
        pokemon5_back_x_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_X_Pos"]
        pokemon5_back_y_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_Y_Pos"]


        pokemon5_front_x_Night_1 = mon_file["Front_Position"]["Night_1_X_Pos"]
        pokemon5_front_y_Night_1 = mon_file["Front_Position"]["Night_1_Y_Pos"]
        pokemon5_front_x_Night_2 = mon_file["Front_Position"]["Night_2_X_Pos"]
        pokemon5_front_y_Night_2 = mon_file["Front_Position"]["Night_2_Y_Pos"]
        pokemon5_front_x_Night_3 = mon_file["Front_Position"]["Night_3_X_Pos"]
        pokemon5_front_y_Night_3 = mon_file["Front_Position"]["Night_3_Y_Pos"]
        pokemon5_front_x_Night_4 = mon_file["Front_Position"]["Night_4_X_Pos"]
        pokemon5_front_y_Night_4 = mon_file["Front_Position"]["Night_4_Y_Pos"]
        pokemon5_front_x_Night_5 = mon_file["Front_Position"]["Night_5_X_Pos"]
        pokemon5_front_y_Night_5 = mon_file["Front_Position"]["Night_5_Y_Pos"]
        pokemon5_front_x_Night_6 = mon_file["Front_Position"]["Night_6_X_Pos"]
        pokemon5_front_y_Night_6 = mon_file["Front_Position"]["Night_6_Y_Pos"]
        pokemon5_front_x_Night_7 = mon_file["Front_Position"]["Night_7_X_Pos"]
        pokemon5_front_y_Night_7 = mon_file["Front_Position"]["Night_7_Y_Pos"]
        pokemon5_front_x_Night_8 = mon_file["Front_Position"]["Night_8_X_Pos"]
        pokemon5_front_y_Night_8 = mon_file["Front_Position"]["Night_8_Y_Pos"]
        

        pokemon5_back_x_Night_1 = mon_file["Back_Position"]["Night_1_X_Pos"]
        pokemon5_back_y_Night_1 = mon_file["Back_Position"]["Night_1_Y_Pos"]
        pokemon5_back_x_Night_2 = mon_file["Back_Position"]["Night_2_X_Pos"]
        pokemon5_back_y_Night_2 = mon_file["Back_Position"]["Night_2_Y_Pos"]
        pokemon5_back_x_Night_3 = mon_file["Back_Position"]["Night_3_X_Pos"]
        pokemon5_back_y_Night_3 = mon_file["Back_Position"]["Night_3_Y_Pos"]
        pokemon5_back_x_Night_4 = mon_file["Back_Position"]["Night_4_X_Pos"]
        pokemon5_back_y_Night_4 = mon_file["Back_Position"]["Night_4_Y_Pos"]
        pokemon5_back_x_Night_5 = mon_file["Back_Position"]["Night_5_X_Pos"]
        pokemon5_back_y_Night_5 = mon_file["Back_Position"]["Night_5_Y_Pos"]
        pokemon5_back_x_Night_6 = mon_file["Back_Position"]["Night_6_X_Pos"]
        pokemon5_back_y_Night_6 = mon_file["Back_Position"]["Night_6_Y_Pos"]
        pokemon5_back_x_Night_7 = mon_file["Back_Position"]["Night_7_X_Pos"]
        pokemon5_back_y_Night_7 = mon_file["Back_Position"]["Night_7_Y_Pos"]
        pokemon5_back_x_Night_8 = mon_file["Back_Position"]["Night_8_X_Pos"]
        pokemon5_back_y_Night_8 = mon_file["Back_Position"]["Night_8_Y_Pos"]

        pokemon6_name = self.pokemon6_combo.currentText()
        pokemon6_move1 = self.pokemon6_move1.currentText()
        pokemon6_move2 = self.pokemon6_move2.currentText()
        pokemon6_move3 = self.pokemon6_move3.currentText()
        pokemon6_move4 = self.pokemon6_move4.currentText()
        pokemon6_level = self.pokemon6_level.value()
        pokemon6_item = self.pokemon6_item.currentText()
        with open("battle_system/pokemon_data/" + pokemon6_name + ".json", "r") as loop:
                    mon_file = json.load(loop)
        pokemon6_base_hp = mon_file["Stats"]["HP"]
        pokemon6_base_attack = mon_file["Stats"]["Attack"]
        pokemon6_base_defense = mon_file["Stats"]["Defense"]
        pokemon6_base_sp_atk = mon_file["Stats"]["Sp. Atk"]
        pokemon6_base_sp_def = mon_file["Stats"]["Sp. Def"]
        pokemon6_base_speed = mon_file["Stats"]["Speed"]
        pokemon6_icon = mon_file["Resource_data"]["Image_dir"] + "icon.png"
        pokemon6_front = mon_file["Resource_data"]["Image_dir"] + pokemon6_name + "_front.png"
        pokemon6_back = mon_file["Resource_data"]["Image_dir"] + pokemon6_name + "_back.png"

        pokemon6_max_hp = math.floor(((2 * pokemon1_base_hp + 28 + 1) * (pokemon1_level / 100) + pokemon1_level + 10))
        pokemon6_max_attack = math.floor((2 * pokemon6_base_attack + 4 + 0) * ((pokemon6_base_attack / 100) + 5) * 0.9)
        pokemon6_max_defense = math.floor((2 * pokemon6_base_defense + 4 + 0) * ((pokemon6_base_defense / 100) + 5) * 0.9)
        pokemon6_max_sp_atk = math.floor((2 * pokemon6_base_sp_atk + 4 + 0) * ((pokemon6_base_sp_atk / 100) + 5) * 0.9)
        pokemon6_max_sp_def = math.floor((2 * pokemon6_base_sp_def + 4 + 0) * ((pokemon6_base_sp_def / 100) + 5) * 0.9)
        pokemon6_max_speed = math.floor((2 * pokemon6_base_speed + 4 + 0) * ((pokemon6_base_speed / 100) + 5) * 0.9)

        # Hard code the values for the backgrounds
        pokemon6_front_x_Morning_1 = mon_file["Front_Position"]["Morning_1_X_Pos"]
        pokemon6_front_y_Morning_1 = mon_file["Front_Position"]["Morning_1_Y_Pos"]
        pokemon6_front_x_Morning_2 = mon_file["Front_Position"]["Morning_2_X_Pos"]
        pokemon6_front_y_Morning_2 = mon_file["Front_Position"]["Morning_2_Y_Pos"]
        pokemon6_front_x_Morning_3 = mon_file["Front_Position"]["Morning_3_X_Pos"]
        pokemon6_front_y_Morning_3 = mon_file["Front_Position"]["Morning_3_Y_Pos"]
        pokemon6_front_x_Morning_4 = mon_file["Front_Position"]["Morning_4_X_Pos"]
        pokemon6_front_y_Morning_4 = mon_file["Front_Position"]["Morning_4_Y_Pos"]
        pokemon6_front_x_Morning_5 = mon_file["Front_Position"]["Morning_5_X_Pos"]
        pokemon6_front_y_Morning_5 = mon_file["Front_Position"]["Morning_5_Y_Pos"]
        pokemon6_front_x_Morning_6 = mon_file["Front_Position"]["Morning_6_X_Pos"]
        pokemon6_front_y_Morning_6 = mon_file["Front_Position"]["Morning_6_Y_Pos"]
        pokemon6_front_x_Morning_7 = mon_file["Front_Position"]["Morning_7_X_Pos"]
        pokemon6_front_y_Morning_7 = mon_file["Front_Position"]["Morning_7_Y_Pos"]
        pokemon6_front_x_Morning_8 = mon_file["Front_Position"]["Morning_8_X_Pos"]
        pokemon6_front_y_Morning_8 = mon_file["Front_Position"]["Morning_8_Y_Pos"]

        pokemon6_back_x_Morning_1 = mon_file["Back_Position"]["Morning_1_X_Pos"]
        pokemon6_back_y_Morning_1 = mon_file["Back_Position"]["Morning_1_Y_Pos"]
        pokemon6_back_x_Morning_2 = mon_file["Back_Position"]["Morning_2_X_Pos"]
        pokemon6_back_y_Morning_2 = mon_file["Back_Position"]["Morning_2_Y_Pos"]
        pokemon6_back_x_Morning_3 = mon_file["Back_Position"]["Morning_3_X_Pos"]
        pokemon6_back_y_Morning_3 = mon_file["Back_Position"]["Morning_3_Y_Pos"]
        pokemon6_back_x_Morning_4 = mon_file["Back_Position"]["Morning_4_X_Pos"]
        pokemon6_back_y_Morning_4 = mon_file["Back_Position"]["Morning_4_Y_Pos"]
        pokemon6_back_x_Morning_5 = mon_file["Back_Position"]["Morning_5_X_Pos"]
        pokemon6_back_y_Morning_5 = mon_file["Back_Position"]["Morning_5_Y_Pos"]
        pokemon6_back_x_Morning_6 = mon_file["Back_Position"]["Morning_6_X_Pos"]
        pokemon6_back_y_Morning_6 = mon_file["Back_Position"]["Morning_6_Y_Pos"]
        pokemon6_back_x_Morning_7 = mon_file["Back_Position"]["Morning_7_X_Pos"]
        pokemon6_back_y_Morning_7 = mon_file["Back_Position"]["Morning_7_Y_Pos"]
        pokemon6_back_x_Morning_8 = mon_file["Back_Position"]["Morning_8_X_Pos"]
        pokemon6_back_y_Morning_8 = mon_file["Back_Position"]["Morning_8_Y_Pos"]


        pokemon6_front_x_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_X_Pos"]
        pokemon6_front_y_Afternoon_1 = mon_file["Front_Position"]["Afternoon_1_Y_Pos"]
        pokemon6_front_x_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_X_Pos"]
        pokemon6_front_y_Afternoon_2 = mon_file["Front_Position"]["Afternoon_2_Y_Pos"]
        pokemon6_front_x_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_X_Pos"]
        pokemon6_front_y_Afternoon_3 = mon_file["Front_Position"]["Afternoon_3_Y_Pos"]
        pokemon6_front_x_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_X_Pos"]
        pokemon6_front_y_Afternoon_4 = mon_file["Front_Position"]["Afternoon_4_Y_Pos"]
        pokemon6_front_x_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_X_Pos"]
        pokemon6_front_y_Afternoon_5 = mon_file["Front_Position"]["Afternoon_5_Y_Pos"]
        pokemon6_front_x_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_X_Pos"]
        pokemon6_front_y_Afternoon_6 = mon_file["Front_Position"]["Afternoon_6_Y_Pos"]
        pokemon6_front_x_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_X_Pos"]
        pokemon6_front_y_Afternoon_7 = mon_file["Front_Position"]["Afternoon_7_Y_Pos"]
        pokemon6_front_x_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_X_Pos"]
        pokemon6_front_y_Afternoon_8 = mon_file["Front_Position"]["Afternoon_8_Y_Pos"]


        pokemon6_back_x_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_X_Pos"]
        pokemon6_back_y_Afternoon_1 = mon_file["Back_Position"]["Afternoon_1_Y_Pos"]
        pokemon6_back_x_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_X_Pos"]
        pokemon6_back_y_Afternoon_2 = mon_file["Back_Position"]["Afternoon_2_Y_Pos"]
        pokemon6_back_x_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_X_Pos"]
        pokemon6_back_y_Afternoon_3 = mon_file["Back_Position"]["Afternoon_3_Y_Pos"]
        pokemon6_back_x_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_X_Pos"]
        pokemon6_back_y_Afternoon_4 = mon_file["Back_Position"]["Afternoon_4_Y_Pos"]
        pokemon6_back_x_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_X_Pos"]
        pokemon6_back_y_Afternoon_5 = mon_file["Back_Position"]["Afternoon_5_Y_Pos"]
        pokemon6_back_x_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_X_Pos"]
        pokemon6_back_y_Afternoon_6 = mon_file["Back_Position"]["Afternoon_6_Y_Pos"]
        pokemon6_back_x_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_X_Pos"]
        pokemon6_back_y_Afternoon_7 = mon_file["Back_Position"]["Afternoon_7_Y_Pos"]
        pokemon6_back_x_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_X_Pos"]
        pokemon6_back_y_Afternoon_8 = mon_file["Back_Position"]["Afternoon_8_Y_Pos"]

        pokemon6_front_x_Night_1 = mon_file["Front_Position"]["Night_1_X_Pos"]
        pokemon6_front_y_Night_1 = mon_file["Front_Position"]["Night_1_Y_Pos"]
        pokemon6_front_x_Night_2 = mon_file["Front_Position"]["Night_2_X_Pos"]
        pokemon6_front_y_Night_2 = mon_file["Front_Position"]["Night_2_Y_Pos"]
        pokemon6_front_x_Night_3 = mon_file["Front_Position"]["Night_3_X_Pos"]
        pokemon6_front_y_Night_3 = mon_file["Front_Position"]["Night_3_Y_Pos"]
        pokemon6_front_x_Night_4 = mon_file["Front_Position"]["Night_4_X_Pos"]
        pokemon6_front_y_Night_4 = mon_file["Front_Position"]["Night_4_Y_Pos"]
        pokemon6_front_x_Night_5 = mon_file["Front_Position"]["Night_5_X_Pos"]
        pokemon6_front_y_Night_5 = mon_file["Front_Position"]["Night_5_Y_Pos"]
        pokemon6_front_x_Night_6 = mon_file["Front_Position"]["Night_6_X_Pos"]
        pokemon6_front_y_Night_6 = mon_file["Front_Position"]["Night_6_Y_Pos"]
        pokemon6_front_x_Night_7 = mon_file["Front_Position"]["Night_7_X_Pos"]
        pokemon6_front_y_Night_7 = mon_file["Front_Position"]["Night_7_Y_Pos"]
        pokemon6_front_x_Night_8 = mon_file["Front_Position"]["Night_8_X_Pos"]
        pokemon6_front_y_Night_8 = mon_file["Front_Position"]["Night_8_Y_Pos"]


        pokemon6_back_x_Night_1 = mon_file["Back_Position"]["Night_1_X_Pos"]
        pokemon6_back_y_Night_1 = mon_file["Back_Position"]["Night_1_Y_Pos"]
        pokemon6_back_x_Night_2 = mon_file["Back_Position"]["Night_2_X_Pos"]
        pokemon6_back_y_Night_2 = mon_file["Back_Position"]["Night_2_Y_Pos"]
        pokemon6_back_x_Night_3 = mon_file["Back_Position"]["Night_3_X_Pos"]
        pokemon6_back_y_Night_3 = mon_file["Back_Position"]["Night_3_Y_Pos"]
        pokemon6_back_x_Night_4 = mon_file["Back_Position"]["Night_4_X_Pos"]
        pokemon6_back_y_Night_4 = mon_file["Back_Position"]["Night_4_Y_Pos"]
        pokemon6_back_x_Night_5 = mon_file["Back_Position"]["Night_5_X_Pos"]
        pokemon6_back_y_Night_5 = mon_file["Back_Position"]["Night_5_Y_Pos"]
        pokemon6_back_x_Night_6 = mon_file["Back_Position"]["Night_6_X_Pos"]
        pokemon6_back_y_Night_6 = mon_file["Back_Position"]["Night_6_Y_Pos"]
        pokemon6_back_x_Night_7 = mon_file["Back_Position"]["Night_7_X_Pos"]
        pokemon6_back_y_Night_7 = mon_file["Back_Position"]["Night_7_Y_Pos"]
        pokemon6_back_x_Night_8 = mon_file["Back_Position"]["Night_8_X_Pos"]
        pokemon6_back_y_Night_8 = mon_file["Back_Position"]["Night_8_Y_Pos"]
        """
        Begins the dump of data to JSON
        """
        data = {}
        data["Name"] = name
        data["Image_url"] = profile_image
        data["Pokemon1_Stats"] = [pokemon1_name, pokemon1_move1, pokemon1_move2, pokemon1_move3, pokemon1_move4, pokemon1_level, pokemon1_item, pokemon1_max_hp, pokemon1_max_attack, 
        pokemon1_max_defense, pokemon1_max_sp_atk, pokemon1_max_sp_def, pokemon1_max_speed, pokemon1_front, pokemon1_back, pokemon1_icon] 
        data["Pokemon1_Morning_1"] = [pokemon1_front_x_Morning_1, pokemon1_front_y_Morning_1, pokemon1_back_x_Morning_1, pokemon1_back_y_Morning_1]
        data["Pokemon1_Morning_2"] = [pokemon1_front_x_Morning_2, pokemon1_front_y_Morning_2, pokemon1_back_x_Morning_2, pokemon1_back_y_Morning_2]
        data["Pokemon1_Morning_3"] = [pokemon1_front_x_Morning_3, pokemon1_front_y_Morning_3, pokemon1_back_x_Morning_3, pokemon1_back_y_Morning_3]
        data["Pokemon1_Morning_4"] = [pokemon1_front_x_Morning_4, pokemon1_front_y_Morning_4, pokemon1_back_x_Morning_4, pokemon1_back_y_Morning_4]
        data["Pokemon1_Morning_5"] = [pokemon1_front_x_Morning_5, pokemon1_front_y_Morning_5, pokemon1_back_x_Morning_5, pokemon1_back_y_Morning_5]
        data["Pokemon1_Morning_6"] = [pokemon1_front_x_Morning_6, pokemon1_front_y_Morning_6, pokemon1_back_x_Morning_6, pokemon1_back_y_Morning_6]
        data["Pokemon1_Morning_7"] = [pokemon1_front_x_Morning_7, pokemon1_front_x_Morning_7, pokemon1_back_x_Morning_7, pokemon1_back_y_Morning_7]
        data["Pokemon1_Morning_8"] = [pokemon1_front_x_Morning_8, pokemon1_front_y_Morning_8, pokemon1_back_x_Morning_8, pokemon1_back_y_Morning_8]
        data["Pokemon1_Afternoon_1"] = [pokemon1_front_x_Afternoon_1, pokemon1_front_y_Afternoon_1, pokemon1_back_x_Afternoon_1, pokemon1_back_y_Afternoon_1]
        data["Pokemon1_Afternoon_2"] = [pokemon1_front_x_Afternoon_2, pokemon1_front_y_Afternoon_2, pokemon1_back_x_Afternoon_2, pokemon1_back_y_Afternoon_2]
        data["Pokemon1_Afternoon_3"] = [pokemon1_front_x_Afternoon_3, pokemon1_front_y_Afternoon_3, pokemon1_back_x_Afternoon_3, pokemon1_back_y_Afternoon_3]
        data["Pokemon1_Afternoon_4"] = [pokemon1_front_x_Afternoon_4, pokemon1_front_y_Afternoon_4, pokemon1_back_x_Afternoon_4, pokemon1_back_y_Afternoon_4]
        data["Pokemon1_Afternoon_5"] = [pokemon1_front_x_Afternoon_5, pokemon1_front_y_Afternoon_5, pokemon1_back_x_Afternoon_5, pokemon1_back_y_Afternoon_5]
        data["Pokemon1_Afternoon_6"] = [pokemon1_front_x_Afternoon_6, pokemon1_front_y_Afternoon_6, pokemon1_back_x_Afternoon_6, pokemon1_back_y_Afternoon_6]
        data["Pokemon1_Afternoon_7"] = [pokemon1_front_x_Afternoon_7, pokemon1_front_x_Afternoon_7, pokemon1_back_x_Afternoon_7, pokemon1_back_y_Afternoon_7]
        data["Pokemon1_Afternoon_8"] = [pokemon1_front_x_Afternoon_8, pokemon1_front_y_Afternoon_8, pokemon1_back_x_Afternoon_8, pokemon1_back_y_Afternoon_8]
        data["Pokemon1_Night_1"] = [pokemon1_front_x_Night_1, pokemon1_front_y_Night_1, pokemon1_back_x_Night_1, pokemon1_back_y_Night_1]
        data["Pokemon1_Night_2"] = [pokemon1_front_x_Night_2, pokemon1_front_y_Night_2, pokemon1_back_x_Night_2, pokemon1_back_y_Night_2]
        data["Pokemon1_Night_3"] = [pokemon1_front_x_Night_3, pokemon1_front_y_Night_3, pokemon1_back_x_Night_3, pokemon1_back_y_Night_3]
        data["Pokemon1_Night_4"] = [pokemon1_front_x_Night_4, pokemon1_front_y_Night_4, pokemon1_back_x_Night_4, pokemon1_back_y_Night_4]
        data["Pokemon1_Night_5"] = [pokemon1_front_x_Night_5, pokemon1_front_y_Night_5, pokemon1_back_x_Night_5, pokemon1_back_y_Night_5]
        data["Pokemon1_Night_6"] = [pokemon1_front_x_Night_6, pokemon1_front_y_Night_6, pokemon1_back_x_Night_6, pokemon1_back_y_Night_6]
        data["Pokemon1_Night_7"] = [pokemon1_front_x_Night_7, pokemon1_front_x_Night_7, pokemon1_back_x_Night_7, pokemon1_back_y_Night_7]
        data["Pokemon1_Night_8"] = [pokemon1_front_x_Night_8, pokemon1_front_y_Night_8, pokemon1_back_x_Night_8, pokemon1_back_y_Night_8]


        data["Pokemon2_Stats"] = [pokemon2_name, pokemon2_move1, pokemon2_move2, pokemon2_move3, pokemon2_move4, pokemon2_level, pokemon2_item, pokemon2_max_hp, pokemon2_max_attack, pokemon2_max_defense, pokemon2_max_sp_atk, pokemon2_max_sp_def, pokemon2_max_speed, pokemon2_front, pokemon2_back, pokemon2_icon]
        data["Pokemon2_Morning_1"] = [pokemon2_front_x_Morning_1, pokemon2_front_y_Morning_1, pokemon2_back_x_Morning_1, pokemon2_back_y_Morning_1]
        data["Pokemon2_Morning_2"] = [pokemon2_front_x_Morning_2, pokemon2_front_y_Morning_2, pokemon2_back_x_Morning_2, pokemon2_back_y_Morning_2]
        data["Pokemon2_Morning_3"] = [pokemon2_front_x_Morning_3, pokemon2_front_y_Morning_3, pokemon2_back_x_Morning_3, pokemon2_back_y_Morning_3]
        data["Pokemon2_Morning_4"] = [pokemon2_front_x_Morning_4, pokemon2_front_y_Morning_4, pokemon2_back_x_Morning_4, pokemon2_back_y_Morning_4]
        data["Pokemon2_Morning_5"] = [pokemon2_front_x_Morning_5, pokemon2_front_y_Morning_5, pokemon2_back_x_Morning_5, pokemon2_back_y_Morning_5]
        data["Pokemon2_Morning_6"] = [pokemon2_front_x_Morning_6, pokemon2_front_y_Morning_6, pokemon2_back_x_Morning_6, pokemon2_back_y_Morning_6]
        data["Pokemon2_Morning_7"] = [pokemon2_front_x_Morning_7, pokemon2_front_x_Morning_7, pokemon2_back_x_Morning_7, pokemon2_back_y_Morning_7]
        data["Pokemon2_Morning_8"] = [pokemon2_front_x_Morning_8, pokemon2_front_y_Morning_8, pokemon2_back_x_Morning_8, pokemon2_back_y_Morning_8]
        data["Pokemon2_Afternoon_1"] = [pokemon2_front_x_Afternoon_1, pokemon2_front_y_Afternoon_1, pokemon2_back_x_Afternoon_1, pokemon2_back_y_Afternoon_1]
        data["Pokemon2_Afternoon_2"] = [pokemon2_front_x_Afternoon_2, pokemon2_front_y_Afternoon_2, pokemon2_back_x_Afternoon_2, pokemon2_back_y_Afternoon_2]
        data["Pokemon2_Afternoon_3"] = [pokemon2_front_x_Afternoon_3, pokemon2_front_y_Afternoon_3, pokemon2_back_x_Afternoon_3, pokemon2_back_y_Afternoon_3]
        data["Pokemon2_Afternoon_4"] = [pokemon2_front_x_Afternoon_4, pokemon2_front_y_Afternoon_4, pokemon2_back_x_Afternoon_4, pokemon2_back_y_Afternoon_4]
        data["Pokemon2_Afternoon_5"] = [pokemon2_front_x_Afternoon_5, pokemon2_front_y_Afternoon_5, pokemon2_back_x_Afternoon_5, pokemon2_back_y_Afternoon_5]
        data["Pokemon2_Afternoon_6"] = [pokemon2_front_x_Afternoon_6, pokemon2_front_y_Afternoon_6, pokemon2_back_x_Afternoon_6, pokemon2_back_y_Afternoon_6]
        data["Pokemon2_Afternoon_7"] = [pokemon2_front_x_Afternoon_7, pokemon2_front_x_Afternoon_7, pokemon2_back_x_Afternoon_7, pokemon2_back_y_Afternoon_7]
        data["Pokemon2_Afternoon_8"] = [pokemon2_front_x_Afternoon_8, pokemon2_front_y_Afternoon_8, pokemon2_back_x_Afternoon_8, pokemon2_back_y_Afternoon_8]
        data["Pokemon2_Night_1"] = [pokemon2_front_x_Night_1, pokemon2_front_y_Night_1, pokemon2_back_x_Night_1, pokemon2_back_y_Night_1]
        data["Pokemon2_Night_2"] = [pokemon2_front_x_Night_2, pokemon2_front_y_Night_2, pokemon2_back_x_Night_2, pokemon2_back_y_Night_2]
        data["Pokemon2_Night_3"] = [pokemon2_front_x_Night_3, pokemon2_front_y_Night_3, pokemon2_back_x_Night_3, pokemon2_back_y_Night_3]
        data["Pokemon2_Night_4"] = [pokemon2_front_x_Night_4, pokemon2_front_y_Night_4, pokemon2_back_x_Night_4, pokemon2_back_y_Night_4]
        data["Pokemon2_Night_5"] = [pokemon2_front_x_Night_5, pokemon2_front_y_Night_5, pokemon2_back_x_Night_5, pokemon2_back_y_Night_5]
        data["Pokemon2_Night_6"] = [pokemon2_front_x_Night_6, pokemon2_front_y_Night_6, pokemon2_back_x_Night_6, pokemon2_back_y_Night_6]
        data["Pokemon2_Night_7"] = [pokemon2_front_x_Night_7, pokemon2_front_x_Night_7, pokemon2_back_x_Night_7, pokemon2_back_y_Night_7]
        data["Pokemon2_Night_8"] = [pokemon2_front_x_Night_8, pokemon2_front_y_Night_8, pokemon2_back_x_Night_8, pokemon2_back_y_Night_8]


        data["Pokemon3_Stats"] = [pokemon3_name, pokemon3_move1, pokemon3_move2, pokemon3_move3, pokemon3_move4, pokemon3_level, pokemon3_item, pokemon3_max_hp, pokemon3_max_attack, pokemon3_max_defense, pokemon3_max_sp_atk, pokemon3_max_sp_def, pokemon3_max_speed, pokemon3_front, pokemon3_back, pokemon3_icon]
        data["Pokemon3_Morning_1"] = [pokemon3_front_x_Morning_1, pokemon3_front_y_Morning_1, pokemon3_back_x_Morning_1, pokemon3_back_y_Morning_1]
        data["Pokemon3_Morning_2"] = [pokemon3_front_x_Morning_2, pokemon3_front_y_Morning_2, pokemon3_back_x_Morning_2, pokemon3_back_y_Morning_2]
        data["Pokemon3_Morning_3"] = [pokemon3_front_x_Morning_3, pokemon3_front_y_Morning_3, pokemon3_back_x_Morning_3, pokemon3_back_y_Morning_3]
        data["Pokemon3_Morning_4"] = [pokemon3_front_x_Morning_4, pokemon3_front_y_Morning_4, pokemon3_back_x_Morning_4, pokemon3_back_y_Morning_4]
        data["Pokemon3_Morning_5"] = [pokemon3_front_x_Morning_5, pokemon3_front_y_Morning_5, pokemon3_back_x_Morning_5, pokemon3_back_y_Morning_5]
        data["Pokemon3_Morning_6"] = [pokemon3_front_x_Morning_6, pokemon3_front_y_Morning_6, pokemon3_back_x_Morning_6, pokemon3_back_y_Morning_6]
        data["Pokemon3_Morning_7"] = [pokemon3_front_x_Morning_7, pokemon3_front_x_Morning_7, pokemon3_back_x_Morning_7, pokemon3_back_y_Morning_7]
        data["Pokemon3_Morning_8"] = [pokemon3_front_x_Morning_8, pokemon3_front_y_Morning_8, pokemon3_back_x_Morning_8, pokemon3_back_y_Morning_8]
        data["Pokemon3_Afternoon_1"] = [pokemon3_front_x_Afternoon_1, pokemon3_front_y_Afternoon_1, pokemon3_back_x_Afternoon_1, pokemon3_back_y_Afternoon_1]
        data["Pokemon3_Afternoon_2"] = [pokemon3_front_x_Afternoon_2, pokemon3_front_y_Afternoon_2, pokemon3_back_x_Afternoon_2, pokemon3_back_y_Afternoon_2]
        data["Pokemon3_Afternoon_3"] = [pokemon3_front_x_Afternoon_3, pokemon3_front_y_Afternoon_3, pokemon3_back_x_Afternoon_3, pokemon3_back_y_Afternoon_3]
        data["Pokemon3_Afternoon_4"] = [pokemon3_front_x_Afternoon_4, pokemon3_front_y_Afternoon_4, pokemon3_back_x_Afternoon_4, pokemon3_back_y_Afternoon_4]
        data["Pokemon3_Afternoon_5"] = [pokemon3_front_x_Afternoon_5, pokemon3_front_y_Afternoon_5, pokemon3_back_x_Afternoon_5, pokemon3_back_y_Afternoon_5]
        data["Pokemon3_Afternoon_6"] = [pokemon3_front_x_Afternoon_6, pokemon3_front_y_Afternoon_6, pokemon3_back_x_Afternoon_6, pokemon3_back_y_Afternoon_6]
        data["Pokemon3_Afternoon_7"] = [pokemon3_front_x_Afternoon_7, pokemon3_front_x_Afternoon_7, pokemon3_back_x_Afternoon_7, pokemon3_back_y_Afternoon_7]
        data["Pokemon3_Afternoon_8"] = [pokemon3_front_x_Afternoon_8, pokemon3_front_y_Afternoon_8, pokemon3_back_x_Afternoon_8, pokemon3_back_y_Afternoon_8]
        data["Pokemon3_Night_1"] = [pokemon3_front_x_Night_1, pokemon3_front_y_Night_1, pokemon3_back_x_Night_1, pokemon3_back_y_Night_1]
        data["Pokemon3_Night_2"] = [pokemon3_front_x_Night_2, pokemon3_front_y_Night_2, pokemon3_back_x_Night_2, pokemon3_back_y_Night_2]
        data["Pokemon3_Night_3"] = [pokemon3_front_x_Night_3, pokemon3_front_y_Night_3, pokemon3_back_x_Night_3, pokemon3_back_y_Night_3]
        data["Pokemon3_Night_4"] = [pokemon3_front_x_Night_4, pokemon3_front_y_Night_4, pokemon3_back_x_Night_4, pokemon3_back_y_Night_4]
        data["Pokemon3_Night_5"] = [pokemon3_front_x_Night_5, pokemon3_front_y_Night_5, pokemon3_back_x_Night_5, pokemon3_back_y_Night_5]
        data["Pokemon3_Night_6"] = [pokemon3_front_x_Night_6, pokemon3_front_y_Night_6, pokemon3_back_x_Night_6, pokemon3_back_y_Night_6]
        data["Pokemon3_Night_7"] = [pokemon3_front_x_Night_7, pokemon3_front_x_Night_7, pokemon3_back_x_Night_7, pokemon3_back_y_Night_7]
        data["Pokemon3_Night_8"] = [pokemon3_front_x_Night_8, pokemon3_front_y_Night_8, pokemon3_back_x_Night_8, pokemon3_back_y_Night_8]


        data["Pokemon4_Stats"] = [pokemon4_name, pokemon4_move1, pokemon4_move2, pokemon4_move3, pokemon4_move4, pokemon4_level, pokemon4_item, pokemon4_max_hp, pokemon4_max_attack, pokemon4_max_defense, pokemon4_max_sp_atk, pokemon4_max_sp_def, pokemon4_max_speed, pokemon4_front, pokemon4_back, pokemon4_icon]
        data["Pokemon4_Morning_1"] = [pokemon4_front_x_Morning_1, pokemon4_front_y_Morning_1, pokemon4_back_x_Morning_1, pokemon4_back_y_Morning_1]
        data["Pokemon4_Morning_2"] = [pokemon4_front_x_Morning_2, pokemon4_front_y_Morning_2, pokemon4_back_x_Morning_2, pokemon4_back_y_Morning_2]
        data["Pokemon4_Morning_3"] = [pokemon4_front_x_Morning_3, pokemon4_front_y_Morning_3, pokemon4_back_x_Morning_3, pokemon4_back_y_Morning_3]
        data["Pokemon4_Morning_4"] = [pokemon4_front_x_Morning_4, pokemon4_front_y_Morning_4, pokemon4_back_x_Morning_4, pokemon4_back_y_Morning_4]
        data["Pokemon4_Morning_5"] = [pokemon4_front_x_Morning_5, pokemon4_front_y_Morning_5, pokemon4_back_x_Morning_5, pokemon4_back_y_Morning_5]
        data["Pokemon4_Morning_6"] = [pokemon4_front_x_Morning_6, pokemon4_front_y_Morning_6, pokemon4_back_x_Morning_6, pokemon4_back_y_Morning_6]
        data["Pokemon4_Morning_7"] = [pokemon4_front_x_Morning_7, pokemon4_front_x_Morning_7, pokemon4_back_x_Morning_7, pokemon4_back_y_Morning_7]
        data["Pokemon4_Morning_8"] = [pokemon4_front_x_Morning_8, pokemon4_front_y_Morning_8, pokemon4_back_x_Morning_8, pokemon4_back_y_Morning_8]
        data["Pokemon4_Afternoon_1"] = [pokemon4_front_x_Afternoon_1, pokemon4_front_y_Afternoon_1, pokemon4_back_x_Afternoon_1, pokemon4_back_y_Afternoon_1]
        data["Pokemon4_Afternoon_2"] = [pokemon4_front_x_Afternoon_2, pokemon4_front_y_Afternoon_2, pokemon4_back_x_Afternoon_2, pokemon4_back_y_Afternoon_2]
        data["Pokemon4_Afternoon_3"] = [pokemon4_front_x_Afternoon_3, pokemon4_front_y_Afternoon_3, pokemon4_back_x_Afternoon_3, pokemon4_back_y_Afternoon_3]
        data["Pokemon4_Afternoon_4"] = [pokemon4_front_x_Afternoon_4, pokemon4_front_y_Afternoon_4, pokemon4_back_x_Afternoon_4, pokemon4_back_y_Afternoon_4]
        data["Pokemon4_Afternoon_5"] = [pokemon4_front_x_Afternoon_5, pokemon4_front_y_Afternoon_5, pokemon4_back_x_Afternoon_5, pokemon4_back_y_Afternoon_5]
        data["Pokemon4_Afternoon_6"] = [pokemon4_front_x_Afternoon_6, pokemon4_front_y_Afternoon_6, pokemon4_back_x_Afternoon_6, pokemon4_back_y_Afternoon_6]
        data["Pokemon4_Afternoon_7"] = [pokemon4_front_x_Afternoon_7, pokemon4_front_x_Afternoon_7, pokemon4_back_x_Afternoon_7, pokemon4_back_y_Afternoon_7]
        data["Pokemon4_Afternoon_8"] = [pokemon4_front_x_Afternoon_8, pokemon4_front_y_Afternoon_8, pokemon4_back_x_Afternoon_8, pokemon4_back_y_Afternoon_8]
        data["Pokemon4_Night_1"] = [pokemon4_front_x_Night_1, pokemon4_front_y_Night_1, pokemon4_back_x_Night_1, pokemon4_back_y_Night_1]
        data["Pokemon4_Night_2"] = [pokemon4_front_x_Night_2, pokemon4_front_y_Night_2, pokemon4_back_x_Night_2, pokemon4_back_y_Night_2]
        data["Pokemon4_Night_3"] = [pokemon4_front_x_Night_3, pokemon4_front_y_Night_3, pokemon4_back_x_Night_3, pokemon4_back_y_Night_3]
        data["Pokemon4_Night_4"] = [pokemon4_front_x_Night_4, pokemon4_front_y_Night_4, pokemon4_back_x_Night_4, pokemon4_back_y_Night_4]
        data["Pokemon4_Night_5"] = [pokemon4_front_x_Night_5, pokemon4_front_y_Night_5, pokemon4_back_x_Night_5, pokemon4_back_y_Night_5]
        data["Pokemon4_Night_6"] = [pokemon4_front_x_Night_6, pokemon4_front_y_Night_6, pokemon4_back_x_Night_6, pokemon4_back_y_Night_6]
        data["Pokemon4_Night_7"] = [pokemon4_front_x_Night_7, pokemon4_front_x_Night_7, pokemon4_back_x_Night_7, pokemon4_back_y_Night_7]
        data["Pokemon4_Night_8"] = [pokemon4_front_x_Night_8, pokemon4_front_y_Night_8, pokemon4_back_x_Night_8, pokemon4_back_y_Night_8]


        data["Pokemon5_Stats"] = [pokemon5_name, pokemon5_move1, pokemon5_move2, pokemon5_move3, pokemon5_move4, pokemon5_level, pokemon5_item, pokemon5_max_hp, pokemon5_max_attack, pokemon5_max_defense, pokemon5_max_sp_atk, pokemon5_max_sp_def, pokemon5_max_speed, pokemon5_front, pokemon5_back, pokemon5_icon]
        data["Pokemon5_Morning_1"] = [pokemon5_front_x_Morning_1, pokemon5_front_y_Morning_1, pokemon5_back_x_Morning_1, pokemon5_back_y_Morning_1]
        data["Pokemon5_Morning_2"] = [pokemon5_front_x_Morning_2, pokemon5_front_y_Morning_2, pokemon5_back_x_Morning_2, pokemon5_back_y_Morning_2]
        data["Pokemon5_Morning_3"] = [pokemon5_front_x_Morning_3, pokemon5_front_y_Morning_3, pokemon5_back_x_Morning_3, pokemon5_back_y_Morning_3]
        data["Pokemon5_Morning_4"] = [pokemon5_front_x_Morning_4, pokemon5_front_y_Morning_4, pokemon5_back_x_Morning_4, pokemon5_back_y_Morning_4]
        data["Pokemon5_Morning_5"] = [pokemon5_front_x_Morning_5, pokemon5_front_y_Morning_5, pokemon5_back_x_Morning_5, pokemon5_back_y_Morning_5]
        data["Pokemon5_Morning_6"] = [pokemon5_front_x_Morning_6, pokemon5_front_y_Morning_6, pokemon5_back_x_Morning_6, pokemon5_back_y_Morning_6]
        data["Pokemon5_Morning_7"] = [pokemon5_front_x_Morning_7, pokemon5_front_x_Morning_7, pokemon5_back_x_Morning_7, pokemon5_back_y_Morning_7]
        data["Pokemon5_Morning_8"] = [pokemon5_front_x_Morning_8, pokemon5_front_y_Morning_8, pokemon5_back_x_Morning_8, pokemon5_back_y_Morning_8]
        data["Pokemon5_Afternoon_1"] = [pokemon5_front_x_Afternoon_1, pokemon5_front_y_Afternoon_1, pokemon5_back_x_Afternoon_1, pokemon5_back_y_Afternoon_1]
        data["Pokemon5_Afternoon_2"] = [pokemon5_front_x_Afternoon_2, pokemon5_front_y_Afternoon_2, pokemon5_back_x_Afternoon_2, pokemon5_back_y_Afternoon_2]
        data["Pokemon5_Afternoon_3"] = [pokemon5_front_x_Afternoon_3, pokemon5_front_y_Afternoon_3, pokemon5_back_x_Afternoon_3, pokemon5_back_y_Afternoon_3]
        data["Pokemon5_Afternoon_4"] = [pokemon5_front_x_Afternoon_4, pokemon5_front_y_Afternoon_4, pokemon5_back_x_Afternoon_4, pokemon5_back_y_Afternoon_4]
        data["Pokemon5_Afternoon_5"] = [pokemon5_front_x_Afternoon_5, pokemon5_front_y_Afternoon_5, pokemon5_back_x_Afternoon_5, pokemon5_back_y_Afternoon_5]
        data["Pokemon5_Afternoon_6"] = [pokemon5_front_x_Afternoon_6, pokemon5_front_y_Afternoon_6, pokemon5_back_x_Afternoon_6, pokemon5_back_y_Afternoon_6]
        data["Pokemon5_Afternoon_7"] = [pokemon5_front_x_Afternoon_7, pokemon5_front_x_Afternoon_7, pokemon5_back_x_Afternoon_7, pokemon5_back_y_Afternoon_7]
        data["Pokemon5_Afternoon_8"] = [pokemon5_front_x_Afternoon_8, pokemon5_front_y_Afternoon_8, pokemon5_back_x_Afternoon_8, pokemon5_back_y_Afternoon_8]
        data["Pokemon5_Night_1"] = [pokemon5_front_x_Night_1, pokemon5_front_y_Night_1, pokemon5_back_x_Night_1, pokemon5_back_y_Night_1]
        data["Pokemon5_Night_2"] = [pokemon5_front_x_Night_2, pokemon5_front_y_Night_2, pokemon5_back_x_Night_2, pokemon5_back_y_Night_2]
        data["Pokemon5_Night_3"] = [pokemon5_front_x_Night_3, pokemon5_front_y_Night_3, pokemon5_back_x_Night_3, pokemon5_back_y_Night_3]
        data["Pokemon5_Night_4"] = [pokemon5_front_x_Night_4, pokemon5_front_y_Night_4, pokemon5_back_x_Night_4, pokemon5_back_y_Night_4]
        data["Pokemon5_Night_5"] = [pokemon5_front_x_Night_5, pokemon5_front_y_Night_5, pokemon5_back_x_Night_5, pokemon5_back_y_Night_5]
        data["Pokemon5_Night_6"] = [pokemon5_front_x_Night_6, pokemon5_front_y_Night_6, pokemon5_back_x_Night_6, pokemon5_back_y_Night_6]
        data["Pokemon5_Night_7"] = [pokemon5_front_x_Night_7, pokemon5_front_x_Night_7, pokemon5_back_x_Night_7, pokemon5_back_y_Night_7]
        data["Pokemon5_Night_8"] = [pokemon5_front_x_Night_8, pokemon5_front_y_Night_8, pokemon5_back_x_Night_8, pokemon5_back_y_Night_8]


        data["Pokemon6_Stats"] = [pokemon6_name, pokemon6_move1, pokemon6_move2, pokemon6_move3, pokemon6_move4, pokemon6_level, pokemon6_item, pokemon6_max_hp, pokemon6_max_attack, pokemon6_max_defense, pokemon6_max_sp_atk, pokemon6_max_sp_def, pokemon6_max_speed, pokemon6_front, pokemon6_back, pokemon6_icon]

        data["Pokemon6_Morning_1"] = [pokemon6_front_x_Morning_1, pokemon6_front_y_Morning_1, pokemon6_back_x_Morning_1, pokemon6_back_y_Morning_1]
        data["Pokemon6_Morning_2"] = [pokemon6_front_x_Morning_2, pokemon6_front_y_Morning_2, pokemon6_back_x_Morning_2, pokemon6_back_y_Morning_2]
        data["Pokemon6_Morning_3"] = [pokemon6_front_x_Morning_3, pokemon6_front_y_Morning_3, pokemon6_back_x_Morning_3, pokemon6_back_y_Morning_3]
        data["Pokemon6_Morning_4"] = [pokemon6_front_x_Morning_4, pokemon6_front_y_Morning_4, pokemon6_back_x_Morning_4, pokemon6_back_y_Morning_4]
        data["Pokemon6_Morning_5"] = [pokemon6_front_x_Morning_5, pokemon6_front_y_Morning_5, pokemon6_back_x_Morning_5, pokemon6_back_y_Morning_5]
        data["Pokemon6_Morning_6"] = [pokemon6_front_x_Morning_6, pokemon6_front_y_Morning_6, pokemon6_back_x_Morning_6, pokemon6_back_y_Morning_6]
        data["Pokemon6_Morning_7"] = [pokemon6_front_x_Morning_7, pokemon6_front_x_Morning_7, pokemon6_back_x_Morning_7, pokemon6_back_y_Morning_7]
        data["Pokemon6_Morning_8"] = [pokemon6_front_x_Morning_8, pokemon6_front_y_Morning_8, pokemon6_back_x_Morning_8, pokemon6_back_y_Morning_8]
        data["Pokemon6_Afternoon_1"] = [pokemon6_front_x_Afternoon_1, pokemon6_front_y_Afternoon_1, pokemon6_back_x_Afternoon_1, pokemon6_back_y_Afternoon_1]
        data["Pokemon6_Afternoon_2"] = [pokemon6_front_x_Afternoon_2, pokemon6_front_y_Afternoon_2, pokemon6_back_x_Afternoon_2, pokemon6_back_y_Afternoon_2]
        data["Pokemon6_Afternoon_3"] = [pokemon6_front_x_Afternoon_3, pokemon6_front_y_Afternoon_3, pokemon6_back_x_Afternoon_3, pokemon6_back_y_Afternoon_3]
        data["Pokemon6_Afternoon_4"] = [pokemon6_front_x_Afternoon_4, pokemon6_front_y_Afternoon_4, pokemon6_back_x_Afternoon_4, pokemon6_back_y_Afternoon_4]
        data["Pokemon6_Afternoon_5"] = [pokemon6_front_x_Afternoon_5, pokemon6_front_y_Afternoon_5, pokemon6_back_x_Afternoon_5, pokemon6_back_y_Afternoon_5]
        data["Pokemon6_Afternoon_6"] = [pokemon6_front_x_Afternoon_6, pokemon6_front_y_Afternoon_6, pokemon6_back_x_Afternoon_6, pokemon6_back_y_Afternoon_6]
        data["Pokemon6_Afternoon_7"] = [pokemon6_front_x_Afternoon_7, pokemon6_front_x_Afternoon_7, pokemon6_back_x_Afternoon_7, pokemon6_back_y_Afternoon_7]
        data["Pokemon6_Afternoon_8"] = [pokemon6_front_x_Afternoon_8, pokemon6_front_y_Afternoon_8, pokemon6_back_x_Afternoon_8, pokemon6_back_y_Afternoon_8]
        data["Pokemon6_Night_1"] = [pokemon6_front_x_Night_1, pokemon6_front_y_Night_1, pokemon6_back_x_Night_1, pokemon6_back_y_Night_1]
        data["Pokemon6_Night_2"] = [pokemon6_front_x_Night_2, pokemon6_front_y_Night_2, pokemon6_back_x_Night_2, pokemon6_back_y_Night_2]
        data["Pokemon6_Night_3"] = [pokemon6_front_x_Night_3, pokemon6_front_y_Night_3, pokemon6_back_x_Night_3, pokemon6_back_y_Night_3]
        data["Pokemon6_Night_4"] = [pokemon6_front_x_Night_4, pokemon6_front_y_Night_4, pokemon6_back_x_Night_4, pokemon6_back_y_Night_4]
        data["Pokemon6_Night_5"] = [pokemon6_front_x_Night_5, pokemon6_front_y_Night_5, pokemon6_back_x_Night_5, pokemon6_back_y_Night_5]
        data["Pokemon6_Night_6"] = [pokemon6_front_x_Night_6, pokemon6_front_y_Night_6, pokemon6_back_x_Night_6, pokemon6_back_y_Night_6]
        data["Pokemon6_Night_7"] = [pokemon6_front_x_Night_7, pokemon6_front_x_Night_7, pokemon6_back_x_Night_7, pokemon6_back_y_Night_7]
        data["Pokemon6_Night_8"] = [pokemon6_front_x_Night_8, pokemon6_front_y_Night_8, pokemon6_back_x_Night_8, pokemon6_back_y_Night_8]
        
        file = open("trainer_data/" + name + ".json", "w")

        # Dumps the data to the file
        json.dump(data, file, indent = 1)
        file.close()