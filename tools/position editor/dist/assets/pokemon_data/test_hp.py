import json
import unittest
from hp import read_hp
from glob import glob
import re
class HPTest(unittest.TestCase):
    def test_hp(self):
        pokemon = []
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the hp test case")
            self.assertGreater(read_hp(i), 0)
            
                
            
            