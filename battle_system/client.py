import pygame
import json
import glob
import random
from pathlib import Path
import time
from datetime import datetime
# Creates our colors
BLACK = (0, 0, 0)
transparent = (0, 0, 0, 0)
def select_background(background_dir, time_tag):
    backgrounds = [d for d in os.listdir(background_dir) if time_tag in d]
    background = random.choice(backgrounds)
    return background_dir + background

def select_music(string_of_music_dir):
    music_list = []
    for path in Path(string_of_music_dir).rglob('*.ogg'):
        path = str(path).replace("\\", "/")
        music_list.append(str(path))
    music = random.choice(music_list)
    return music

# Does the status screen for the beginning
def status_screen_state(player, opponent, screen, background):
    player_icon1 = pygame.image.load(player.pokemon1.icon).convert_alpha()
    player_icon2 = pygame.image.load(player.pokemon2.icon).convert_alpha()
    player_icon3 = pygame.image.load(player.pokemon3.icon).convert_alpha()
    player_icon4 = pygame.image.load(player.pokemon4.icon).convert_alpha()
    player_icon5 = pygame.image.load(player.pokemon5.icon).convert_alpha()
    player_icon6 = pygame.image.load(player.pokemon6.icon).convert_alpha()

    # Get from the server
    # enemy_icon1 = pygame.image.load(opponent.pokemon1.icon).convert_alpha()
    # enemy_icon2 = pygame.image.load(opponent.pokemon2.icon).convert_alpha()
    # enemy_icon3 = pygame.image.load(opponent.pokemon3.icon).convert_alpha()
    # enemy_icon4 = pygame.image.load(opponent.pokemon4.icon).convert_alpha()
    # enemy_icon5 = pygame.image.load(opponent.pokemon5.icon).convert_alpha()
    # enemy_icon6 = pygame.image.load(opponent.pokemon6.icon).convert_alpha()

    screen.blit(background, (250,0))
    screen.blit(enemy_icon1, (255,0))
    screen.blit(enemy_icon2, (343,0))
    screen.blit(enemy_icon3, (430,0))
    screen.blit(enemy_icon4, (255,80))
    screen.blit(enemy_icon5, (343,80))
    screen.blit(enemy_icon6, (430,80))
    
    # Get back from the server
    # enemy_icon1_rect = Rect(255,0, 50, 50)
    # enemy_icon2_rect = Rect(94,0, 50, 50)
    # enemy_icon3_rect = Rect(180,0, 50, 50)
    # enemy_icon4_rect = Rect(5,80, 50, 50)
    # enemy_icon5_rect = Rect(94,80, 50, 50)
    # enemy_icon6_rect = Rect(180,80, 50, 50)

    screen.blit(background, (0,0))
    screen.blit(player_icon1, (5,0))
    screen.blit(player_icon2, (94,0))
    screen.blit(player_icon3, (180,0))
    screen.blit(player_icon4, (5,80))
    screen.blit(player_icon5, (94,80))
    screen.blit(player_icon6, (180,80))

    font = pygame.font.SysFont('arial', 15)
    start_option = font.render("START", True, BLACK)

    player_icon1_rect = Rect(5,0, 50, 50)
    player_icon2_rect = Rect(94,0, 50, 50)
    player_icon3_rect = Rect(180,0, 50, 50)
    player_icon4_rect = Rect(5,80, 50, 50)
    player_icon5_rect = Rect(94,80, 50, 50)
    player_icon6_rect = Rect(180,80, 50, 50)
    start_rec = Rect(220, 150, 50, 50)
    carryOn = True
    clock = pygame.time.Clock()
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            
        # --- Game logic should go here
        # Will be rewritten
            mouse_pos = pygame.mouse.get_pos()
            opponent_pos = pygame.mouse.get_pos()
            if pygame.key.get_pressed()[pygame.K_q]:
                print("The quit key has been used!")
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                Checks to see if we have no fainted pokemon, if we don't, add the pokemon to the list of current pokemon
                """
                if(len(player.pokemon_fainted) <= 0 and len(opponent.pokemon_fainted) <= 0):
                    """
                    Check if the mouse has clicked, and if we have any pokemons in our load out, if not, add pokemons. Only proceed if both players have pokemon
                    """
                    if(len(player.pokemon_in_use) <= 0):
                        if player_icon1_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon1)
                            print(player.pokemon1.name + " has joined the party!\nNow waiting for second player!\n")
                            
                        elif player_icon2_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon2)
                            print(player.pokemon2.name + " has joined the party!\nNow waiting for second player!\n")

                        elif player_icon3_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon3)
                            print(player.pokemon3.name + " has joined the party!\nNow waiting for second player!\n")

                    # Do network stuff here
                    # else:
                    #     print("\nBoth players have confirmed their choices!")
                    #     print("Pokemon sent out are: " + str(player.pokemon_in_use[0].name) + " vs " + str(opponent.pokemon_in_use[0].name))
                    #     screen.blit(start_option, (220,150))
                    #     if start_rec.collidepoint(mouse_pos):
                    #         carryOn = False
                    #         pokemon_player_battle_state(player.pokemon_in_use[0], opponent.pokemon_in_use[0], screen)
                
                
                
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

# Loads in our basic assets that will be loaded each fight
def start_game(player, opponent):
    pygame.init()
    with open("assets/config/game_config.json", "r") as loop:
                gameconfig = json.load(loop)
    
    width = gameconfig["Resolution"]["Width"]
    height = gameconfig["Resolution"]["Height"]
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pokemon Battle Sim")

    music_string = select_music('assets/resources/music/')
    pygame.mixer.music.load(music_string)
    pygame.mixer.music.play(-1)
    status_screen = pygame.image.load("assets/resources/graphics/battle_ui/status_screen.png").convert_alpha()
    status_screen_state(player, opponent, screen, status_screen)