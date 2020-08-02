import pygame
import os
import json
import glob
import random
from pathlib import Path
from pypresence import Presence
from pygame.locals import *
import sys
from require import require
status_screen_util = require("localhost_utils/status_screen_util.py")
"""
Created by Abrahan Nevarez
zenith110 - Github
https://www.linkedin.com/in/abrahan-nevarez/ - Linkedin
https://github.com/zenith110/pokemon_battle_sim - Repo
"""

"""
Selects the music using the path provided, and the extension that will be used
"""
def select_music(string_of_music_dir, player):
    music_list = []
    for path in Path(string_of_music_dir).rglob('*.ogg'):
        path = str(path).replace("\\", "/")
        music_list.append(str(path))
    music = random.choice(music_list)
    selection = str(music).replace("assets/resources/music/", "").replace(".ogg", "")
    player.music = selection
    return music

"""
Sets up the configuration and the music, then lead to the status screen
"""
def start_game(player, opponent, rpc):
    pygame.init()
    with open("assets/config/game_config.json", "r") as loop:
                gameconfig = json.load(loop)
    
    width = gameconfig["Resolution"]["Width"]
    height = gameconfig["Resolution"]["Height"]
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pokemon Battle Sim")
    screen = pygame.display.set_mode(size)
    screenB = pygame.display.set_mode((500,195), 0, 32)
    music_string = select_music('assets/resources/music/', player)
    pygame.mixer.music.load(music_string)
    pygame.mixer.music.play(-1)
    status_screen = pygame.image.load("assets/resources/graphics/battle_ui/status_screen.png").convert_alpha()
    status_screen_util.status_screen_state(player, opponent, screen, status_screen, rpc, screenB)

pygame.quit()