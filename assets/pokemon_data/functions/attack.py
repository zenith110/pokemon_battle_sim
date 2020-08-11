import json
def read_attack(file):
    with open(file, "r") as loop:
        data = json.load(loop)
    return data["Stats"]["Attack"]