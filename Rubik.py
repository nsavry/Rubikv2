# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Rubik.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nsavry <nsavry@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/10/20 14:44:29 by nsavry            #+#    #+#              #
#    Updated: 2015/10/23 19:29:56 by nsavry           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import Cube

test = Cube.Cube()
test.init()
try:
	args = sys.argv[1].upper().split(" ")
except:
	print "ERROR: Sequence required"
	quit()
for av in args:
	try:
		print av
		print test.move_tab[av]
		test.move(test.move_tab[av])
	except:
		print "ERROR: Wrong Move: '" + av + "'"
		quit()
print ""
test.display()
