import pygame
import random

from pygame.sprite import Sprite

class Drop(Sprite):
	
	def __init__(self,screen,settings):
		super().__init__()
		self.setting = settings
		self.x = random.uniform(0,self.setting.width)
		self.y = random.uniform(-500,-50)
		self.z = random.uniform(0,20)
		self.y_speed = self.z_map(2,8)
		self.screen = screen
		self.len = self.z_map(10,20)
		
	def z_map(self, x, y):
		z = (self.z/20) * (y - x)
		return z	
		
	def update(self):
		self.y = self.y + self.y_speed
		grv = self.z_map(0,0.05)
		self.y_speed = self.y_speed + grv
		if (self.y > self.setting.height):
			self.y = random.uniform(-200, -100)
			self.y_speed = self.z_map(2,8)
			
	def show(self):
		stroke = int(self.z_map(1,3))
		pygame.draw.line(self.screen,(138, 43, 226),(self.x, self.y),
			(self.x, self.y + self.len), stroke)
