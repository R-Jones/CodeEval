import sys

board = 'ABCESFCSADEE'

visited = [False, False, False, False, False, False, False, False, False, False, False, False]

def visit(pos, string):
	if(len(string) < 2):
		return True

	visited[pos] = True

	#test above
	nextNode = pos - 4
	if(nextNode > -1 and not visited[nextNode] and board[nextNode] == string[1]):
		if(visit(nextNode, string[1:]) == True):
			visited[pos] = False
			return True
		
	#test right
	nextNode = pos + 1
	if(pos % 4 != 3 and nextNode < 12 and not visited[nextNode] and board[nextNode] == string[1]):
		if(visit(nextNode, string[1:]) == True):
			visited[pos] = False
			return True
		
	#test bottom
	nextNode = pos + 4
	if(nextNode < 12 and not visited[nextNode] and board[nextNode] == string[1]):
		if(visit(nextNode, string[1:]) == True):
			visited[pos] = False
			return True
		
	#test left
	nextNode = pos - 1
	if(pos % 4 != 0 and nextNode > -1 and not visited[nextNode] and board[nextNode] == string[1]):
		if(visit(nextNode, string[1:]) == True):
			visited[pos] = False
			return True
		
	visited[pos] = False
	return False



with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		string = line.strip('\n')
		found = False
		for x in range(0, 12):
			visited[x] = True
			if(board[x] == string[0] and visit(x, string)):
				found = True
				visited[x] = False
				break
			visited[x] = False
		print(found)