import os
import copy
from searchAlgorithm import *
from guiSource.gui_Attribute import WIDTH2_SCREEN, HEIGHT2_SCREEN, HEIGHT_BOX_CONTROLLER

WIDTH = 30

class Box:
	def __init__(self, name, box_size, box_pos, text_pos):
		self.name = name
		self.box_size = box_size
		self.box_pos = box_pos
		self.text_pos = text_pos

class Stone:
	def __init__(self, weight, S_size, S_pos):
		self.weight = str(weight)
		self.S_size = S_size
		self.S_pos = S_pos
	
class Ares:
	def __init__(self, A_size, A_pos):
		self.A_size = A_size
		self.A_pos = A_pos

class Algorithm:
	def __init__(self, name, step, weight, node, time, memory, listOfStep):
		self.name = name
		self.step = step
		self.weight = weight
		self.node = node
		self.time = time
		self.memory = memory
		self.listOfStep = listOfStep

def makeBoxFileInput():
	input_box = []
	folder_path = "Inputs"
	file_list = os.listdir(folder_path)

	width = 80
	height = 30
	numOfBox = 0
	numOfBoxOnLine = 3
	dis_from_leftSide = 35
	dis_from_top = 90
	dis_between_box_hor = 20
	dis_between_box_ver = 30

	for file in file_list:
		posX_temp = dis_from_leftSide + numOfBox*(width + dis_between_box_hor)
		posY_temp = dis_from_top
		input_box.append(Box(file, (width, height), (posX_temp, posY_temp), (posX_temp+1, posY_temp+7)))
		numOfBox += 1
		if numOfBox == numOfBoxOnLine:
			numOfBox = 0
			dis_from_top += height + dis_between_box_ver
	
	return input_box

def readFile(file_name):
	with open(os.getcwd() + "/Inputs/" + file_name, "r") as file:
		stone_weight = list(map(int, file.readline().split()))
		matrix = [list(line.rstrip("\n")) for line in file]
	return stone_weight, matrix

def makeStoneAndPerson(stone_weight, matrix):
	ares = ()
	countStone = 0
	countTop = 0
	dis_from_top = (HEIGHT2_SCREEN - HEIGHT_BOX_CONTROLLER - len(matrix)*WIDTH) / 2 + HEIGHT_BOX_CONTROLLER
	dis_from_leftSide = (WIDTH2_SCREEN - len(matrix[0])*WIDTH) / 2
	Stones = []
	for row in matrix:
		countLeft = 0
		for element in row:
			match element:
				case '$':
					Stones.append(Stone(stone_weight[countStone], (WIDTH, WIDTH), [dis_from_leftSide + WIDTH*countLeft, dis_from_top + WIDTH*countTop]))
					countStone += 1
				case '@':
					ares = Ares((WIDTH, WIDTH), [dis_from_leftSide + WIDTH*countLeft, dis_from_top + WIDTH*countTop])
				case '*':
					Stones.append(Stone(stone_weight[countStone], (WIDTH, WIDTH), [dis_from_leftSide + WIDTH*countLeft, dis_from_top + WIDTH*countTop]))
					countStone += 1
				case '+':
					ares = Ares((WIDTH, WIDTH), [dis_from_leftSide + WIDTH*countLeft, dis_from_top + WIDTH*countTop])
			countLeft += 1
		countTop += 1
	return Stones, ares, (dis_from_top, dis_from_leftSide)

def readFileOutput(file_name):
	my_dict_al = {}
	output_name = file_name.replace("input", "output")
	with open(os.getcwd() + "/Outputs/" + output_name, "r") as file:
		lines = file.readlines()

	i = 0
	count = 1
	while i < len(lines):
		name = lines[i].strip()
		i += 1
		details = lines[i].strip().split(", ")
		i += 1
		path = lines[i].strip()
		i += 1

		steps = int(details[0].split(": ")[1])
		weight = int(details[1].split(": ")[1])
		nodes = int(details[2].split(": ")[1])
		time = float(details[3].split(": ")[1])
		memory = float(details[4].split(": ")[1])

		al_temp = Algorithm(name, steps, weight, nodes, time, memory, path)
		my_dict_al[count] = al_temp
		count += 1

	return my_dict_al

def solveAllAlgorithm(stone_weight, matrix, file_name):	
	path = ""
	output_name = file_name.replace("input", "output")
	with open(os.getcwd() + "/Outputs/" + output_name, "w") as file:
		path += BFS_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		path += DFS_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		path += UCS_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		path += A_star_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		path += GBFS_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		path += SWARM_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		path += DIJKSTRA_solve(copy.deepcopy(matrix), stone_weight)+ "\n"
		print(f"Finish file {output_name}")
		file.write(path)
