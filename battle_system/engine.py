import pygame
import os
import json
import glob
import random
from pathlib import Path
from pypresence import Presence
import time
from datetime import datetime
# Creates our colors
BLACK = (0, 0, 0)
transparent = (0, 0, 0, 0)

# Makes our basic player class
class player_data(object):
    def __init__(self, player_data_file, enemy_sprite):
        with open(player_data_file, "r") as loop:
                player_data = json.load(loop)
        self.name = player_data["Name"]
        self.trainer_image = player_data["Image_url"]
        self.time_spent = player_data["Time_Spent"]
        # Declares our lists that has the pokemon data
        self.pokemon1 = []
        self.pokemon2 = []
        self.pokemon3 = []
        self.pokemon4 = []
        self.pokemon5 = []
        self.pokemon6 = []
        for i in range(0, 11):
            self.pokemon1.append(player_data["Pokemon1"][i])
            self.pokemon2.append(player_data["Pokemon2"][i])
            self.pokemon3.append(player_data["Pokemon3"][i])
            self.pokemon4.append(player_data["Pokemon4"][i])
            self.pokemon5.append(player_data["Pokemon5"][i])
            self.pokemon6.append(player_data["Pokemon6"][i])
        self.enemy_sprite = enemy_sprite
        self.is_defeated = False
        self.has_attacked = False
        self.pokemon1_icon = self.pokemon1[10]
        self.pokemon2_icon = self.pokemon2[10]
        self.pokemon3_icon = self.pokemon3[10]
        self.pokemon4_icon = self.pokemon4[10]
        self.pokemon5_icon = self.pokemon5[10]
        self.pokemon6_icon = self.pokemon6[10]

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

def render_pokemon_fainted(screen, background, player_sprite, move_bar, hp_bar, level_text,  Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp, move_text):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(level_text, (235, 124))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
    screen.blit(move_text,(8, 163))

def render2_status_screen(screen, background, icon1, icon2, icon3, icon4, icon5, icon6):
    screen.blit(background, (250,0))
    screen.blit(icon1, (255,0))
    screen.blit(icon2, (343,0))
    screen.blit(icon3, (430,0))
    screen.blit(icon4, (255,80))
    screen.blit(icon5, (343,80))
    screen.blit(icon6, (430,80))

def render1_attack_menu_bar(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp, move_text):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(level_text, (235, 124))
    screen.blit(enemy_level, (81, 32))
    screen.blit(enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))
    screen.blit(move_text,(8, 163))

def render1_after_attack_physical(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(system_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do_text, (8, 163))
    screen.blit(level_text, (235, 124))
    screen.blit(Fight_option, (130, 165))
    screen.blit(Pokemon_option, (130, 180))
    screen.blit(Bag_option, (195, 165))
    screen.blit(Quit_option, (195, 180))
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))

def render_moves(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(move_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(level_text, (235, 124))
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))

def render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(enemy_level, (478, 124))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))

def render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(enemy_level, (478, 124))
    screenB.blit(FightB_option, (380, 165))
    screenB.blit(PokemonB_option, (380, 180))
    screenB.blit(BagB_option, (450, 165))
    screenB.blit(QuitB_option, (450, 180))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))
    
def render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp):
    screenB.blit(background, (250,0))
    screenB.blit(playerB_sprite, (415,40))
    screenB.blit(enemyB_sprite, (260,110))
    screenB.blit(system_bar, (250,160))
    screenB.blit(hp_bar, (375,113))
    screenB.blit(enemy_bar, (250,20))
    screenB.blit(what_will_you_do_textB, (260, 163))
    screenB.blit(enemy_level, (478, 124))
    screenB.blit(FightB_option, (380, 165))
    screenB.blit(PokemonB_option, (380, 180))
    screenB.blit(BagB_option, (450, 165))
    screenB.blit(QuitB_option, (450, 180))
    screenB.blit(level_text, (333, 32))
    screenB.blit(Player_pokemon_name, (250, 30))
    screenB.blit(Enemy_name, (390, 125))
    screenB.blit(enemy_max_hp, (472, 143))
    screenB.blit(enemy_current_hp, (452, 143))

def render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp):
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(system_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do_text, (8, 163))
    screen.blit(level_text, (235, 124))
    screen.blit(Fight_option, (130, 165))
    #screen.blit(arrow, (175, 160))
    screen.blit(Pokemon_option, (130, 180))
    screen.blit(Bag_option, (195, 165))
    screen.blit(Quit_option, (195, 180))
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon1_max_hp, (215, 144))
    screen.blit(pokemon1_current_hp, (195, 144))


# Loads our menu whenever we click fight on the player side
def move_selection_option_player(screen, num_of_pokemon, font):
    move_1 = font.render(num_of_pokemon[1],True, BLACK)
    screen.blit(move_1, (4,165))
    move_2 = font.render(num_of_pokemon[2],True, BLACK)
    screen.blit(move_2, (4,180))
    move_3 = font.render(num_of_pokemon[3],True, BLACK)
    screen.blit(move_3, (65,165))
    move_4 = font.render(num_of_pokemon[4],True, BLACK)
    screen.blit(move_4, (65,180))

def server_host_play(player1):
    print("Game is loading up")

def local_host_play(player1, player2):
    # Checks to see that the pokemons have attacked yet
    pygame.init()
    with open("battle_system/battle_code/config/game_config.json", "r") as loop:
                gameconfig = json.load(loop)
    
    width = gameconfig["Resolution"]["Width"]
    height = gameconfig["Resolution"]["Height"]
    size = (width, height)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pokemon Battle Sim")
    screenB = pygame.display.set_mode((500,195), 0, 32)

    # Loads for the first pokemon sprite
    with open(player1, "r") as loop:
                player1_data = json.load(loop)

    # Loads for the first pokemon sprite
    with open(player2, "r") as loop:
                player2_data = json.load(loop)
    player = player_data(player1, player2_data["Pokemon1"][8])
    opponent = player_data(player2, player1_data["Pokemon1"][9])
    

    now = datetime.now()
    current_time = now.strftime("%H")
    print("Current Time =", current_time)

    if int(current_time) >= 18  or int(current_time) >= 1 and int(current_time) < 7:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "night")
    if int(current_time) >= 7 and int(current_time) <= 11:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "morning")
    if int(current_time) >= 12 and int(current_time) <= 17:
        background = select_background("battle_system/battle_code/resources/graphics/battle_backgrounds/", "afternoon")

    player_sprite_string = opponent.enemy_sprite
    player_sprite =  pygame.image.load(player_sprite_string).convert_alpha()  
    enemy_sprite_string = player.enemy_sprite
    enemy_sprite =  pygame.image.load(enemy_sprite_string).convert_alpha()
    background = pygame.image.load(background).convert_alpha()
    system_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/system_bar.png").convert_alpha()
    hp_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/hp_bar.png").convert_alpha()
    enemy_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/enemy_hp_bar.png").convert_alpha()
    arrow = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/arrow.png").convert_alpha()
    move_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/move_bar.png").convert_alpha()
    move_attack_bar = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/attack_bar.png").convert_alpha()
    status_screen = pygame.image.load("battle_system/battle_code/resources/graphics/battle_ui/status_screen.png").convert_alpha()
    font = pygame.font.SysFont(None, 12)
    what_will_you_do_text = font.render("What will " + player.pokemon1[0] + " do?", True, BLACK)
    level_text = font.render(str(player.pokemon1[5]), True, BLACK)
    fight_option = font.render("FIGHT", True, BLACK)
    fight_rec = fight_option.get_rect()
    pokemon_option = font.render("POKEéMON", True, BLACK)
    bag_option = font.render("BAG", True, BLACK)
    quit_option = font.render("QUIT", True, BLACK)
    enemy_level = font.render(str(opponent.pokemon1[5]), True, BLACK)
    enemy_name = font.render(str(opponent.pokemon1[0]), True, BLACK)
    player_pokemon_name = font.render(str(player.pokemon1[0]), True, BLACK)
    pokemon_max_hp = font.render(str(player.pokemon1[7]), True, BLACK)
    pokemon_current_hp = font.render(str(player.pokemon1[7]), True, BLACK)
    player_icon1 = pygame.image.load(player.pokemon1_icon).convert_alpha()
    player_icon2 = pygame.image.load(player.pokemon2_icon).convert_alpha()
    player_icon3 = pygame.image.load(player.pokemon3_icon).convert_alpha()
    player_icon4 = pygame.image.load(player.pokemon4_icon).convert_alpha()
    player_icon5 = pygame.image.load(player.pokemon5_icon).convert_alpha()
    player_icon6 = pygame.image.load(player.pokemon6_icon).convert_alpha()
    render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, fight_option, pokemon_option, bag_option, quit_option, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp)
    
    music_string = select_music('battle_system/battle_code/resources/music/')
    pygame.mixer.music.load(music_string)
    pygame.mixer.music.play(-1)

    # Begins the second window
    playerB_sprite_string = player.pokemon1[8]
    playerB_sprite =  pygame.image.load(playerB_sprite_string).convert_alpha() 
    enemyB_sprite_string = opponent.pokemon1[9]
    enemyB_sprite =  pygame.image.load(enemyB_sprite_string).convert_alpha() 
    what_will_you_do_textB = font.render("What will " + opponent.pokemon1[0] + " do?", True, BLACK)
    fightB_option = font.render("FIGHT", True, BLACK)
    pokemonB_option = font.render("POKEéMON", True, BLACK)
    bagB_option = font.render("BAG", True, BLACK)
    quitB_option = font.render("QUIT", True, BLACK)
    enemy_icon1 = pygame.image.load(opponent.pokemon1_icon).convert_alpha()
    enemy_icon2 = pygame.image.load(opponent.pokemon2_icon).convert_alpha()
    enemy_icon3 = pygame.image.load(opponent.pokemon3_icon).convert_alpha()
    enemy_icon4 = pygame.image.load(opponent.pokemon4_icon).convert_alpha()
    enemy_icon5 = pygame.image.load(opponent.pokemon5_icon).convert_alpha()
    enemy_icon6 = pygame.image.load(opponent.pokemon6_icon).convert_alpha()

    
    enemy_current_hp = font.render(str(opponent.pokemon1[7]), True, BLACK)
    enemy_max_hp = font.render(str(opponent.pokemon1[7]), True, BLACK)
    render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)

    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    carryOn = True
    isPokemon1 = True
    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            
        # --- Game logic should go here
        # Will be rewritten
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                screen.fill(pygame.Color("black")) # erases the entire screen surface
                render_moves(screen, background, player_sprite, enemy_sprite, move_bar, hp_bar, enemy_bar,  level_text, enemy_level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp)
                move_selection_option_player(screen, player.pokemon1, font)
                render2_screen(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)

                #     #print (str(mx) + " is the current x " + str(my) + " is the current y")
                # if mx in range(128, 191) and my in range(164, 175):
                #     print("mouse is over 'fight option'")
                #     # Need to blip away the stuff here
                # # Move1 rec
                # if mx in range(3, 58) and my in range(164, 172):
                #     # Going to make the below rendering into a method to make it a bit tidier
                #         print("")    
                # if mx in range(63, 122) and my in range(162, 173):
                #       print("")  
                # if mx in range(2, 58) and my in range(177, 187):
                #     if(isPokemon1 == True):
                #         Move3 = player.pokemon1[3]
                #         with open("battle_system/move_data/" + Move3 + ".json", "r") as loop:
                #             move3 = json.load(loop)
                        
                #         damage = move3["Data"]["Base_Damage"]
                #         status = move3["Data"]["Status"]
                #         # Checks if we have a damage hitting move
                #         if(status == "Damage"):
                #         # Checks if have any health
                #             if(enemy_current_hp > 0):
                #                 # Take away the enemy's health
                #                 enemy_current_hp -= damage
                #                 screen.fill(pygame.Color("black")) # erases the entire screen surface
                #                 pokemon1_current_hp = font.render(str(current_health), True, BLACK)
                #                 render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                #                 enemy_current_hp = font.render(str(enemy_current_hp), True, BLACK)
                #                 render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                #                 print("Total hp is: " + str(enemy_current_hp))
                #                 print("There's still health to go after!")
                #             if(enemy_current_hp <= 0):
                #                 screen.fill(pygame.Color("black")) # erases the entire screen surface
                #                 enemy_current_hp = 0
                #                 enemy_current_hp = font.render(str(enemy_current_hp), True, BLACK)
                #                 render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                #                 print(enemy_pokemon_data + " has fainted!")
                #         if(status == "Status-effect"):
                #             print(Move1 + " causes a status, no damage taken!")
                #             pokemon1_attack = True
                # if mx in range(65, 121) and my in range(184, 191):
                #     if(isPokemon1 == True):
                #         Move4 = player.pokemon1[4]
                #         with open("battle_system/move_data/" + Move4 + ".json", "r") as loop:
                #             move4 = json.load(loop)
                        
                #         damage = move4["Data"]["Base_Damage"]
                #         status = move4["Data"]["Status"]
                #         # Checks if we have a damage hitting move
                #         if(status == "Damage"):
                #         # Checks if have any health
                #             if(enemy_current_hp > 0):
                #                 # Take away the enemy's health
                #                 enemy_current_hp -= damage
                #                 screen.fill(pygame.Color("black")) # erases the entire screen surface
                #                 pokemon1_current_hp = font.render(str(current_health), True, BLACK)
                #                 render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, Fight_option, Pokemon_option, Bag_option, Quit_option, enemy_level, Enemy_name, Player_pokemon_name, pokemon1_max_hp, pokemon1_current_hp)
                #                 enemy_current_hp = font.render(str(enemy_current_hp), True, BLACK)
                #                 render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                #                 print("Total hp is: " + str(enemy_current_hp))
                #                 print("There's still health to go after!")
                #             if(enemy_current_hp <= 0):
                #                 screen.fill(pygame.Color("black")) # erases the entire screen surface
                #                 enemy_current_hp = 0
                #                 enemy_current_hp = font.render(str(enemy_current_hp), True, BLACK)
                #                 render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, FightB_option, PokemonB_option, BagB_option, QuitB_option, enemy_level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                #                 print(enemy_pokemon_data + " has fainted!")
                #         if(status == "Status-effect"):
                #             print(Move1 + " causes a status, no damage taken!")
                #             pokemon1_attack = True

                if mx in range(195, 250) and my in range(164, 175):
                    print("mouse is over 'bag option'")
                if mx in range(128, 191) and my in range(180, 187):
                    print("mouse is over 'pokemon option'")
                if mx in range(194, 250) and my in range(183, 187):
                    print("mouse is over 'quit option'")
                    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
 
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()
    