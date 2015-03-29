import sys, functools

fibo = []
fibo.append(0)
fibo.append(1)

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		n = int(line)
		while len(fibo) < n + 1:
			fibo.append(fibo[-1] + fibo[-2])
		print(fibo[n])
