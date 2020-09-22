import sys
import pygame

class Settings():
	
	def __init__(self):
		self.width = 600
		self.height = 400
		self.bg_color = (51,51,51)
		
	def check_events(self,event):
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
