import sys


with open(sys.argv[1], 'r') as test_cases:

	for test in test_cases:
		
		lineOut = ""
		split = test.split()

		for x in range(1, int(split[-1])):

			if x % int(split[0]) == 0 and x % int(split[1]) == 0:
				lineOut += "FB"
			elif x % int(split[0]) == 0:
				lineOut += "F"
			elif x % int(split[1]) == 0:
				lineOut += "B"
			else:
				lineOut += str(x)

			if x < int(split[-1]) - 1:
				lineOut += " "

		print(lineOut)