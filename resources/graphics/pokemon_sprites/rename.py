# A batch script to automate the pokemon graphic folder
# Credits to Abrahan/HackerOfDarkness
# ---- Instructions ----------------------------------#
# Change the file to whatever text file that holds the name #
# Change the directory of where your pokeemerald pokemon graphics are stored #
import os
import re
from shutil import move
import glob
# Opens the directory that stores the names
PokemonNames = []
with open('pokemon_names.txt') as f1:
    # Loops through the contents of the file
    for name in f1:
        content = f1.readline()
        # Splits the names of the pokemon file so they're in the proper text format
        new_name = (content.split('\n')[0])
        PokemonNames.append(new_name)

        

# Renaming files in the directory       
# Changes directory to where the pokemon are stored        
i = 0     
for f in (filename for filename in glob.iglob('*') if '.png' in filename):
    f_name, f_ext = (os.path.splitext(f))
    digit_name = PokemonNames[i]
    print(digit_name)
    move(f,digit_name + ".png")
    i+=1