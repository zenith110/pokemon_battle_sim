import unittest
from glob import glob
import re
import os
from require import require
moves = require("../functions/moves.py")
class MoveTest(unittest.TestCase):
    def test_moves(self):
        pokemon = []
        os.chdir("../input")
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the move test case")
            self.assertGreater(moves.read_moves(i), 0)
            
                
            
            