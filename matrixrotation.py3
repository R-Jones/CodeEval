import sys, math

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		lineOut = []
		letters = line.split();
		size = int(math.sqrt(len(letters)))
		for x in range(0, size):
			for y in range(1, size + 1):
				lineOut.append(letters[-(size * y) + x])
		print(" ".join(lineOut))