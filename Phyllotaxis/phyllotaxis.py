import pygame
from settings import Settings
from point import Point

def run():
	pygame.init()
	ai = Settings()
	screen = pygame.display.set_mode((ai.width,ai.height))
	pygame.display.set_caption("Phyllotaxis")
	
	point1 = Point(screen,ai,4)
	
	while True:
		for event in pygame.event.get():
			ai.check_events(event)
			
		screen.fill(ai.bg_color)
		
		point1.dataStore()
		for data in point1.data:
			point1.show(data[0],data[1],data[2])
			
		pygame.display.flip()
		
run()
