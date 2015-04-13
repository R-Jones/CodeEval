import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		nums = line.strip('\n').split(';')[1].split(',')
		for num in nums:
			if(nums.count(num) > 1):
				print(num)
				break
