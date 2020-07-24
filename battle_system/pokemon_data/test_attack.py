import json
import unittest
from attack import read_attack
from glob import glob
import re
class AttackTest(unittest.TestCase):
    def test_attack(self):
        pokemon = []
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        for i in pokemon:
            print(i + " is being run by the attack test case")
            self.assertGreater(read_attack(i), 0)
        