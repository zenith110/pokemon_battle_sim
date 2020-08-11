import pygame
from pygame.locals import *
BLACK = (0, 0, 0)
class icon_button(object):
    def __init__(self, text, graphic, rect_x, rect_y, screen):
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.text = text
        self.graphic = graphic
        self.icon = pygame.image.load(graphic).convert_alpha()
        self.rect = Rect(self.rect_x, self.rect_y, 50, 50)
        self.screen = screen
        self.screen.blit(self.icon, (self.rect_x, self.rect_y))
class start_button(object):
    def __init__(self, font, text, image, rect_x, rect_y, screen):
        self.font = font
        self.text = text
        self.image = image
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect = Rect(self.rect_x, self.rect_y, 50, 50)
        self.screen = screen
        self.button_graphic_render = pygame.image.load(image).convert_alpha()
        self.screen.blit(self.button_graphic_render, (self.rect_x - 30, self.rect_y - 10))
        self.button_text_render = self.font.render(self.text,True, BLACK)
        self.screen.blit(self.button_text_render, (self.rect_x,self.rect_y))
class battle_button(object):
    def __init__(self, font, text, image, rect_x, rect_y, screen):
        self.font = font
        self.text = text
        self.image = image
        self.rect_x = rect_x
        self.rect_y = rect_y
        self.rect = Rect(self.rect_x, self.rect_y, 50, 50)
        self.screen = screen
        self.button_text_render = self.font.render(self.text,True, BLACK)
        self.screen.blit(self.button_text_render, (self.rect_x,self.rect_y))

def make_battle_button(font, text, image, rect_x, rect_y, screen):
    new_button = battle_button(font, text, image, rect_x, rect_y, screen)
    return new_button

def make_icon_button(text, graphic, rect_x, rect_y, screen):
    new_button = icon_button(text, graphic, rect_x, rect_y, screen)
    return new_button
def make_start_button(font, text, graphic, rect_x, rect_y, screen):
    new_button = start_button(font, text, graphic, rect_x, rect_y, screen)
    return new_button
