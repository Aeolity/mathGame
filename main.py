from cgitb import grey
import pygame
import sys
from player import Player
from settings import *
from level import Level

# Pygame setup
pygame.init()
global game_active
game_active = True
global fight_scene
fight_scene = False
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map, screen)
test_font = pygame.font.Font('font/Pixeltype.ttf', 80)
LvL1background = pygame.image.load(
    'graphics/backgrounds/darkbrick.png').convert()
LvL1foreground = pygame.image.load(
    'graphics/foregrounds/untitled.png').convert_alpha()
#Lvl1Background_scaled = pygame.transform.scale(LvL1background, (1725, 1024))

# intro screen
game_name = test_font.render('Mathgame', False, (111, 196, 169))
game_name_rect = game_name.get_rect(center=(400, 80))

intro_directions = test_font.render(
    'press space to begin', False, (111, 196, 169))
intro_directions_rect = intro_directions.get_rect(center=(600, 400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if game_active == False:
        screen.fill((54, 38, 148))
        screen.blit(game_name, game_name_rect)
        screen.blit(intro_directions, intro_directions_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game_active = True

    if game_active:
        screen.blit(LvL1background, (0, 0))
        level.run()
        screen.blit(level.snail, level.snail_rect)
        if level.game_active == False:
            game_active = False
        screen.blit(LvL1foreground, (0, 4))

        pygame.display.update()
        clock.tick(60)