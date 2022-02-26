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

#adding the words and other items
game_name = test_font.render('MathGame', False, (111,196,169))
game_name_rect = game_name.get_rect(center = (400,80))


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	if game_active:
		screen.fill('black')
		level.run()
	
	if game_active == False:
		screen.fill((68,29,183))
		screen.blit(game_name, game_name_rect)

	
	pygame.display.update()
	clock.tick(60)