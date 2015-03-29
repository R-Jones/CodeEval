import sys, re
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		if(len(line) <= 2):
			continue
		items = line.strip('\n')[38:-3]
		labeledItems = re.findall(r'{\"id\": ([0-9]*?), \"label\": \"Label [0-9]*?\"}',items)
		print(sum(map(int, labeledItems)))