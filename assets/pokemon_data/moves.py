import json
def read_moves(file):
    with open(file, "r") as loop:
        data = json.load(loop)
    return len(data["Moves"])