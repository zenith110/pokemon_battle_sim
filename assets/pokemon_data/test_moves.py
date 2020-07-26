import unittest
from moves import read_moves
from glob import glob
import re
class MoveTest(unittest.TestCase):
    def test_moves(self):
        pokemon = []
        for f_name in glob("[A-Z]*.json"):
            if re.match("list_of_pokemon.json", f_name):
                continue
            else:
                pokemon.append(f_name)
        print("\n")
        for i in pokemon:
            print(i + " is being run by the move test case")
            self.assertGreater(read_moves(i), 0)
            
                
            
            