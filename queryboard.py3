import sys

board = [[0 for x in range(0, 256)] for y in range(0, 256)]

def SetCol(col, value):
	for record in board:
		record[col] = value

def SetRow(row, value):
	board[row] = [value for x in range(0, 256)]

def QueryCol(col):
	print(sum(record[col] for record in board))

def QueryRow(row):
	print(sum(board[row]))

queries = {'SetCol':SetCol, 'SetRow':SetRow, 'QueryCol':QueryCol, 'QueryRow':QueryRow}

with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		spl = line.strip('\n').split()
		func = queries[spl[0]]
		if(func in (SetCol, SetRow)):
			func(int(spl[1]), int(spl[2]))
		else:
			func(int(spl[1]))
		#func(spl[1], spl[2])