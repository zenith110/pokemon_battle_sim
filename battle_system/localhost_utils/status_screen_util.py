from pygame.locals import *
import pygame
import os
import sys
from battle_system.localhost_utils import battle_render
from battle_system.localhost_utils import button
BLACK = (0, 0, 0)

"""
Used for the beginning, and whenever a pokemon is defeated and updates accordingly
"""
def status_screen_state(player, opponent, screen, background, RPC, screenB):
    

    screen.blit(background, (250,0))
    screen.blit(background, (0,0))
    player_icon1 = button.make_icon_button("", player.pokemon1.icon, 5, 0, screen)
    player_icon2 = button.make_icon_button("", player.pokemon2.icon, 94, 0, screen)
    player_icon3 = button.make_icon_button("", player.pokemon3.icon, 180, 0, screen)
    player_icon4 = button.make_icon_button("", player.pokemon4.icon, 5, 80, screen)
    player_icon5 = button.make_icon_button("", player.pokemon5.icon, 94, 80, screen)
    player_icon6 = button.make_icon_button("", player.pokemon6.icon, 180, 80, screen)

    enemy_icon1 = button.make_icon_button("", opponent.pokemon1.icon, 255, 0, screen)
    enemy_icon2 = button.make_icon_button("", opponent.pokemon2.icon, 343, 0, screen)
    enemy_icon3 = button.make_icon_button("", opponent.pokemon3.icon, 430, 0, screen)
    enemy_icon4 = button.make_icon_button("", opponent.pokemon4.icon, 255, 80, screen)
    enemy_icon5 = button.make_icon_button("", opponent.pokemon5.icon, 343, 80, screen)
    enemy_icon6 = button.make_icon_button("", opponent.pokemon6.icon, 430, 80, screen)
    font = pygame.font.SysFont('arial', 15)
    start_option = font.render("START", True, BLACK)
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
                        if player_icon1.rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon1)
                            RPC.update(state="In battle screen", details= player.name + " has selected " + player.pokemon1.name) # Set the presence
                            print(player.pokemon1.name + " has joined the party!\nNow waiting for second player!\n")
                            
                        elif player_icon2.rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon2)
                            RPC.update(state="In battle screen", details= player.name + " has selected " + player.pokemon2.name)  # Set the presence
                            print(player.pokemon2.name + " has joined the party!\nNow waiting for second player!\n")

                        elif player_icon3.rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon3)
                            RPC.update(state="In battle screen", details= player.name + " has selected " + player.pokemon3.name)  # Set the presence
                            print(player.pokemon3.name + " has joined the party!\nNow waiting for second player!\n")
                            selected_pokemon = button.make_icon_button("", "assets/resources/graphics/battle_ui/selected_pokemon.png", 5, 0, screen)

                    # Logic check for the opponent pokemon 
                    elif(len(opponent.pokemon_in_use) <= 0):
                        if(enemy_icon1.rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon1)
                            print(opponent.pokemon1.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon2.rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon2)
                            print(opponent.pokemon2.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon3.rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon3)
                            print(opponent.pokemon3.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon4.rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon4)
                            print(opponent.pokemon4.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon5.rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon5)
                            print(opponent.pokemon5.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon6.rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon6)
                            print(opponent.pokemon6.name + " has joined the party!\nNow waiting for first player!\n")
                    else:
                        print("\nBoth players have confirmed their choices!")
                        print("Pokemon sent out are: " + str(player.pokemon_in_use[0].name) + " vs " + str(opponent.pokemon_in_use[0].name))
                        RPC.update(state=player.name + "'s " + str(player.pokemon_in_use[0].name) + " vs " + opponent.name + "'s " + str(opponent.pokemon_in_use[0].name), details="🎵 " + player.music + " is currently being played")
                        start_option = button.make_start_button(font, "START", "assets/resources/graphics/battle_ui/generic_ui_box.png", 220, 150, screen)
                        if start_option.rect.collidepoint(mouse_pos):
                            carryOn = False
                            battle_render.pokemon_player_battle_state(player.pokemon_in_use[0], opponent.pokemon_in_use[0], screen, screenB)
                
            else:
                for i in player.pokemon_defeated:
                    if(i == "Pokemon1"):
                        print("Pokemon1 is fainted, removing the option")
                    elif(i == "Pokemon2"):
                        print("hi")
                    elif(i == "Pokemon3"):
                        print("hi")
                    elif(i == "Pokemon4"):
                        print("hi")
                    elif(i == "Pokemon5"):
                        print("hi")
                    elif(i == "Pokemon6"):
                        print("hi")
                for i in opponent.pokemon_defeated:
                    if(i == "Pokemon1"):
                        print("Pokemon1 is fainted, removing the option")
                    elif(i == "Pokemon2"):
                        print("hi")
                    elif(i == "Pokemon3"):
                        print("hi")
                    elif(i == "Pokemon4"):
                        print("hi")
                    elif(i == "Pokemon5"):
                        print("hi")
                    elif(i == "Pokemon6"):
                        print("hi")
                
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)