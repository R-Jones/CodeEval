import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split();
		counter = 0
		crossover = 0
		for char in split[1]:
			if char in ('+', '-'):
				operation = char
				crossover = counter
			else:
				counter+=1
		
		firstNumber = split[0][:crossover]
		secondNumber = split[0][crossover:]
		if operation == '+':
			print(int(firstNumber) + int(secondNumber))
		else:
			print(int(firstNumber) - int(secondNumber))