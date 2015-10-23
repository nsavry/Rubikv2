# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Cube.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nsavry <nsavry@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/10/20 15:45:20 by nsavry            #+#    #+#              #
#    Updated: 2015/10/23 16:11:16 by nsavry           ###   ########.fr        #
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

	def display_color(self, color):
		i = " "
		j = " "
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

		
