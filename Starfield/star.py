import random
import pygame
from pygame.sprite import Sprite

class Star(Sprite):
	
	def __init__(self,ai_setting, screen):
		
		super().__init__()
		
		self.width = ai_setting.width
		self.height = ai_setting.height
		self.x = random.uniform(-1*self.width/2, self.width/2) 
		self.y = random.uniform(-1*self.height/2, self.height/2)
		self.z = random.uniform(0,self.height)
		self.rect = 0
		self.screen = screen
		self.pz = self.z
		
	def translator(self,x,y):
		px = x + self.width/2
		py = y + self.height/2
		return px, py 
	
	def z_update(self):
		self.z = self.width
		self.x = random.uniform(-1*self.width/2, self.width/2) 
		self.y = random.uniform(-1*self.height/2, self.height/2)
		
	def r_update(self):
		r = 16 * (1 - self.z/self.height)
		return r	
		
	def show(self):	
		sx = (self.x/self.z) * self.width
		sy = (self.y/self.z) * self.height
		sxx, syy = self.translator(sx,sy)
		r = self.r_update()
		self.rect = (sxx , syy, r, r)
		pygame.draw.ellipse(self.screen, (255, 255, 255), self.rect)
		
		#print("its drawing")
	
	def update(self, speed=15):
		self.z = self.z - speed
		if self.z < 1:
			self.z_update()
		#print("its updating")

