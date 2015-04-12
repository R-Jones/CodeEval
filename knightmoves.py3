import sys, itertools

letters = "abcdefgh"

matrix = itertools.product({-1,1},{-1,1},{1,2})

with open(sys.argv[1], 'r') as test_cases:

	for line in test_cases:
		matrix = itertools.product({-1,1},{-1,1},{1,2})
		solutions = []
		for i, j, k in matrix:

			xoffset = (i * k)
			x = letters.find(line[0]) + xoffset

			yoffset = (j * (2 if k == 1 else 1))
			y = int(line[1]) + yoffset

			if(x in range(0,8) and y in range(1,9)):
				solutions.append(letters[x] + str(y))

		print(" ".join(sorted(solutions)))