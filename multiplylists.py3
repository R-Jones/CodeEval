import sys, functools

with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		split = line.strip('\n').split('|')
		list1 = split[0].split()
		list2 = split[1].split()
		#for x in range(0, len(list1)):
		print(functools.reduce(lambda x, y:x + " " + str(int(list1[y]) * int(list2[y])),range(0, len(list1)), "")[1:])