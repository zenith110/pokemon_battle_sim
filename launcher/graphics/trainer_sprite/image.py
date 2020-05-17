import os
from pathlib import Path
from PIL import Image
import sys
import shutil
import glob
# Basic python script that makes all of our images transparent
def image_edit(trainer_image, transparent):
    trainer_sprite = Image.open(trainer_image + ".png")
    trainer_sprite.convert("RGBA")
    trainer_sprite_pixel_data = trainer_sprite.load()
    trainer_sprite_data = trainer_sprite.getdata()
        
    if transparent:
        resizedFrontNewData = []
        for item in trainer_sprite_data:
            if item[0] == trainer_sprite_pixel_data[0,0][0] and item[1] == trainer_sprite_pixel_data[0,0][1] and item[2] == trainer_sprite_pixel_data[0,0][2]:
                resizedFrontNewData.append((255,255,255,0))
            else:
                resizedFrontNewData.append(item)
        trainer_sprite.putdata(resizedFrontNewData)
        trainer_sprite.save(trainer_image + ".png", "PNG")

if __name__ == "__main__":
    i = 0
    listP = os.listdir()
    listP.sort()
    transparent = True
    # Loops through the entire folder
    for filename in (filename for filename in glob.iglob('*') if '.png' in filename):
        fileName, f_ext = os.path.splitext(filename)
        print("Now adding transparency " + filename)
        image_edit(fileName, transparent)
        i += 1
    print("I finished with all the .png files!")