import pygame
import random as r
import math as m

colors = [(145,170,255),(255,158,158),(255,128,197),(122,251,255),(138,255,156)]

class Vector():
	
	def __init__(self,x,y):
		self.x = x
		self.y = y
		
	def add(self,vec):
		self.x = self.x + vec.x
		self.y = self.y + vec.y
		
	def mult(self,a):
		self.x = self.x * a
		self.y = self.y * a
	
	def random2d(self):
		self.x = r.uniform(-1,1)
		self.y = m.sqrt(1 - m.pow(self.x,2))*r.choice([1,-1])

class Particle():
	
	def __init__(self,x,y,screen,settings,firework,color=''):
		self.pos = Vector(x,y)
		if firework:
			self.vel = Vector(0,(-1.5)*r.uniform(1/10,1/7))
		else:
			self.vel = Vector(0,0)
			self.vel.random2d()
			self.vel.mult(r.uniform(1/12,1/7))
		self.acc = Vector(0,0)
		self.scr = screen
		self.set = settings
		if color:
			self.col = color
		else:	
			self.col = r.choice(colors)
			
		self.r = 4
		
	def applyForce(self,force):
		self.acc.add(force)
		
	def update(self):
		self.vel.add(self.acc)
		self.pos.add(self.vel)
		self.acc.mult(0)
	
	def show(self):
		#rect = Vector(self.pos.x-self.r/2,self.pos.y-self.r/2)
		pygame.draw.ellipse(self.scr,self.col,(self.pos.x,self.pos.y,self.r,self.r))
		
class Fireworks():
	
	def __init__(self,screen,settings,gravity):
		self.scr = screen
		self.set = settings
		self.g = gravity
		self.firework = Particle(r.uniform(0,self.set.width),self.set.height,self.scr,self.set,True)
		self.explode = False
		self.particles = []
		
	def update(self):
		if not self.explode:
			self.firework.applyForce(self.g)
			self.firework.update()
			if self.firework.vel.y >= 0:
				self.explode = True
				self.explosion()
		for particle in self.particles:
			particle.applyForce(self.g)
			particle.update()
		
	def show(self):
		if not self.explode:
			self.firework.show()
		for particle in self.particles:
			particle.show()
			
	def explosion(self):
		for i in range(20):
			p = Particle(self.firework.pos.x,self.firework.pos.x,self.scr,self.set,False,self.firework.col)
			self.particles.append(p)
		
		
		
