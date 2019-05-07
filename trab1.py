import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))

white=(255,255,255)
black=(0,0,0)

def bresenham(coord):
	start = coord[0]
	end = coord[1]
	x1, y1 = start
	x2, y2 = end
	tam_vert = pygame.display.get_surface().get_height()
	y1 = tam_vert - y1
	y2 = tam_vert - y2

	if x1>x2:
		x1,x2 = x2, x1
		y1,y2 = y2, y1

	dx = x2 - x1
	dy = abs(y2-y1)

	if y2-y1 < 0:
		sinaly = -1
	elif y2-y1>0:
		sinaly = 1
	else:
		sinaly = 0

	if dy>dx:
		dx, dy = dy, dx
		mudou = 1
	else:
		mudou = 0
	
	print("start and end xy = ["+str(x1))
	dy2   = 2*dy 
	dy2mdx  = dy2 - dx #2*dy - dx menos dx
	dydx2 = dy2 - 2*dx #2*dy*dx

	x = x1
	y = y1
	screen.set_at((x,y),white)

	for i in range(dx):
		if dy2mdx < 0:
			if mudou >0:
				y = y + sinaly
			else:
				x = x+1
			dy2mdx = dy2mdx + dy2
		else:
			y = y+sinaly
			x = x+1
			dy2mdx = dy2mdx + dydx2
		screen.set_at((x,y),white)

	pygame.display.flip()


def clica():
	i = 0
	posic = []
	while i<2:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()
			if e.type == pygame.MOUSEBUTTONDOWN:
				posic.append(pygame.mouse.get_pos())
				i = i+1
	print(posic)
	return posic


while 1:
	screen.fill((0,0,0))
	bresenham(clica())

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()