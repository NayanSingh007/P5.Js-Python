import pygame
import math as m

#this function is taken from net
def hsv2rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    h60 = h / 60.0
    h60f = m.floor(h60)
    hi = int(h60f) % 6
    f = h60 - h60f
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    r, g, b = 0, 0, 0
    if hi == 0: r, g, b = v, t, p
    elif hi == 1: r, g, b = q, v, p
    elif hi == 2: r, g, b = p, v, t
    elif hi == 3: r, g, b = p, q, v
    elif hi == 4: r, g, b = t, p, v
    elif hi == 5: r, g, b = v, p, q
    r, g, b = int(r * 255), int(g * 255), int(b * 255)
    return (r, g, b)

class Point():
	
	def __init__(self,screen,settings,c):
		self.c = c
		self.n = 0
		self.scr = screen
		self.set = settings
		self.data = []
		
	def dataStore(self):
		a = self.n * 137.5
		r = self.c * m.sqrt(self.n)
		x = r * m.cos(a*m.pi/180) + self.set.width / 2
		y = r * m.sin(a*m.pi/180) + self.set.height / 2
		self.data.append([x,y,self.n])
		self.n = self.n + 1
		
	def show(self,x,y,n):
		color = hsv2rgb(n%255,1,1)
		#print(color)
		pygame.draw.ellipse(self.scr,color,(x,y,4,4))
	
	
