import json
import unittest
from defense import read_defense
from glob import glob
import re
class Defense_Test(unittest.TestCase):
    def test_defense(self):
        pokemon = []
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the defense test case")
            self.assertGreater(read_defense(i), 0)
            
                
            
            