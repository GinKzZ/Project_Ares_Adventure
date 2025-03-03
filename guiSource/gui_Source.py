import os
import time
import copy
import sys
import pygame
import Function
import pygame_widgets
from pygame_widgets.dropdown import Dropdown
from . import gui_Attribute
sys.path.append(os.path.abspath(".."))

time_go = 6
exit_game = False
flag_pause = True
flag_start = False
flag_finish = False
count_Step = 0
pygame.font.init()
curPath = os.getcwd()
image1 = pygame.image.load(curPath + "/guiSource/wallpaper/wpp1.jpeg")
image2 = pygame.image.load(curPath + "/guiSource/wallpaper/wpp2.jpeg")
image3 = pygame.image.load(curPath + "/guiSource/wallpaper/wpp3.jpeg")
image1 = pygame.transform.scale(image1, (gui_Attribute.WIDTH1_SCREEN, gui_Attribute.HEIGHT1_SCREEN))
image2 = pygame.transform.scale(image2, (gui_Attribute.WIDTH1_SCREEN, gui_Attribute.HEIGHT1_SCREEN))
image3 = pygame.transform.scale(image3, (gui_Attribute.WIDTH2_SCREEN, gui_Attribute.HEIGHT2_SCREEN))
imagerect1 = image1.get_rect()
imagerect2 = image2.get_rect()
imagerect3 = image3.get_rect()
imagerect1.center = ((gui_Attribute.WIDTH1_SCREEN/2, gui_Attribute.HEIGHT1_SCREEN/2))
imagerect2.center = ((gui_Attribute.WIDTH1_SCREEN/2, gui_Attribute.HEIGHT1_SCREEN/2))
imagerect3.center = ((gui_Attribute.WIDTH2_SCREEN/2, gui_Attribute.HEIGHT2_SCREEN/2))

font1 = pygame.font.Font(None, gui_Attribute.TEXT_FONT1)
font2 = pygame.font.Font(None, gui_Attribute.TEXT_FONT2)
font3 = pygame.font.Font(None, gui_Attribute.TEXT_FONT3)

button_start_surface = pygame.Surface(gui_Attribute.BUTTON_START_SIZE, pygame.SRCALPHA)
button_start_surface.fill(gui_Attribute.GRAY_BUTTON) 
text_button_start = font1.render("START", True, gui_Attribute.BLACK)

button_exit_surface = pygame.Surface(gui_Attribute.BUTTON_EXIT_SIZE, pygame.SRCALPHA)
button_exit_surface.fill(gui_Attribute.GRAY_BUTTON) 
text_button_exit = font1.render("EXIT", True, gui_Attribute.BLACK)

box_input_surface = pygame.Surface(gui_Attribute.BOX_INPUT_SIZE, pygame.SRCALPHA)
box_input_surface.fill(gui_Attribute.GRAY_BUTTON) 
text_box_input = font2.render("CHOOSE YOUR INPUT", True, gui_Attribute.RED)

box_waiting = pygame.Surface(gui_Attribute.BOX_WAITING_SIZE, pygame.SRCALPHA)
box_waiting.fill(gui_Attribute.GRAY_BUTTON) 
text_box_waiting = font2.render("WAITING...", True, gui_Attribute.BLACK)

box_controller = pygame.Surface(gui_Attribute.BOX_CONTROLLER_SIZE, pygame.SRCALPHA)
box_controller.fill(gui_Attribute.GRAY_BUTTON) 

back_button = pygame.image.load(curPath + "/guiSource/icon/back_button.png")
back_button = pygame.transform.scale(back_button, gui_Attribute.BACK_BUTTON_SIZE)

start_button = pygame.image.load(curPath + "/guiSource/icon/start_button.png")
start_button = pygame.transform.scale(start_button, gui_Attribute.START_BUTTON_SIZE)

pause_button_1 = pygame.image.load(curPath + "/guiSource/icon/pause_button_1.png")
pause_button_1 = pygame.transform.scale(pause_button_1, gui_Attribute.PAUSE_BUTTON_SIZE)

pause_button_2 = pygame.image.load(curPath + "/guiSource/icon/pause_button_2.png")
pause_button_2 = pygame.transform.scale(pause_button_2, gui_Attribute.PAUSE_BUTTON_SIZE)

white_circle = pygame.image.load(curPath + "/guiSource/icon/white_circle.png")
white_circle = pygame.transform.scale(white_circle, gui_Attribute.PAUSE_BUTTON_SIZE)

reset_button = pygame.image.load(curPath + "/guiSource/icon/reset_button.png")
reset_button = pygame.transform.scale(reset_button, gui_Attribute.RESET_BUTTON_SIZE)

block_gray = pygame.Surface(gui_Attribute.SIDE, pygame.SRCALPHA)
block_gray.fill(gui_Attribute.GRAY_BUTTON_DIF) 

text_box_step = font2.render("STEP", True, gui_Attribute.BLACK)
box_step_surface = pygame.Surface((55, 30), pygame.SRCALPHA)
box_step_surface.fill(gui_Attribute.WHITE)

wall = pygame.image.load(curPath + "/guiSource/icon/wall.png")
wall = pygame.transform.scale(wall, gui_Attribute.SIDE)

person = pygame.image.load(curPath + "/guiSource/icon/miner.png")
person = pygame.transform.scale(person, gui_Attribute.SIDE)

switch = pygame.image.load(curPath + "/guiSource/icon/bullet_point.png")
switch = pygame.transform.scale(switch, gui_Attribute.SIDE)

stone = pygame.image.load(curPath + "/guiSource/icon/diamond.png")
stone = pygame.transform.scale(stone, gui_Attribute.SIDE)

def end_Program():
	pygame.display.quit()
	pygame.quit()
	quit()

def draw_Window1(Screen):
	Screen.blit(image1, imagerect1)
	Screen.blit(button_start_surface, gui_Attribute.BUTTON_START_POS)
	Screen.blit(button_exit_surface, gui_Attribute.BUTTON_EXIT_POS)
	Screen.blit(text_button_start, gui_Attribute.TEXT_BUTTON_START_POS)
	Screen.blit(text_button_exit, gui_Attribute.TEXT_BUTTON_EXIT_POS)
	pygame.display.update()

	global exit_game
	while exit_game == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end_Program()				
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouse_x, mouse_y = pygame.mouse.get_pos()

					start_rect = pygame.Rect(gui_Attribute.BUTTON_START_POS, gui_Attribute.BUTTON_START_SIZE)
					exit_rect = pygame.Rect(gui_Attribute.BUTTON_EXIT_POS, gui_Attribute.BUTTON_EXIT_SIZE)

					if start_rect.collidepoint(mouse_x, mouse_y):
						input_box = Function.makeBoxFileInput()
						draw_Window2(Screen, input_box)

					if exit_rect.collidepoint(mouse_x, mouse_y):
						end_Program()

def draw_Input_Box(Screen, input_box):
	for box in input_box:
		box_input = pygame.Surface(box.box_size, pygame.SRCALPHA)
		box_input.fill(gui_Attribute.GRAY_BUTTON) 
		text_box = font3.render(box.name, True, gui_Attribute.BLACK)
		Screen.blit(box_input, box.box_pos)
		Screen.blit(text_box, box.text_pos)

def draw_Window2(Screen, input_box):
	Screen = pygame.display.set_mode((gui_Attribute.WIDTH1_SCREEN, gui_Attribute.HEIGHT1_SCREEN))	
	Screen.blit(image2, imagerect2)
	Screen.blit(box_input_surface, gui_Attribute.BOX_INPUT_POS)
	Screen.blit(text_box_input, gui_Attribute.TEXT_BOX_INPUT_POS)
	draw_Input_Box(Screen, input_box)
	pygame.display.update()

	global exit_game
	while exit_game == False:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				end_Program()

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouse_x, mouse_y = pygame.mouse.get_pos()

					for box in input_box:
						box_rec = pygame.Rect(box.box_size, box.box_pos)
						if box_rec.collidepoint(mouse_x, mouse_y):
							Screen.blit(box_waiting, gui_Attribute.BOX_WAITING_POS)
							Screen.blit(text_box_waiting, gui_Attribute.TEXT_BOX_WAITING_POS)
							pygame.display.update()
							draw_Window3(Screen, box.name, input_box)

def draw_button(Screen):
	Screen.blit(box_controller, gui_Attribute.BOX_CONTROLLER_POS)
	Screen.blit(back_button, gui_Attribute.BACK_BUTTON_POS)
	Screen.blit(start_button, gui_Attribute.START_BUTTON_POS)
	if flag_start == False or flag_pause == True: 
		Screen.blit(pause_button_2, gui_Attribute.PAUSE_BUTTON_POS)
	else:
		Screen.blit(pause_button_1, gui_Attribute.PAUSE_BUTTON_POS)
	Screen.blit(reset_button, gui_Attribute.RESET_BUTTON_POS)
	Screen.blit(box_step_surface, (470, 0))
	Screen.blit(text_box_step, (390, 5))

def draw_matrix(Screen, distance, matrix):
	sideOfIcon = gui_Attribute.SIDE[0]
	curWidth = distance[1]
	curHeight = distance[0]
	for row in matrix:
		for element in row:
			match element:
				case '#':
					Screen.blit(wall, (curWidth, curHeight))					
				case '.':
					Screen.blit(block_gray, (curWidth, curHeight))
					Screen.blit(switch, (curWidth, curHeight))
				case '*':
					Screen.blit(block_gray, (curWidth, curHeight))
					Screen.blit(switch, (curWidth, curHeight))
				case '+':
					Screen.blit(block_gray, (curWidth, curHeight))
					Screen.blit(switch, (curWidth, curHeight))
				case _:
					Screen.blit(block_gray, (curWidth, curHeight))
			curWidth += sideOfIcon
		curHeight += sideOfIcon
		curWidth = distance[1]

def draw_PS(Screen, Stones, ares):
	for s in Stones:
		Screen.blit(stone, s.S_pos)
		weight = font3.render(s.weight, True, gui_Attribute.BLACK)
		Screen.blit(weight, (s.S_pos[0]+10, s.S_pos[1]+5))

	Screen.blit(person, ares.A_pos)

def solve_Maze(Screen, steps, Stones, ares, step_size):
	global count_Step, flag_start, flag_pause, flag_finish, time_go
	if len(steps) == 0:
		flag_start = False
		flag_pause = True
		flag_finish = True
		return steps
	step = steps[-1]
	steps = steps[:-1]
	count_Step += 1
	time.sleep(0.2)
	match step:
		case 'u':
			for i in range(0, time_go):
				ares.A_pos[1] -= step_size/time_go 
		case 'd':
			for i in range(0, time_go):
				ares.A_pos[1] += step_size/time_go
		case 'r':
			for i in range(0, time_go):
				ares.A_pos[0] += step_size/time_go 
		case 'l':
			for i in range(0, time_go):
				ares.A_pos[0] -= step_size/time_go
		case 'U':
			stone_move = None 
			for stone in Stones:
				stone_rec = pygame.Rect(stone.S_pos, stone.S_size)
				if stone_rec.collidepoint(ares.A_pos[0], ares.A_pos[1]-step_size):
					stone_move = stone
					break
			for i in range(0, time_go):
				ares.A_pos[1] -= step_size/time_go
				stone_move.S_pos[1] -= step_size/time_go
		case 'D':
			stone_move = None
			for stone in Stones:
				stone_rec = pygame.Rect(stone.S_pos, stone.S_size)
				if stone_rec.collidepoint(ares.A_pos[0], ares.A_pos[1]+step_size):
					stone_move = stone
					break
			for i in range(0, time_go):
				ares.A_pos[1] += step_size/time_go 
				stone_move.S_pos[1] += step_size/time_go
		case 'R':
			stone_move = None
			for stone in Stones:
				stone_rec = pygame.Rect(stone.S_pos, stone.S_size)
				if stone_rec.collidepoint(ares.A_pos[0]+step_size, ares.A_pos[1]):
					stone_move = stone
					break
			for i in range(0, time_go):
				ares.A_pos[0] += step_size/time_go 
				stone_move.S_pos[0] += step_size/time_go
		case 'L':
			stone_move = None
			for stone in Stones:
				stone_rec = pygame.Rect(stone.S_pos, stone.S_size)
				if stone_rec.collidepoint(ares.A_pos[0]-step_size, ares.A_pos[1]):
					stone_move = stone
					break
			for i in range(0, time_go):
				ares.A_pos[0] -= step_size/time_go
				stone_move.S_pos[0] -= step_size/time_go
	return steps

def draw_Window3(Screen, file_name, input_box):
	stone_weight, matrix = Function.readFile(file_name)
	Function.solveAllAlgorithm(stone_weight, matrix, file_name)
	Stones, ares, distance = Function.makeStoneAndPerson(stone_weight, matrix)
	my_dict_al = Function.readFileOutput(file_name)
	Stones_back_up = copy.deepcopy(Stones)
	ares_back_up = copy.deepcopy(ares)
	steps = ""
	step_size = gui_Attribute.SIDE[0]

	flag = False
	lastVal = -1
	valAl = 0
	back_rec = pygame.Rect(gui_Attribute.BACK_BUTTON_POS, gui_Attribute.BACK_BUTTON_SIZE)
	start_rec = pygame.Rect(gui_Attribute.START_BUTTON_POS, gui_Attribute.START_BUTTON_SIZE)
	pause_rec = pygame.Rect(gui_Attribute.PAUSE_BUTTON_POS, gui_Attribute.PAUSE_BUTTON_SIZE)
	reset_rec = pygame.Rect(gui_Attribute.RESET_BUTTON_POS, gui_Attribute.RESET_BUTTON_SIZE)
	dropdown = Dropdown(Screen, gui_Attribute.DROPDOWN_POSX, gui_Attribute.DROPDOWN_POSY, 
		gui_Attribute.DROPDOWN_WIDTH, gui_Attribute.DROPDOWN_HEIGHT, name='Select algorithm',
	    choices=['BFS','DFS', 'UCS', 'A*', 'GBFS', 'SWARM', "DIJKSTRA"],
	    borderRadius=3, colour=pygame.Color('green'), values=[1, 2, 3, 4, 5, 6, 7], direction='down', textHAlign='left')

	Screen = pygame.display.set_mode((gui_Attribute.WIDTH2_SCREEN, gui_Attribute.HEIGHT2_SCREEN))	
	Screen.blit(image3, imagerect3)
	draw_button(Screen)
	draw_matrix(Screen, distance, matrix)
	draw_PS(Screen, Stones, ares)
	pygame.display.update()

	global exit_game, flag_start, flag_pause, flag_finish, count_Step
	while exit_game == False:
		events = pygame.event.get()
		for event in events:
			if event.type == pygame.QUIT:
					end_Program()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					mouse_x, mouse_y = pygame.mouse.get_pos()

					if back_rec.collidepoint(mouse_x, mouse_y):
						flag_pause = True
						flag_start = False
						flag_finish = False
						count_Step = 0
						count_Step = 0
						return draw_Window2(Screen, input_box)
					if start_rec.collidepoint(mouse_x, mouse_y) and flag_start == False and flag_finish == False:
						flag_start = True
						flag_pause = False
						drop = dropdown.getSelected()
						if drop == None:
							steps = my_dict_al[1].listOfStep
						else:
							steps = my_dict_al[drop].listOfStep
						steps = steps[::-1]
					if pause_rec.collidepoint(mouse_x, mouse_y):
						if flag_pause == True:
							flag_pause = False
						else:
							flag_pause = True
					if reset_rec.collidepoint(mouse_x, mouse_y):
						flag_pause = True
						flag_start = False
						flag_finish = False
						count_Step = 0
						Stones = copy.deepcopy(Stones_back_up)
						ares = copy.deepcopy(ares_back_up)
						draw_button(Screen)
						draw_matrix(Screen, distance, matrix)
						draw_PS(Screen, Stones, ares)
						pygame.display.update()					

		if flag_start == True and flag_pause == False:
			steps = solve_Maze(Screen, steps, Stones, ares, step_size)
		if flag_pause:
			Screen.blit(white_circle, gui_Attribute.PAUSE_BUTTON_POS)
			Screen.blit(pause_button_2, gui_Attribute.PAUSE_BUTTON_POS)
		else:
			Screen.blit(white_circle, gui_Attribute.PAUSE_BUTTON_POS)
			Screen.blit(pause_button_1, gui_Attribute.PAUSE_BUTTON_POS)

		Screen.blit(image3, imagerect3)
		draw_button(Screen)
		draw_matrix(Screen, distance, matrix)
		draw_PS(Screen, Stones, ares)
		text_count_step = font1.render(str(count_Step), True, gui_Attribute.BLACK)
		Screen.blit(text_count_step, (471, 1))
				
		valDD = dropdown.getSelected()
		if valDD != None and valDD != lastVal:
			lastVal = valDD
			Screen.blit(image3, imagerect3)
			draw_button(Screen)
			draw_matrix(Screen, distance, matrix)
			draw_PS(Screen, Stones, ares)
		pygame_widgets.update(events)
		pygame.display.update()

def draw_UI():
	pygame.init()

	Screen = pygame.display.set_mode((gui_Attribute.WIDTH1_SCREEN, gui_Attribute.HEIGHT1_SCREEN))
	pygame.display.set_caption('Ares’s adventure')

	draw_Window1(Screen)