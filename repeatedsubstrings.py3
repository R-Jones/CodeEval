import sys, functools

bestString = ''
repetitions = 0

def testCandidate(line, startingFrom, length):
	global bestString, repetitions
	candidate = line[startingFrom - length:startingFrom]
	if(len(candidate.strip(' ')) == 0):
		return
	reps = 0
	while(startingFrom + length <= len(line) and candidate == line[startingFrom:startingFrom + length]):
		reps += 1
		startingFrom += length

	if(reps > 0):#1 rep equals 1 repetition
			if(len(candidate) * reps > len(bestString) * repetitions):
				bestString = candidate
				repetitions = reps

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.strip('\n')
		bestString = ''
		repetitions = 0
		for x in range(1,len(line)):
			for length in range(1, min(x, len(line) - x) + 1):
				testCandidate(line, x, length)

		#still need to prune down to smallest repeating substring


		print(bestString if len(bestString) > 0 else "NONE")