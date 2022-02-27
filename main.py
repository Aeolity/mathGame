import pygame, sys
from settings import * 
from level import Level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
#DISPLAYSURF = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
LvL1background = pygame.image.load('graphics/backgrounds/2638149.jpg').convert()
#Lvl1Background_scaled = pygame.transform.scale(LvL1background, (1725, 1024))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	screen.blit(LvL1background,(0,0))
	#screen.fill('black')
	level.run()

	pygame.display.update()
	clock.tick(60)