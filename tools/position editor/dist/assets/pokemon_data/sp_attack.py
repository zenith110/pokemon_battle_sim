import json
def read_sp_attack(file):
    with open(file, "r") as loop:
        data = json.load(loop)
    return data["Stats"]["Sp. Atk"]