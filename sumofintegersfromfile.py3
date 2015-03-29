import sys

x = 0
with open(sys.argv[1], 'r') as lines:
	for line in lines:
		x+=int(line)
	print(x)