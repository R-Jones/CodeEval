import sys

#Stolen from Wikipedia
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

x = 1
primeCount = 0
primeSum = 0

while primeCount < 1000:
	if(is_prime(x)):
		primeSum += x
		primeCount += 1
	x += 1

print(primeSum)