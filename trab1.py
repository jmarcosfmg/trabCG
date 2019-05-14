import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((400,400))
tela = pygame.Surface((500, 400))

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
screen.fill(white)
lista_cores = [white,silver,gray,black,maroon,red,magenta,purple,navy,blue,teal,teal,aqua,lime,green,olive,yellow]
color = black #default

menu_rect = pygame.Rect(0, 0, 100, 400)
screen_rect = pygame.Rect(100, 0, 400, 400)

white_rect = pygame.Rect(5, 25, 20, 20)
silver_rect = pygame.Rect(27, 25, 20, 20)
gray_rect = pygame.Rect(5, 47, 20, 20)
black_rect = pygame.Rect(27, 47, 20, 20)
maroon_rect = pygame.Rect(5, 69, 20, 20)
red_rect = pygame.Rect(27, 69, 20, 20)
magenta_rect = pygame.Rect(5, 91, 20, 20)
purple_rect = pygame.Rect(27, 91, 20, 20)
navy_rect = pygame.Rect(5, 113, 20, 20)
blue_rect = pygame.Rect(27, 113, 20, 20)
teal_rect = pygame.Rect(5, 135, 20, 20)
aqua_rect = pygame.Rect(27, 135, 20, 20)
lime_rect = pygame.Rect(5, 157, 20, 20) 
green_rect = pygame.Rect(27, 157, 20, 20)
olive_rect = pygame.Rect(5, 179, 20, 20)
yellow_rect = pygame.Rect(27, 179, 20, 20)

lista_rect_cores = [white_rect,silver_rect,gray_rect,black_rect,maroon_rect,red_rect,magenta_rect,purple_rect,navy_rect,blue_rect,teal_rect,teal_rect,aqua_rect,lime_rect,green_rect,olive_rect,yellow_rect]

draw = False

def rect_b_color():
	for x in range(len(lista_cores)):
		pygame.draw.rect(screen,lista_cores[x],lista_rect_cores[x])
		if color == lista_cores[x]:
			border = 3
		else:
			border = 1
			pygame.draw.rect(screen, black, lista_rect_cores[x], border)

# collision detection for COLOR
def escolher_cor(mouse_pos): 
	global color
	if white_rect.collidepoint(mouse_pos):
		color = white
	if silver_rect.collidepoint(mouse_pos):
		color = silver
	if gray_rect.collidepoint(mouse_pos):
		color = gray
	if black_rect.collidepoint(mouse_pos):
		color = black
	if maroon_rect.collidepoint(mouse_pos):
		color = maroon
	if red_rect.collidepoint(mouse_pos):
		color = red
	if magenta_rect.collidepoint(mouse_pos):
		color = magenta
	if purple_rect.collidepoint(mouse_pos):
		color = purple
	if navy_rect.collidepoint(mouse_pos):
		color = navy
	if blue_rect.collidepoint(mouse_pos):
		color = blue
	if teal_rect.collidepoint(mouse_pos):
		color = teal
	if aqua_rect.collidepoint(mouse_pos):
		color = aqua
	if lime_rect.collidepoint(mouse_pos):
		color = lime
	if green_rect.collidepoint(mouse_pos):
		color = green
	if olive_rect.collidepoint(mouse_pos):
		color = olive
	if yellow_rect.collidepoint(mouse_pos):
		color = yellow

rect_b_color()
tela.blit(screen,(0,0),menu_rect)

pygame.draw.line(screen, black, (95, 40), (95, 360))
pygame.draw.line(screen, black, (100, 40), (100, 360))

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
	screen.set_at((x,y),color)

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
	return end #retorna o ultimo ponto

def clica():
	i = 0
	posic = []
	while i<2:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()
			if e.type == pygame.MOUSEBUTTONDOWN:
				a = pygame.mouse.get_pos()
				if (a[0]<100):
					escolher_cor(a)
				else:
					posic.append(pygame.mouse.get_pos())
					i = i+1
	return posic


pygame.display.flip()
while 1:
	
	bresenham(clica())

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()