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
		test.move(test.move_tab[av])
	except:
		print "ERROR: Wrong Move: '" + av + "'"
		quit()
print ""
test.display()
if test.second_ring() == True:
	print "true"
else:
	print "false"
