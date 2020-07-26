import json
import unittest
from sp_attack import read_sp_attack
from glob import glob
import re
class Sp_Attack_Test(unittest.TestCase):
    def test_sp_attack(self):
        pokemon = []
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the sp attack test case")
            self.assertGreater(read_sp_attack(i), 0)
            
                
            
            