import json
def read_speed(file):
    with open(file, "r") as loop:
        data = json.load(loop)
    return data["Stats"]["Speed"]