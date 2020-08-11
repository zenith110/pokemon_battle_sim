import json
import unittest
from glob import glob
import re
import os
from require import require
speed = require("../functions/speed.py")
class Speed_Test(unittest.TestCase):
    def test_speed(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the speed test case")
            self.assertGreater(speed.read_speed(i), 0)
            
                
            
            