#Shamelessly stolen from Wikipedia
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_palindrome(x):
	strung = str(x)
	digits = len(strung)
	for y in xrange(0, digits):
		if y > digits / 2:
			return True
		if strung[y] != strung[-(y + 1)]:
			return False

for x in range(1000, 0, -1):
	if(is_prime(x) and is_palindrome(x)):
		print(x)
		break;