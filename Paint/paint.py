import pygame
from settings import Settings
from draw import Draw
import sys

def run():
	pygame.init()
	ai = Settings()
	screen = pygame.display.set_mode((ai.width,ai.height))
	pygame.display.set_caption("Paint")
	
	paint = False
	space = False
	data = []
	brush = Draw(screen)
	
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				paint = True
			if event.type == pygame.MOUSEBUTTONUP:
				paint = False
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
				if event.key == pygame.K_SPACE:
					space = True
					#print("space True")
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_SPACE:
					space = False
			
		screen.fill(ai.bg_color)
		if paint:
			x,y = pygame.mouse.get_pos()
			data.append([x,y])
			
		for i in data:
			brush.draw(i[0],i[1])
		 
		if space:
			 data = []
			 screen.fill(ai.bg_color)
		pygame.display.flip()
			 
run()
