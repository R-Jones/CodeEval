import functools

for x in range(1,13):
	print(functools.reduce(lambda a,b:a + str(b).rjust(4),range(2*x,12*x + 1,x), str(x)))
		