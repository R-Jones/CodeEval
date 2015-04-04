import sys, functools

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		num = int(line.strip('\n'))
		while(True):
			if(num < 11):
				print(1 if num in {10, 1, 7} else 0)
				break
			num = functools.reduce(lambda x,y:x + int(y),str(num),0)