from cgitb import grey
import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
game_active = False
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
LvL1background = pygame.image.load('graphics/backgrounds/2638149.jpg').convert()
#Lvl1Background_scaled = pygame.transform.scale(LvL1background, (1725, 1024))

#intro screen
game_name = test_font.render('Mathgame', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	if game_active == False:
		screen.fill((54,38,148))
		screen.blit(game_name, game_name_rect)

	if game_active:
		screen.blit(LvL1background,(0,0))
		level.run()
	
	pygame.display.update()
	clock.tick(60)