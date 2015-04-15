import sys, re, math

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		matches = re.findall('\(([\d-]+), ([\d-]+)\) \(([\d-]+), ([\d-]+)\)', line)[0]
		hyp = math.sqrt((int(matches[2]) - int(matches[0])) ** 2 + (int(matches[3]) - int(matches[1])) ** 2)
		print(int(hyp))