import pygame
import random
import math

class Cell():
	
	def __init__(self,sett,scr,x='',y='',r='',c=''):
		
		if x:
			self.x = x
		else:
			self.x = random.randint(25,600)
		if y:
			self.y = y
		else:
			self.y = random.randint(25,600)
		if c:
			self.c = c
		else:
			self.c = ((random.uniform(0,255),0,random.uniform(0,255),122.5))
		if r:
			self.r = int(r)
		else:
			self.r = 80
			
		self.set = sett
		self.scr = scr
		self.rect = 0
		
	def show(self):
		self.rect = (self.x,self.y,self.r,self.r)
		pygame.draw.ellipse(self.scr,self.c,self.rect)
		
		
	def move(self):
		x,y =  random.uniform(-1,1), random.uniform(-1,1)
		self.x = self.x + x/2
		self.y = self.y + y/2
		
	def d(self,x1,y1,x2,y2):
		dis = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)
		return math.sqrt(dis)
		
	def collision(self,x,y):
		dis = self.d(self.x,self.y,x,y)
		if dis <= self.r :
			return True
