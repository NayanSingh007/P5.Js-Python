import pygame
from settings import Settings
from fire import Vector, Fireworks
import random as r
#from math import *

def run():
	pygame.init()
	ai = Settings()
	screen = pygame.display.set_mode((ai.width,ai.height))
	pygame.display.set_caption("Fireworks")
	
	gravity = Vector(0,1/10000)
	fireworks = []
	
	
	
	while True:
		for event in pygame.event.get():
			ai.check_events(event)
			
		screen.fill(ai.bg_color)
		
		if r.uniform(0,1) < 0.001:
			firework = Fireworks(screen,ai,gravity)
			fireworks.append(firework)
		
		for firework in fireworks:
			firework.update()
			firework.show()
			for particle in firework.particles:
				if particle.pos.y > ai.height:
					firework.particles.remove(particle)
		
		pygame.display.flip()
		
run()
