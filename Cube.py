# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Cube.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nsavry <nsavry@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/10/20 15:45:20 by nsavry            #+#    #+#              #
#    Updated: 2015/10/23 16:43:31 by nsavry           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
	
	def display(self):
		for i in range(-1,2):
			sys.stdout.write("             ")
			for j in range(-1,2):
				self.display_color(self.found_color(j, 1, i)[1])
			print "\n"

	def found_color(self, x, y, z):
		for sticker in self.cube:
			if ((sticker[0] == 0 and x == 0) or (sticker[0] != 0 and sticker[0] / abs(sticker[0])) == x):
				if ((sticker[1] == 0 and y == 0) or (sticker[1] != 0 and sticker[1] / abs(sticker[1])) == y):
					if ((sticker[2] == 0 and z == 0) or (sticker[2] != 0 and sticker[2] / abs(sticker[2])) == z):
						return sticker

	def display_color(self, color):
		i = " "
		j = " "
		color = abs(color)
		if color == 1:
			sys.stdout.write("\033[42m\033[30m" + str(i) + "\033[0m")
			sys.stdout.write("\033[42m\033[30m" + str(j) + "\033[0m")
		if color == 2:
			sys.stdout.write("\033[44m\033[30m" + str(i) + "\033[0m")
			sys.stdout.write("\033[44m\033[30m" + str(j) + "\033[0m")
		if color == 3:
			sys.stdout.write("\033[47m\033[30m" + str(i) + "\033[0m")
			sys.stdout.write("\033[47m\033[30m" + str(j) + "\033[0m")
		if color == 4:
			sys.stdout.write("\033[43m\033[30m" + str(i) + "\033[0m")
			sys.stdout.write("\033[43m\033[30m" + str(j) + "\033[0m")
		if color == 5:
			sys.stdout.write("\033[41m\033[30m" + str(i) + "\033[0m")
			sys.stdout.write("\033[41m\033[30m" + str(j) + "\033[0m")
		if color == 6:
			sys.stdout.write("\033[48;5;202m\033[30m" + str(i) + "\033[0m")
			sys.stdout.write("\033[48;5;202m\033[30m" + str(j) + "\033[0m")
		sys.stdout.write("  ")
