# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Rubik.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nsavry <nsavry@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2015/10/20 14:44:29 by nsavry            #+#    #+#              #
#    Updated: 2015/10/23 16:12:36 by nsavry           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import Cube

test = Cube.Cube()
test.init()
#try:
#	args = sys.argv[1].upper().split(" ")
#except:
#	print "ERROR: Sequence required"
#	quit()
#for av in args:
#	try:
#		test.tab[av]()
#	except:
#		print "ERROR: Wrong Move: '" + av + "'"
#		quit()
#print ""
test.display()
