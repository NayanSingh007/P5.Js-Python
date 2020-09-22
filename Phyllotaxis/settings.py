import sys
import pygame

class Settings():
	
	def __init__(self):
		self.width = 400
		self.height = 400
		self.bg_color = (0,0,0)
		
	def check_events(self,event):
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
