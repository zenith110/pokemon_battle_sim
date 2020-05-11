import os
from pathlib import Path
from PIL import Image
import sys
import shutil
import glob
# Created by hackerofdarkness for the usage of cropping sprites

# Lets us debug the image data
def printInfo(left, top, right, bottom, tag):
    print("The " + tag + " left value is: " + str(left) + "\nThe " + tag + " top value is: " + str(top)
    + "\nThe " + tag + " right value is: " + str(right) + "\nThe " + tag + " bottom value is: " + str(bottom) + "\n")

def imageCropper(pokemonImage, transparent): 
    pokemonName = pokemonImage.replace("_front.png", "")
    pokemonName = pokemonImage.replace("_back.png", "")
    pokemonName = pokemonImage.replace("_shiny_front.png", "")
    pokemonName = pokemonImage.replace("_shiny_back.png", "")
    pokemonFolder = Path(os.getcwd() + "/output/" + pokemonName).mkdir(parents= True, exist_ok= True)
    # Create an image
    image = (pokemonImage + ".png")
    originalSprite = Image.open(image)

    width, height = originalSprite.size

    # This is for the front sprite
    frontLeft = 0
    frontTop = 0
    frontRight = 64
    frontBottom = 64

    # Tags for debugging, simply pass it to debug and it'll add it to the command line
    front = "front"
    frontShiny = "front shiny"
    backShiny = "back shiny"
    back = "back"

    # This is for the shiny front sprite
    frontShinyLeft = 64
    frontShinyTop = 0
    frontShinyRight = 128
    frontShinyBottom = 64

    # This is for the regular back sprite
    backLeft = 128
    backTop = 0
    backRight = 192
    backBottom = 64

    # This is for the shiny back sprite
    backShinyLeft = 192
    backShinyTop = 0
    backShinyRight = 256 
    backShinyBottom = 64

    # Crops the individual images
    croppedFront = originalSprite.crop((frontLeft, frontTop, frontRight, frontBottom))
    croppedFrontShiny = originalSprite.crop((frontShinyLeft, frontShinyTop, frontShinyRight, frontShinyBottom))
    croppedBack = originalSprite.crop((backLeft, backTop, backRight, backBottom))
    croppedShinyBack = originalSprite.crop((backShinyLeft, backShinyTop, backShinyRight, backShinyBottom))
    
    # Saves the images to a file
    croppedFront.save(pokemonImage + "_front.png")
    croppedFrontShiny.save(pokemonImage + "_front_shiny.png")
    croppedBack.save(pokemonImage + "_back.png")
    croppedShinyBack.save(pokemonImage + "_shiny_back.png")
    print("Now making transparent")
     # Transparent change
    resizedFrontA = Image.open(pokemonImage + "_front.png")
    resizedFrontA.convert("RGBA")
    resizedFrontPixelData = resizedFrontA.load()
    resizedFrontData = resizedFrontA.getdata()
        
    if transparent:
        resizedFrontNewData = []
        for item in resizedFrontData:
            if item[0] == resizedFrontPixelData[0,0][0] and item[1] == resizedFrontPixelData[0,0][1] and item[2] == resizedFrontPixelData[0,0][2]:
                resizedFrontNewData.append((255,255,255,0))
            else:
                resizedFrontNewData.append(item)
        resizedFrontA.putdata(resizedFrontNewData)
        resizedFrontA.save(pokemonImage + "_front.png", "PNG")

    
    resizedFrontShinyA = Image.open(pokemonImage + "_front_shiny.png")
    resizedFrontShinyA.convert("RGBA")
    resizedFrontShinyPixelData = resizedFrontShinyA.load()
    resizedFrontShinyData = resizedFrontShinyA.getdata()
        
    if transparent:
        resizedFrontShinyNewData = []
        for item in resizedFrontShinyData:
            if item[0] == resizedFrontShinyPixelData[0,0][0] and item[1] == resizedFrontShinyPixelData[0,0][1] and item[2] == resizedFrontShinyPixelData[0,0][2]:
                resizedFrontShinyNewData.append((255,255,255,0))
            else:
                resizedFrontShinyNewData.append(item)
    resizedFrontShinyA.putdata(resizedFrontShinyNewData)
    resizedFrontShinyA.save(pokemonImage + "_front_shiny.png", "PNG")

           

    resizedBackA = Image.open(pokemonImage + "_back.png")
    resizedBackA.convert("RGBA")
    resizedBackPixelData = resizedBackA.load()
    resizedBackData = resizedBackA.getdata()
        
    if transparent:
        resizedBackNewData = []
        for item in resizedBackData:
            if item[0] == resizedBackPixelData[0,0][0] and item[1] == resizedBackPixelData[0,0][1] and item[2] == resizedBackPixelData[0,0][2]:
                resizedBackNewData.append((255,255,255,0))
            else:
                resizedBackNewData.append(item)
        resizedBackA.putdata(resizedBackNewData)
        resizedBackA.save(pokemonImage + "_back.png", "PNG")

    

    resizedBackShinyA = Image.open(pokemonImage + "_shiny_back.png")
    resizedBackShinyA.convert("RGBA")
    resizedBackShinyPixelData = resizedBackShinyA.load()
    resizedBackShinyData = resizedBackShinyA.getdata()
        
    if transparent:
        resizedBackShinyNewData = []
        for item in resizedBackShinyData:
            if item[0] == resizedBackShinyPixelData[0,0][0] and item[1] == resizedBackShinyPixelData[0,0][1] and item[2] == resizedBackShinyPixelData[0,0][2]:
                resizedBackShinyNewData.append((255,255,255,0))
            else:
                resizedBackShinyNewData.append(item)
    resizedBackShinyA.putdata(resizedBackShinyNewData)
    resizedBackShinyA.save(pokemonImage + "_shiny_back.png", "PNG")

    # Moves the images to the appropriate folder
    shutil.move(pokemonImage + "_front.png", "output/" + pokemonImage)
    shutil.move(pokemonImage + "_front_shiny.png", "output/" + pokemonImage)
    shutil.move(pokemonImage + "_back.png", "output/" + pokemonImage)
    shutil.move(pokemonImage + "_shiny_back.png", "output/" + pokemonImage)

    #printInfo(frontLeft, frontTop, frontRight, frontBottom, front)
    #printInfo(frontShinyLeft, frontShinyTop, frontShinyRight, frontShinyBottom, frontShiny)
    #printInfo(backLeft, backTop, backRight, backBottom, back)
    #printInfo(backShinyLeft, backShinyTop, backShinyRight, backShinyBottom, backShiny)

if __name__ == "__main__":
    i = 0
    listP = os.listdir()
    listP.sort()
    transparent = True
    # Loops through the entire folder
    for filename in (filename for filename in glob.iglob('*') if '.png' in filename):
        fileName, f_ext = os.path.splitext(filename)
        print("Now cropping " + filename)
        imageCropper(fileName, transparent)
        i += 1
    print("I finished with all the .png files")