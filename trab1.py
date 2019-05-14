import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((600,400))
tela = pygame.Surface((600, 400))
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

menu_font = pygame.font.Font(None, 17)

limpar_txt = menu_font.render("Limpar", True, black)
linha_txt = menu_font.render("Linha", True, black)
retangulo_txt = menu_font.render("Retangulo", True, black)
quadrado_txt = menu_font.render("Quadrado", True, black)
circulo_txt = menu_font.render("Circulo", True, black)
polilinha_txt = menu_font.render("Polilinha", True, black)
curva_txt = menu_font.render("Curva", True, black)
preenchimento_txt = menu_font.render("Preench.", True, black)
lista_cores = [white,silver,gray,black,maroon,red,magenta,purple,navy,blue,teal,teal,aqua,lime,green,olive,yellow]
color = black #default
funcao = 1 #1 = Bresenham #2=...
preenchido = False
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
limpar_rect = pygame.Rect(5,200,42,20)
linha_rect = pygame.Rect(5,222,42,20)
retangulo_rect = pygame.Rect(5,244,42,20)
quadrado_rect = pygame.Rect(5,266,42,20)
polilinha_rect = pygame.Rect(5,288,42,20)
curva_rect = pygame.Rect(5,310,42,20)
circulo_rect = pygame.Rect(5,332,42,20)
preenchimento_rect = pygame.Rect(5,354,42,20)

lista_rect_cores = [white_rect,silver_rect,gray_rect,black_rect,maroon_rect,red_rect,magenta_rect,purple_rect,navy_rect,blue_rect,teal_rect,teal_rect,aqua_rect,lime_rect,green_rect,olive_rect,yellow_rect]

def desenha_menu():
	for x in range(len(lista_cores)):
		pygame.draw.rect(screen,lista_cores[x],lista_rect_cores[x])
		if color == lista_cores[x]:
			border = 3
		else:
			border = 1
			pygame.draw.rect(screen, black, lista_rect_cores[x], border)
	pygame.draw.rect(screen,silver,limpar_rect)
	screen.blit(limpar_txt,(7,204))
	pygame.draw.rect(screen,silver,linha_rect)
	screen.blit(linha_txt,(7,226))
	pygame.draw.rect(screen,silver,retangulo_rect)
	screen.blit(retangulo_txt,(7,248))
	pygame.draw.rect(screen,silver,quadrado_rect)
	screen.blit(quadrado_txt,(7,270))
	pygame.draw.rect(screen,silver,polilinha_rect)
	screen.blit(polilinha_txt,(7,292))
	pygame.draw.rect(screen,silver,curva_rect)
	screen.blit(curva_txt,(7,314))
	pygame.draw.rect(screen,silver,circulo_rect)
	screen.blit(circulo_txt,(7,336))
	pygame.draw.rect(screen,silver,curva_rect)
	screen.blit(curva_txt,(7,314))
	if preenchido == True:
		pygame.draw.rect(screen,silver,preenchimento_rect)
	else:
		pygame.draw.rect(screen,gray,preenchimento_rect)
	screen.blit(preenchimento_txt,(7,359))

# collision detection for COLOR
def escolhe_menu(mouse_pos): 
	global color
	global funcao
	global preenchido
	if white_rect.collidepoint(mouse_pos):
		color = white
	elif silver_rect.collidepoint(mouse_pos):
		color = silver
	elif gray_rect.collidepoint(mouse_pos):
		color = gray
	elif black_rect.collidepoint(mouse_pos):
		color = black
	elif maroon_rect.collidepoint(mouse_pos):
		color = maroon
	elif red_rect.collidepoint(mouse_pos):
		color = red
	elif magenta_rect.collidepoint(mouse_pos):
		color = magenta
	elif purple_rect.collidepoint(mouse_pos):
		color = purple
	elif navy_rect.collidepoint(mouse_pos):
		color = navy
	elif blue_rect.collidepoint(mouse_pos):
		color = blue
	elif teal_rect.collidepoint(mouse_pos):
		color = teal
	elif aqua_rect.collidepoint(mouse_pos):
		color = aqua
	elif lime_rect.collidepoint(mouse_pos):
		color = lime
	elif green_rect.collidepoint(mouse_pos):
		color = green
	elif olive_rect.collidepoint(mouse_pos):
		color = olive
	elif yellow_rect.collidepoint(mouse_pos):
		color = yellow
	elif limpar_rect.collidepoint(mouse_pos):
		limpa_tela()
	elif linha_rect.collidepoint(mouse_pos):
		funcao = 1
	elif quadrado_rect.collidepoint(mouse_pos):
		funcao = 2
	elif polilinha_rect.collidepoint(mouse_pos):
		funcao = 3
	elif circulo_rect.collidepoint(mouse_pos):
		funcao = 4
	elif curva_rect.collidepoint(mouse_pos):
		funcao = 5
	elif retangulo_rect.collidepoint(mouse_pos):
		funcao = 6
	elif preenchimento_rect.collidepoint(mouse_pos):
		preenchido = not preenchido
		desenha_menu()
		pygame.display.flip()
		


def limpa_tela():
	screen.fill(white)
	desenha_menu()
	tela.blit(screen,(0,0),menu_rect)
	pygame.draw.line(screen, black, (55, 40), (55, 360))
	pygame.draw.line(screen, black, (59, 40), (59, 360))
	pygame.display.flip()


def frange(start, stop, step):#para aceitar float
	x = start
	while x < stop:
		yield x
		x += step

def bezier():
	coord = []
	coord[0:1] = pipf()
	coord[2:3] = pipf()
	for t in frange(0,1,0.01):
		x1,y1 = coord[0] #ponto onde começa da curva
		x2,y2 = coord[1] #primeiro ponto de controle
		x3,y3 = coord[2] #segundo ponto de controle
		x4,y4 = coord[3] #ponto onde termina a curva
		omt = 1-t
		omt2 = omt*omt
		omt3 = omt2*omt
		t2 = t*t
		t3 = t2*t
		x = omt3 * x1 + ((3*omt2)*t*x2) + (3*omt*t2*x3)+t3*x4
		y = omt3 * y1 + ((3*omt2)*t*y2) + (3*omt*t2*y3)+t3*y4
		
		x = int(round(x,0))#arredonda e transforma para inteiro
		y = int(round(y,0))

		screen.set_at((x,y),color)
		pygame.display.flip()

def circle(): #cx,cy = centro da circunferencia
	(cx,cy),(aux1,aux2) = pipf()
	raio = int(((abs(cx-aux1)**2)+(abs(cy-aux2)**2))**(1/2))
	if preenchido:
		cont = raio
	else:
		cont = 1

	for linha in range(cont):
		x = 0
		y = raio
		d = 1-raio
		while x < y:
			plotCircle(x,y,cx,cy)
			x += 1
			if d < 0:
				d += 2 * x + 1
			else:
				y -= 1
				d += 2*(x-y) + 1
		raio = raio -1

	pygame.display.flip()


def plotCircle(x,y,cx,cy):
	gfxdraw.pixel(screen,cx+x,cy+y,color)
	gfxdraw.pixel(screen,cx-x,cy+y,color)
	gfxdraw.pixel(screen,cx+x,cy-y,color)
	gfxdraw.pixel(screen,cx-x,cy-y,color)
	gfxdraw.pixel(screen,cx+y,cy+x,color)
	gfxdraw.pixel(screen,cx-y,cy+x,color)
	gfxdraw.pixel(screen,cx+y,cy-x,color)
	gfxdraw.pixel(screen,cx-y,cy-x,color)

def polilinha():
	c1, c2 = bresenham(pipf()) #pega esse ultimo ponto

	while funcao == 3:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				a,b,c = pygame.mouse.get_pressed()
				if(c == True):
					break #sai do loop ao apertar o botão esquerdo
				else:
					x,y = pygame.mouse.get_pos()
					if (x<59):
						escolhe_menu((x,y))
						if funcao != 3: #se mudar de ferramenta
							break
					else:
						c1, c2 = bresenham([(c1,c2),(x,y)])
			if event.type == pygame.QUIT: sys.exit()

def pipf(): #ponto final, ponto inicial
	i = 0
	posic = []
	while i<2:
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()
			if e.type == pygame.MOUSEBUTTONDOWN:
				a = pygame.mouse.get_pos()
				if (a[0]<59):
					escolhe_menu(a)
				else:
					posic.append(pygame.mouse.get_pos())
					i = i+1
	return posic


def retangulo():
	[(x,y),(x2,y2)] = pipf()
	if preenchido:
		if x>x2:
			(x,y),(x2,y2) = (x2,y2),(x,y)
		while(x<=x2):
			bresenham([(x,y),(x,y2)])
			x = x+1
	else:
		bresenham([(x,y),(x2,y)])
		bresenham([(x,y),(x,y2)])
		bresenham([(x,y2),(x2,y2)])
		bresenham([(x2,y),(x2,y2)])

def linha():
	bresenham(pipf())

def quadrado():
	[(x,y),(x2,y2)] = pipf()
	if (abs(x-x2)>abs(y-y2)):
		lado = abs(x-x2)
	else:
		lado = abs(y-y2)
	if preenchido:
		if(x>x2):
			(x,y),(x2,y2) = (x2,y2),(x,y)
		x,y = x-lado,y-lado
		x2,y2 = x+lado,y+lado
		while(x<=x2):
			bresenham([(x,y),(x,y2)])
			x = x+1
	else:
		bresenham([(x-lado,y-lado),(x-lado,y+lado)]) #Ponto1 ao Ponto2
		bresenham([(x-lado,y-lado),(x+lado,y-lado)]) #Ponto1 ao Ponto3
		bresenham([(x+lado,y-lado),(x+lado,y+lado)]) #Ponto3 ao Ponto4
		bresenham([(x-lado,y+lado),(x+lado,y+lado)]) #Ponto2 ao Ponto4

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

limpa_tela()
while True:
	if funcao == 1:
		linha()
	elif funcao == 2:
		quadrado()
	elif funcao == 3:
		polilinha()
	elif funcao == 4:
		circle()
	elif funcao == 5:
		bezier()
	elif funcao == 6:
		retangulo()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()