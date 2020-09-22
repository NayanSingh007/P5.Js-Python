import pygame

class Draw():
	
	def __init__(self,screen):
		self.c = (251,251,251)
		self.r = 30
		self.scr = screen
		
	def draw(self,x,y):
		pygame.draw.ellipse(self.scr,self.c,(x-self.r/2,y-self.r/2,self.r,self.r))
		#print("Draw Hua")
