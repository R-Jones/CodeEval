import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		stripped = line.strip('\n')
		l = len(stripped)
		answer = l
		for x in range(1,l):
			if(l % x == 0 and stripped[:x] * int(l / x) == stripped):
				answer = x
				break

		print(answer)