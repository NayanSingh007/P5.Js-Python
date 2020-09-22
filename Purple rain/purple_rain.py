import sys
from settings import Settings
from drop import Drop
import pygame
from pygame.sprite import Group

def run():
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.width, ai_settings.height))
	pygame.display.set_caption("Purple Rain")
	
	drops = Group()
	
	for i in range(501):
		new_drop = Drop(screen,ai_settings)
		drops.add(new_drop)
	
	while True:
		for event in pygame.event.get():
			ai_settings.check_events(event)
			
		screen.fill(ai_settings.bg_color)
		
		for d in drops:
			d.show()
			d.update()
		
		pygame.display.flip()
		
run()
