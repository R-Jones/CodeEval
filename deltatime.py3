import sys, datetime

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:

		split = line.strip('\n').split()
		time1 = datetime.time(int(split[0][0:2]), int(split[0][3:5]), int(split[0][6:8]))
		time2 = datetime.time(int(split[1][0:2]), int(split[1][3:5]), int(split[1][6:8]))
		timedelta = datetime.timedelta(time1, time2)

		#print(':'.join([str(hour), str(minute), str(second)]))
		