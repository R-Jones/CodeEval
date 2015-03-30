import sys, re
with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		lineOut = ""
		#for entry in line.split(';'):
		match = re.findall(r',([0-9]+?);', line)
		s = sorted(map(int,match))
		s[:0] = [0]
		for x in range(0, len(s) - 1):
			if(x != 0):
				lineOut+=","
			lineOut+=str(s[x + 1] - s[x])
		print(lineOut)