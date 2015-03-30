import sys, functools
with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		split = line.split()
		location = sum(map(int,split[1:])) / float(split[0])
		
		if(int((location * 10) % 10) >= 5):
			location = int(location) + 1
		else:
			location = int(location)

		print(functools.reduce(lambda x,y:x + abs(y - location), map(int,split[1:]),0))
