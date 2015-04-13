import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		if(len(line.strip('\n')) < 56):
			print(line.strip('\n'))
		else:
			lastspace = line[0:40].rfind(' ')
			print((line[0:lastspace] if lastspace != -1 else line[0:40]) + '... <Read More>')
			#print(line[0:41].strip() + '... <Read More>')