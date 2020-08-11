import json
import unittest
from glob import glob
import re
from require import require
import os
sp_defense = require("../functions/sp_defense.py")
class Sp_Defense_Test(unittest.TestCase):
    def test_sp_defense(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the sp_defense test case")
            self.assertGreater(sp_defense.read_sp_defense(i), 0)
            
                
            
            