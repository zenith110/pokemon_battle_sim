import json
import unittest
from glob import glob
import re
from require import require
import os
attack = require("../functions/attack.py")
class AttackTest(unittest.TestCase):
    def test_attack(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        for i in pokemon:
            print(i + " is being run by the attack test case")
            self.assertGreater(attack.read_attack(i), 0)
        