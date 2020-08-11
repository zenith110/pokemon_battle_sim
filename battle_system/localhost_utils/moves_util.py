import pygame
from pypresence import Presence
import json
from pygame.locals import *
from require import require
import sys
screen1_render = require("screen1_render_utils.py")
button = require("button.py")
BLACK = (0, 0, 0)
# Does all of our move logic
def local_host_move_logic(move_name, player_pokemon, opponent_pokemon, screen, background,  move_attack_bar, hp_bar, enemy_bar,  level_text, enemy_Level, screenB, backgroundB,  move_attack_barB, hp_barB, enemy_barB, what_will_you_do_textB, level_textB, enemy_levelB, carryOn, clock, font, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y):
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
            # Checks if opponent have any health
            if(enemy_current_health > 0):
                if(opponent_pokemon.has_selected and player_pokemon.has_selected ):
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
                else:
                    print("We need to wait for the opponent to select a move first before we execute!")
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
            screen1_render.render1_screen(screen, background, pygame.image.load(player_pokemon.back), pygame.image.load(opponent_pokemon.front), system_bar, hp_bar, enemy_bar, what_will_you_do_text, level_text, enemy_Level, font.render(opponent_pokemon.name, True, BLACK), font.render(player_pokemon.name, True, BLACK), pokemon_max_hp, pokemon_current_hp, font, carryOn, clock, player_pokemon, opponent_pokemon, opponent_backgound_front_x, opponent_background_front_y, player_background_back_x, player_background_back_y, screenB)
            #render2_screen_after_hit(screenB, background, opponent_pokemon.back, player_pokemon.front, system_bar, hp_bar, enemy_bar, what_will_you_do_textB, level_text, fightB_option, pokemonB_option, bagB_option, quitB_option, enemy_level, enemy_name, player_pokemon_name, enemy_max_hp, enemy_current_hp)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)

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