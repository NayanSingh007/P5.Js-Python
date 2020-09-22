import sys
from star import Star
import pygame
from pygame.sprite import Group

class Settings():
	
	def __init__(self):
		
		self.width = 600
		self.height = 600
		self.bg_color = (0, 0, 0)

def run():
	pygame.init()
	ai_setting = Settings()
	screen = pygame.display.set_mode((ai_setting.width, ai_setting.height))
	pygame.display.set_caption("StarField")
	
	#star1 = Star(ai_setting, screen)
	
	stars = Group()
	
	num_of_stars = 150
	
	for i in range(num_of_stars):
		stari = Star(ai_setting, screen)
		stars.add(stari)
	
	
	while True:
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					sys.exit()
		
		screen.fill(ai_setting.bg_color)
		x, y = pygame.mouse.get_pos()
		
		speed = (x/ai_setting.width) * 10
		
		for star in stars:
			star.show()
			star.update(speed)
				
		pygame.display.flip()
		
run()
