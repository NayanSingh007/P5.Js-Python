import sys
import pygame

class Settings():
	
	def __init__(self):
		self.width = 640
		self.height = 360
		self.bg_color = (230, 230, 250)
		
	def check_events(self, event):
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
