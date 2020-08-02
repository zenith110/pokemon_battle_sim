from pygame.locals import *
import pygame
from require import require
battle_render = require("battle_render.py")
BLACK = (0, 0, 0)
transparent = (0, 0, 0, 0)
class button(object):
    def __init__(self, x, y, text, graphic):
        self.text = text
        print("hi")
    def get_text(self):
        return self.text

"""
Used for the beginning, and whenever a pokemon is defeated and updates accordingly
"""
def status_screen_state(player, opponent, screen, background, RPC, screenB):
    player_icon1 = pygame.image.load(player.pokemon1.icon).convert_alpha()
    player_icon2 = pygame.image.load(player.pokemon2.icon).convert_alpha()
    player_icon3 = pygame.image.load(player.pokemon3.icon).convert_alpha()
    player_icon4 = pygame.image.load(player.pokemon4.icon).convert_alpha()
    player_icon5 = pygame.image.load(player.pokemon5.icon).convert_alpha()
    player_icon6 = pygame.image.load(player.pokemon6.icon).convert_alpha()

    enemy_icon1 = pygame.image.load(opponent.pokemon1.icon).convert_alpha()
    enemy_icon2 = pygame.image.load(opponent.pokemon2.icon).convert_alpha()
    enemy_icon3 = pygame.image.load(opponent.pokemon3.icon).convert_alpha()
    enemy_icon4 = pygame.image.load(opponent.pokemon4.icon).convert_alpha()
    enemy_icon5 = pygame.image.load(opponent.pokemon5.icon).convert_alpha()
    enemy_icon6 = pygame.image.load(opponent.pokemon6.icon).convert_alpha()

    screen.blit(background, (250,0))
    screen.blit(enemy_icon1, (255,0))
    screen.blit(enemy_icon2, (343,0))
    screen.blit(enemy_icon3, (430,0))
    screen.blit(enemy_icon4, (255,80))
    screen.blit(enemy_icon5, (343,80))
    screen.blit(enemy_icon6, (430,80))

    enemy_icon1_rect = Rect(255,0, 50, 50)
    enemy_icon2_rect = Rect(343,0, 50, 50)
    enemy_icon3_rect = Rect(430,0, 50, 50)
    enemy_icon4_rect = Rect(255,80, 50, 50)
    enemy_icon5_rect = Rect(343,80, 50, 50)
    enemy_icon6_rect = Rect(430,80, 50, 50)

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
                            RPC.update(state="In battle screen", details= player.name + " has selected " + player.pokemon1.name) # Set the presence
                            print(player.pokemon1.name + " has joined the party!\nNow waiting for second player!\n")
                            
                        elif player_icon2_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon2)
                            RPC.update(state="In battle screen", details= player.name + " has selected " + player.pokemon2.name)  # Set the presence
                            print(player.pokemon2.name + " has joined the party!\nNow waiting for second player!\n")

                        elif player_icon3_rect.collidepoint(mouse_pos):
                            player.pokemon_in_use.append(player.pokemon3)
                            RPC.update(state="In battle screen", details= player.name + " has selected " + player.pokemon3.name)  # Set the presence
                            print(player.pokemon3.name + " has joined the party!\nNow waiting for second player!\n")

                    # Logic check for the opponent pokemon 
                    elif(len(opponent.pokemon_in_use) <= 0):
                        if(enemy_icon1_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon1)
                            print(opponent.pokemon1.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon2_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon2)
                            print(opponent.pokemon2.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon3_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon3)
                            print(opponent.pokemon3.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon4_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon4)
                            print(opponent.pokemon4.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon5_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon5)
                            print(opponent.pokemon5.name + " has joined the party!\nNow waiting for first player!\n")
                        elif(enemy_icon6_rect.collidepoint(mouse_pos)):
                            opponent.pokemon_in_use.append(opponent.pokemon6)
                            print(opponent.pokemon6.name + " has joined the party!\nNow waiting for first player!\n")
                    else:
                        print("\nBoth players have confirmed their choices!")
                        print("Pokemon sent out are: " + str(player.pokemon_in_use[0].name) + " vs " + str(opponent.pokemon_in_use[0].name))
                        RPC.update(state=player.name + "'s " + str(player.pokemon_in_use[0].name) + " vs " + opponent.name + "'s " + str(opponent.pokemon_in_use[0].name), details="🎵 " + player.music + " is currently being played")  # Set the presence
                        screen.blit(start_option, (220,150))
                        start_rec = Rect(220, 150, 50, 50)
                        if start_rec.collidepoint(mouse_pos):
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