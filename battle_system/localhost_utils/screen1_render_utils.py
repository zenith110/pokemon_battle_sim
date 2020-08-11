from pygame.locals import *
from pypresence import Presence
import pygame
import json
import sys
from require import require
button = require("button.py")
BLACK = (0, 0, 0)
"""
Does the logic checking depending on status
@move_name - string
@player_pokemon - pokemon object
@opponent_pokemon - pokemon object
@screen - pygame surface
@background - pygame image
@move_attack_bar - pygame image
@hp_bar - pygame image
@level_text - font render
@enemy level - font render
"""
def local_host_move_logic(move_name, player_pokemon, opponent_pokemon, screen, background,  move_attack_bar, hp_bar, enemy_bar,  level_text, enemy_level, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB, carryOn, clock, font, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y):
    with open("assets/move_data/" + move_name + ".json", "r") as loop:
                move = json.load(loop)
                        
    damage = move["Data"]["Base_Damage"]
    status = move["Data"]["Status"]
    pokemon_max_hp = font.render(str(player_pokemon.HP), True, BLACK)
    pokemon_current_hp = font.render(str(player_pokemon.HP), True, BLACK)
    enemy_current_health = font.render(str(opponent_pokemon.HP), True, BLACK)
    carryOn = True
    while carryOn:  
        # Checks if we have a damage hitting move
        if(status == "Damage"):
            # Checks if have any health
            if(enemy_current_health > 0):
            # Take away the enemy's health
                enemy_current_health -= damage
                screen.fill(pygame.Color("black")) # erases the entire screen surface
                pokemon_current_hp = font.render(str(current_health), True, BLACK)
                move_text = font.render(player_pokemon + " attacks "+ opponent_pokemon + " with " + move_name + " dealing " + str(damage) + " damage", True, BLACK)
                render1_attack_menu_bar(screen, background, player_sprite, enemy_sprite, move_attack_bar, hp_bar, enemy_bar,  level_text, enemy_Level, enemy_name, player_pokemon_name, pokemon_max_hp, pokemon_current_hp, move_text)
                enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                what_will_you_do_textB = font.render(opponent_pokemon[0] + " was dealt " + str(damage) + " damage from " + player_pokemon[0] + "'s " + move_name, True, BLACK)
                render2_screen_during_hit(screenB, background, playerB_sprite, enemyB_sprite, move_attack_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, Enemy_Level, Enemy_name, Player_pokemon_name, enemy_max_hp, enemy_current_hp)
                                    
                screenB.fill(pygame.Color("black"))
                what_will_you_do_textB = font.render("What will " + opponent.pokemon + " do?", True, BLACK)
                render1_screen(screen, background, pygame.image.load(player_pokemon.back), pygame.image.load(opponent_pokemon.front), system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, enemy_Level, font.render(opponent_pokemon.name, True, BLACK), font.render(player_pokemon.name, True, BLACK), pokemon_max_hp, pokemon_current_hp, font, carryOn, clock, player_pokemon, opponent_pokemon, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB)
                # render2_screen_after_hit(screenB, background, playerB_sprite, enemyB_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)

                if(enemy_current_health <= 0):
                    screenB.fill(pygame.Color("black")) # erases the entire screen surface
                    enemy_current_health = 0
                    enemy_current_hp = font.render(str(enemy_current_health), True, BLACK)
                    move_text = font.render(opponent_pokemon + " has fainted! Now awaiting for next pokemon", True, BLACK)
                    render_pokemon_fainted(screen, background, player_sprite, move_attack_bar, hp_bar, level_text,  player_pokemon_name, pokemon_max_hp, pokemon_current_hp, move_text)
                    # Keeps track of the pokemon who has fainted
                    opponent_pokemon.fainted.append(opponent_pokemon)
                    render2_status_screen(screenB, status_screen, enemy_icon1, enemy_icon2, enemy_icon3, enemy_icon4, enemy_icon5, enemy_icon6)
                    print(opponent_pokemon + " has fainted!")
        if(status == "Status-effect"):
            print(move_name + " causes a status, no damage taken!")
            carryOn = False
            system_bar = pygame.image.load("assets/resources/graphics/battle_ui/system_bar.png").convert_alpha()
            what_will_you_do_text = font.render("What will " + player_pokemon.name + " do?", True, BLACK)
            what_will_you_do_textB = font.render("What will " + opponent_pokemon.name + " do?", True, BLACK)
            carryOn = False
            render1_screen(screen, background, pygame.image.load(player_pokemon.back), pygame.image.load(opponent_pokemon.front), system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, enemy_level, font.render(opponent_pokemon.name, True, BLACK), font.render(player_pokemon.name, True, BLACK), pokemon_max_hp, pokemon_current_hp, font, carryOn, clock, player_pokemon, opponent_pokemon, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB)
            #render2_screen_after_hit(screenB, background, opponent_pokemon.back, player_pokemon.front, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)
"""
Displays the moves of the current pokemon
"""
# Loads our menu whenever we click fight on the player side
def move_selection_option_player(screen, pokemon, opponent, font, mouse_pos, carryOn, clock, move_attack_bar, hp_bar, enemy_bar, player_pokemon_level, enemy_level, enemy_name, player_pokemon_name, player_pokemon_max_hp, background, player_sprite, opponent_sprite, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB, backgroundB, move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB):
    screen.blit(background, (0,0))
    screen.blit(move_attack_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(player_pokemon_level, (205, 124))
    screen.blit(enemy_level, (81, 32))
    screen.blit(enemy_name, (0, 30))
    screen.blit(player_pokemon_name, (150, 125))
    screen.blit(player_pokemon_max_hp, (215, 142))

    
    screen.blit(player_sprite, (player_background_back_x ,player_background_back_y))
    screen.blit(opponent_sprite, ((10 - opponent_backgound_front_x) , (opponent_background_front_y - 20)))
    move_1 = button.make_battle_button(font, pokemon.move_1, "", 4, 165, screen)
    move_2 = button.make_battle_button(font, pokemon.move_2, "", 4, 180, screen)
    move_3 = button.make_battle_button(font, pokemon.move_3, "", 65, 165, screen)
    move_4 = button.make_battle_button(font, pokemon.move_4, "", 65, 180, screen)
    carryOn = True
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
                 if move_1.rect.collidepoint(mouse_pos):
                     print(pokemon.move_1 + " has been selected!")
                     carryOn = False
                     local_host_move_logic(pokemon.move_1, pokemon, opponent, screen, background,  move_attack_bar, hp_bar, enemy_bar,  player_pokemon_level, enemy_level, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB, carryOn, clock, font, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y)
                 elif move_2.rect.collidepoint(mouse_pos):
                     print(pokemon.move_2 + " has been selected!")
                     carryOn = False
                     local_host_move_logic(pokemon.move_2, pokemon, opponent, screen, background,  move_attack_bar, hp_bar, enemy_bar,  player_pokemon_level, enemy_level, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB, carryOn, clock, font, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y)
                 elif move_3.rect.collidepoint(mouse_pos):
                     print(pokemon.move_3 + " has been selected!")
                     carryOn = False
                     local_host_move_logic(pokemon.move_3, pokemon, opponent, screen, background,  move_attack_bar, hp_bar, enemy_bar,  player_pokemon_level, enemy_level, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB, carryOn, clock, font, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y)
                 elif move_4.rect.collidepoint(mouse_pos):
                     print(pokemon.move_4 + " has been selected!")
                     carryOn = False
                     local_host_move_logic(pokemon.move_4, pokemon, opponent, screen, background,  move_attack_bar, hp_bar, enemy_bar,  player_pokemon_level, enemy_level, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB, carryOn, clock, font, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y)


               
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

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
"""
Updates screen one to show that the pokemon has fainted
"""
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
"""
Renders the default player screen
"""
def render1_screen(screen, background, player_sprite, enemy_sprite, system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, enemy_level, Enemy_name, Player_pokemon_name, pokemon_max_hp, pokemon_current_hp, font, carryOn, clock, player_pokemon, opponent_pokemon, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB):
    fight_option = font.render("FIGHT", True, BLACK)
    pokemon_option = font.render("POKEéMON", True, BLACK)
    bag_option = font.render("BAG", True, BLACK)
    quit_option = font.render("QUIT", True, BLACK)
    move_bar = pygame.image.load("assets/resources/graphics/battle_ui/move_bar.png").convert_alpha()
    screen.blit(background, (0,0))
    screen.blit(player_sprite, (5,110))
    screen.blit(enemy_sprite, (150,50))
    screen.blit(system_bar, (0,160))
    screen.blit(hp_bar, (120,113))
    screen.blit(enemy_bar, (0,20))
    screen.blit(what_will_you_do_text, (8, 163))
    screen.blit(level_text, (235, 124))
    screen.blit(fight_option, (130, 165))
    screen.blit(pokemon_option, (130, 180))
    screen.blit(bag_option, (195, 165))
    screen.blit(quit_option, (195, 180))
    screen.blit(enemy_level, (81, 32))
    screen.blit(Enemy_name, (0, 30))
    screen.blit(Player_pokemon_name, (150, 125))
    screen.blit(pokemon_max_hp, (215, 144))
    screen.blit(pokemon_current_hp, (195, 144))

    fight_rec = Rect(130, 165, 20, 10)
    pokemon_rect = Rect(130, 180, 20, 10)
    bag_rect = Rect(195, 165, 20, 10)
    quit_rect = Rect(195, 180, 20, 10)
    
    
    carryOn = True
    # -------- Main Program Loop -----------
    while carryOn:
    # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                carryOn = False # Flag that we are done so we exit this loop
            if pygame.key.get_pressed()[pygame.K_q]:
                print("The quit key has been used!")
                pygame.quit()
                sys.exit() 
        # --- Game logic should go here
        # Will be rewritten
            mouse_pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if fight_rec.collidepoint(mouse_pos):
                    print("Hi, fight been selected!")
                    screen.fill(pygame.Color("black"))
                    carryOn = False
                    what_will_you_do_textB = font.render("What will " + opponent_pokemon.name + " do?", True, BLACK)
                    move_selection_option_player(screen, player_pokemon, opponent_pokemon, font, mouse_pos, carryOn, clock, move_bar, hp_bar, enemy_bar, level_text, enemy_level, font.render(opponent_pokemon.name, True, BLACK), font.render(player_pokemon.name, True, BLACK),font.render(str(player_pokemon.HP), True, BLACK), background, pygame.image.load(player_pokemon.back).convert_alpha(), pygame.image.load(opponent_pokemon.front).convert_alpha(), opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB, background, move_bar, hp_bar, enemy_bar, what_will_you_do_textB, opponent_pokemon.level, player_pokemon.level)
                    
                elif bag_rect.collidepoint(mouse_pos):
                    print("Bag has been selected")

                elif quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()              
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)