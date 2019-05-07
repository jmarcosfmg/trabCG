import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))


white=(255,255,255)
black=(0,0,0)
red = (255,0,0)
lime = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
aqua = (0,255,255)
magenta = (255,0,255)
silver = (192,192,192)
gray = (128,128,128)
maroon = (128,0,0)
olive = (128,128,0)
green = (0,128,0)
purple = (128,0,128)
teal = (0,128,128)
navy = (0,0,128)

color = black #default

def bresenham(coord):
	start = coord[0]
	end = coord[1]
	x1, y1 = start
	x2, y2 = end
	tam_vert = pygame.display.get_surface().get_height()
	
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
		screen.set_at((x,y),color)

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

screen.fill(white)
pygame.display.flip()
while 1:
	screen.fill(white)
	bresenham(clica())

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()