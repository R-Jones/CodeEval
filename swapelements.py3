import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.strip('\n').split(' : ')
		#print(split)
		elements = split[0].split()
		swaps = split[1].split(', ')
		for swap in swaps:
			a = int(swap.split('-')[0])
			b = int(swap.split('-')[1])
			elements[a], elements[b] = elements[b], elements[a]
		print(' '.join(elements))