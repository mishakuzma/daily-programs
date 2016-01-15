""" Program takes in a day, month, and year as input and returns the day
of the week. 
Created by Mykhaylo Kuzma on January 8, 2016"""

class DayConvert:
	'Takes in (year,month,day) in numbers and outputs day of week'
	# This relies on the Doomsday rule
	#(https://en.wikipedia.org/wiki/Doomsday_rule), which defines
	# weekdays as such:
	# Sun = 0, Mon = 1,..., Sat = 6
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def leapYear(self):
		if int(self.year) % 4 != 0:
			return False
		elif int(self.year) % 100 != 0:
			return True
		elif int(self.year) % 400 != 0:
			return False
		else:
			return True
			
	#determine what is the anchor day for the century
	def anchorDay(self):
		import math
		century = int(\
			str(self.year)[0: int(len(str(self.year))//2)])
		return(century)

	def calcDooms(self):
		numberOf12s = int(str(self.year)[-2:len(str(self.year))])%12
		diffOfYears = max(int(str(self.year)[-2:len(str(self.year))]),\
			numberOf12s) - \
			min(int(str(self.year)[-2:len(str(self.year))]),\
			numberOf12s)
		numberOf4s = diffOfYears % 4
		doomsdayOfyear = numberOf12s + numberOf4s + diffOfYears\
			+ self.anchorDay()
		doomsDayWeek = doomsdayOfyear - (7 * (doomsdayOfyear // 7))
		print("doomsdayOfYear = ", str(doomsdayOfyear))
		print("doomsdayweek = ", str(doomsDayWeek))
		return doomsDayWeek

	def calcWeekday(self):
		#The doomsdays of every month
		if self.leapYear() == False:
			doomsdayInMonth = {
				"01" : 3,
				"02" : 28,
				"03" : 7,
				"04" : 4,
				"05" : 9,
				"06" : 6,
				"07" : 11,
				"08" : 8,
				"09" : 5,
				"10" : 10,
				"11" : 7,
				"12" : 12
			}
		else:	
			doomsdayInMonth = {
				"01" : 4,
				"02" : 29 ,
				"03" : 7,
				"04" : 4,
				"05" : 9,
				"06" : 6,
				"07" : 11,
				"08" : 8,
				"09" : 5,
				"10" : 10,
				"11" : 7,
				"12" : 12
			}



		currentDay = 0
		if int(self.day) > doomsdayInMonth[str(self.month)]:
			if int(self.day) - doomsdayInMonth[str(self.month)] > 7:
				currentDay = self.day - \
				(7 * ((self.day - \
					doomsdayInMonth[str(self.month)]) % 7))
			dayOfWeek = self.calcDooms() - currentDay
			if dayOfWeek < 0:
				dayOfWeek += 7
		else:
			if doomsdayInMonth[str(self.month)] - int(self.day) > 7:
				currentDay = self.day + \
				(7 * ((doomsdayInMonth[str(self.month)] \
					- int(self.day)) % 7))
			dayOfWeek = self.calcDooms() + currentDay
			if dayOfWeek > 6:
				dayOfWeek -= 7

		return dayOfWeek

	def printDayOfWeek(self):
		weekDict = {
			0 : "Sunday",
			1 : "Monday",
			2 : "Tuesday",
			3 : "Wednesday",
			4 : "Thursday",
			5 : "Friday",
			6 : "Saturday"
		}

		print(weekDict[int(self.calcWeekday())])


def main():
	inDay = input("What is the year,month,day? ").split(",")
	inDayClass = DayConvert(str(inDay[0]), str(inDay[1]), str(inDay[2]))
	inDayClass.printDayOfWeek()

main()