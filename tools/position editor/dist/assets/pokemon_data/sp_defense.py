import json
def read_sp_defense(file):
    with open(file, "r") as loop:
        data = json.load(loop)
    return data["Stats"]["Sp. Def"]