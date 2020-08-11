import json
import unittest
from glob import glob
import re
import os
from require import require
sp_attack = require("../functions/sp_attack.py")
class Sp_Attack_Test(unittest.TestCase):
    def test_sp_attack(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the sp attack test case")
            self.assertGreater(sp_attack.read_sp_attack(i), 0)
            
                
            
            