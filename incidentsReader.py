# File reader for incidents dataset

import sys

class Incident:
	def __init__(self, cat, month, day, hour):
		self.cat = cat
		self.month = month
		self.day = day
		self.hour = hour
	def getCat(self): # variable size string
		return self.cat;
	def getMonth(self): # 3 char string
		return self.month
	def getDay(self): # int
		return self.day
	def getHour(self): # int (24h clock)
		return self.hour

def loadData(fileName):
	file = open(fileName, 'r')
	rawText = file.read().split('\n')
	incidents = []
	month = ''
	day = 0
	hour = 0
	timeSlot = -1
	
	for line in rawText:
		splitLine = line.split(',')
		newIncident = Incident(splitLine[0],splitLine[1],splitLine[2],splitLine[3])
		if splitLine[1]==month and splitLine[2]==day and splitLine[3]==hour:
			incidents[timeSlot].append(newIncident)
		else:
			month = splitLine[1]
			day = splitLine[2]
			hour = splitLine[3]
			incidents.append([newIncident])
			timeSlot += 1
	file.close()
	return incidents

def printData(fileName):
	testIncidents = loadData(fileName)
	for i in range(0,len(testIncidents)):
		print(i)
		for j in range(0,len(testIncidents[i])):
			print(testIncidents[i][j].getCat(), ',')
			print(testIncidents[i][j].getMonth(), ',')
			print(testIncidents[i][j].getDay(), ',')
			print(testIncidents[i][j].getHour(), '\n')
	input() #wait for user
	
printData(sys.argv[1])