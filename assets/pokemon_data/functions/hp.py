import json
def read_hp(file):
    with open(file, "r") as loop:
        data = json.load(loop)
    return data["Stats"]["HP"]

