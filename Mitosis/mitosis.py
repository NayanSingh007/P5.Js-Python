import pygame
from settings import Settings
from cell import Cell


def run():
	pygame.init()
	ai = Settings()
	screen = pygame.display.set_mode((ai.width,ai.height))
	pygame.display.set_caption("Mitosis")
	
	cells = []
	for i in range(10):
		cells.append(Cell(ai,screen))
	
	
	while True:
		x,y = 0,0
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x,y = pygame.mouse.get_pos()
				
			else:
				ai.check_events(event)
			
		screen.fill(ai.bg_color)
		
		for i in range(len(cells)):
			
			cells[i].show()
			cells[i].move()
			if x :
				coli = cells[i].collision(x,y)
				if coli :
					(cells.append(Cell(ai,screen,cells[i].x+5,cells[i].y,
						cells[i].r*0.8,cells[i].c)))
					(cells.append(Cell(ai,screen,cells[i].x-5,cells[i].y,
						cells[i].r*0.8,cells[i].c)))
					del cells[i]
				
		pygame.display.flip()
		
		
		
run()
