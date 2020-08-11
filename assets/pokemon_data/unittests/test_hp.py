import json
import unittest
from glob import glob
import re
from require import require
import os
hp = require("../functions/hp.py")
class HPTest(unittest.TestCase):
    def test_hp(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the hp test case")
            self.assertGreater(hp.read_hp(i), 0)
            
                
            
            