import sys

morsecodes = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', 
'....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', 
'.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '-----':'0',
'.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', 'space':' '}

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:

		#print([[char for char in y.strip()] for y in line.strip('\n').split('  ')])
		#print(''.join([[morsecodes[char] for char in y.split()] for y in line.strip('\n').split('  ')]))


		#print([[morsecodes[char] for char in y.split()] for y in line.strip('\n').split('  ')])
		

		print(''.join([morsecodes[char] for char in line.strip('\n').replace('  ', ' space ').split()]))