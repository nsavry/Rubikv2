import sys

class Cube:
	def init(self):
		self.edge = [[0,2,1],[3,0,1],[0,-4,1],[-5,0,1],
					[0,2,-6],[3,0,-6],[0,-4,-6],[-5,0,-6],
					[3,2,0],[3,-4,0],[-5,2,0],[-5,-4,0]]
		self.corner = [[-5,2,1],[3,2,1],[3,-4,1],[-5,-4,1],
					[-5,2,-6],[3,2,-6],[3,-4,-6],[-5,-4,-6]]
		self.fixed = [[0,0,1],[0,0,-6],[0,2,0],[0,-4,0],[3,0,0],[-5,0,0]]
		self.cube = self.edge + self.corner + self.fixed
		self.move_tab = {"U": [1, 2, 0, True, 1], "U'": [1, 0, 2, True, 1], "U2": [1, 2, 0, True, 2],
						"F": [2, 0, 1, True, 1], "F'": [2, 1, 0, True, 1], "F2": [2, 0, 1, True, 2],
						"R": [0, 1, 2, True, 1], "R'": [0, 2, 1, True, 1], "R2": [0, 1, 2, True, 2],
						"L": [0, 1, 2, False, 1], "L'": [0, 2, 1, False, 1], "L2": [0, 1, 2, False, 2],
						"B": [2, 0, 1, False, 1], "B'": [2, 1, 0, False, 1], "B2": [2, 0, 1, False, 2],
						"D": [1, 2, 0, False, 1], "D'": [1, 0, 2, False, 1], "D2": [1, 2, 0, False, 2]}
	
	def display(self):
		for i in range(-1,2):
			sys.stdout.write("              ")
			for j in range(-1,2):
				self.display_color(self.find_sticker(j, 1, i)[1])
			print "\n"
		for j in range(-1,2):
			sys.stdout.write("  ")
			for i in range(-1,2):
				self.display_color(self.find_sticker(-1, -j, i)[0])
			for i in range(-1,2):
				self.display_color(self.find_sticker(i, -j, 1)[2])
			for i in range(-1,2):
				self.display_color(self.find_sticker(1, -j, -i)[0])
			for i in range(-1,2):
				self.display_color(self.find_sticker(-i, -j, -1)[2])
			print "\n"
		for i in range(-1,2):
			sys.stdout.write("              ")
			for j in range(-1,2):
				self.display_color(self.find_sticker(j, -1, -i)[1])
			print "\n"

	def find_sticker(self, x, y, z):
		for sticker in self.cube:
			if ((sticker[0] == 0 and x == 0) or (sticker[0] != 0 and sticker[0] / abs(sticker[0])) == x):
				if ((sticker[1] == 0 and y == 0) or (sticker[1] != 0 and sticker[1] / abs(sticker[1])) == y):
					if ((sticker[2] == 0 and z == 0) or (sticker[2] != 0 and sticker[2] / abs(sticker[2])) == z):
						return sticker

	def display_color(self, color):
		i = "  "
		color = abs(color)
		tab = ["42", "47", "41", "43", "48;5;202", "44"]
		sys.stdout.write("\033[" + tab[color-1] + "m\033[30m" + str(i) + "\033[0m")
		sys.stdout.write("  ")
	
	def move(self, tab):
		for _ in range(tab[4]):
			i = 0
			for sticker in self.cube:
				if tab[3] == True:
					if sticker[tab[0]] > 0:
						tmp = self.cube[i][tab[1]]
						self.cube[i][tab[1]] = self.cube[i][tab[2]]
						self.cube[i][tab[2]] = -tmp
				else:
					if sticker[tab[0]] < 0:
						tmp = self.cube[i][tab[2]]
						self.cube[i][tab[2]] = self.cube[i][tab[1]]
						self.cube[i][tab[1]] = -tmp
				i += 1

	def resolved(self):
		cube_resolved = Cube()
		cube_resolved.init()
		n_edge = 12
		n_corner = 8
		for edge in self.edge:
			for res_edge in cube_resolved.edge:
				if edge == res_edge:
					n_edge -= 1
		for corner in self.corner:
			for res_corner in cube_resolved.corner:
				if corner == res_corner:
					n_corner -= 1
		if n_corner != 0 and n_edge != 0:
			return False
		else:
			return True

	def yellow_cross(self):
		n_edge = 4
		for edge in self.edge:
			if edge == [0,-4,1] or edge == [0,-4,-6] or edge == [3,-4,0] or edge == [-5,-4,0]:
				n_edge -= 1
		if n_edge != 0:
			return False
		return True
	
	def first_ring(self):
		if self.yellow_cross() == False:
			return False
		n_corner = 4
		for corner in self.corner:
			if corner == [3,-4,1] or corner == [-5,-4,1] or corner == [3,-4,-6] or corner == [-5,-4,-6]:
				n_corner -= 1
		if n_corner != 0:
			return False
		return True

	def second_ring(self):
		if self.first_ring() == False:
			return False
		n_edge = 4
		for edge in self.edge:
			if edge == [3,0,1] or edge == [3,0,-6] or edge == [-5,0,1] or edge == [-5,0,-6]:
				n_edge -= 1
		if n_edge != 0:
			return False
		return True
