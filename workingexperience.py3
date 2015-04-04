import sys, datetime

months = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}

timeIntervals = []

def addJob(startDate, endDate):
	global timeIntervals
	for interval in timeIntervals:
		if(interval[0] < startDate and interval[1] > startDate):
			if(interval[1] < endDate):
				interval[1] = endDate
			return
		elif(interval[0] < endDate and interval[1] > endDate):
			if(interval[0] > startDate):
				interval[0] = startDate
			return
		else:#we didn't find it
			timeIntervals += {startDate, endDate}






with open(sys.argv[1],'r') as test_cases:
	for line in test_cases:
		for record in line.split(';'):
			split = record.strip().split('-')
			addJob(
				datetime.date(int(split[0][4:]), months[split[0][:3]], 1),
				datetime.date(int(split[1][4:]), months[split[1][:3]], 28)
				)
			#print(record.strip())
			print(timeIntervals)
