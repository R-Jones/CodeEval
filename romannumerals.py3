import sys

ones = "IXCM"
fives = "VLD"

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		retVal = []
		for x in range(0 , len(line.strip('\n'))):
			num = int(line.strip('\n')[-x - 1])
			if (0 < num < 4):
				retVal += ones[x] * num
			elif (num == 4):
				retVal += fives[x] + ones[x]
			elif (4 < num < 9):
				retVal += (ones[x] * (num - 5)) + fives[x] 
			elif(num == 9):
				retVal += ones[x:x + 2][::-1]
			#print(num)
			#print(x)
			#print(retVal)
		print(''.join(retVal[::-1]))