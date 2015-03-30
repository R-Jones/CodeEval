import sys

def majorElement(line):
	counter = [0]*100
	length = len(line.strip('\n').split(','))
	split = map(int,line.strip('\n').split(','))
	for x in split:
		counter[x]+=1
		if counter[x] > length / 2:
			return x
	return None


with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		print(majorElement(line))