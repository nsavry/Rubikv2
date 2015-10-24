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
if test.yellow_cross() == True:
	print "true"
else:
	print "false"
