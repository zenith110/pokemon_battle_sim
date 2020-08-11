import json
import unittest
from glob import glob
import re
from require import require
import os
defense = require("../functions/defense.py")
class Defense_Test(unittest.TestCase):
    def test_defense(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the defense test case")
            self.assertGreater(defense.read_defense(i), 0)
            
                
            
            