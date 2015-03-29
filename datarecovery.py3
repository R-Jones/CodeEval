import sys

def descramble(sentenceSplit, numberSplit):
	splitOut = [None]*len(sentenceSplit)
	for x in range(0, len(numberSplit)):
		splitOut[int(numberSplit[x]) - 1] = sentenceSplit[x]
		#print(splitOut)

	splitOut[splitOut.index(None)] = sentenceSplit[-1]
	#print(splitOut)
	return " ".join(splitOut)


with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		split = line.split(';')
		sentenceSplit = split[0].split()
		numberSplit = split[1].split()

		print(descramble(sentenceSplit, numberSplit))