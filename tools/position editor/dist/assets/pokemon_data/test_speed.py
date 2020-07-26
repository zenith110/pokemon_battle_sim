import json
import unittest
from speed import read_speed
from glob import glob
import re
class Speed_Test(unittest.TestCase):
    def test_speed(self):
        pokemon = []
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the speed test case")
            self.assertGreater(read_speed(i), 0)
            
                
            
            