import sys

messages = {0:'This program is for humans', 2:'Still in Mama\'s arms', 4:'Preschool Maniac', 11:'Elementary school', 14:'Middle School', 18:'High School', 22:'College', 65:'Working for the man', 100:'The Golden Years', 4294967295:'This program is for humans'}

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		age = int(line)
		for key in sorted(messages.keys()):
			if age < key:
				print(messages[key])
				break