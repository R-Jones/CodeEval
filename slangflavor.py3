import sys, functools, re

endings = (', yeah!', ', this is crazy, I tell ya.', ', can U believe this?', ', eh?', ', aw yea.', ', yo.', '? No way!', '. Awesome!')
endingindex = 0
counter = 0

def concatAString(builtString, char):
	global counter, endingindex
	if char in ('.','?','!'):
		counter += 1
		if counter % 2 == 0:
			endingindex += 1
			return builtString + endings[(endingindex - 1) % len(endings)]
	return builtString + char

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		print(functools.reduce(concatAString,line.strip('\n'),""))