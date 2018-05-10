with open('def.py') as f:
    for line in f:
        for part in line.split():
            if 'color=' in part:
                print part

'''import fileinput
import sys

for line in fileinput.input("def.py", inplace=True):
    line = line.replace("SCREEN_WIDTH = 1080", "SCREEN_WIDTH = 1024")
	line = line.replace("SCREEN_HEIGHT = 764", "SCREEN_HEIGHT = 720")
    # sys.stdout is redirected to the file
    sys.stdout.write(line)

for line in fileinput.input("def.py", inplace=True):
	line = line.replace("SCREEN_HEIGHT = 764", "SCREEN_HEIGHT = 720")
    # sys.stdout is redirected to the file
	sys.stdout.write(line)'''

'''import pygame
from pygame.locals import *

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = [1024, 960]
screen = pygame.display.set_mode(size, HWSURFACE | DOUBLEBUF | RESIZABLE)
map_render = pygame.image.load('./gfx/board/board_border.png').convert()

x = int()
for i in range(100):
	x += 14
	screen.blit(map_render, (x, 0))

pygame.draw.rect(screen, BLACK, [150, 100, 250, 200], 2)	
pygame.display.flip()

done = False
clock = pygame.time.Clock()

def zoom():
	screen.blit(pygame.transform.scale2x(map_render), (0, 0))
	pygame.display.flip()

def dezoom():
	screen.blit(pygame.transform.scale(map_render, (map_render.get_width(), map_render.get_height())), (0, 0))
	pygame.display.flip()


while not done:

	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_PLUS:
			zoom()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_MINUS:
			dezoom()
		if event.type == pygame.QUIT:
			done = True

pygame.quit()'''
