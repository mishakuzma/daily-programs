import time

def leapYear(year):
	leapYear = False

	if year % 400 == 0:
		leapYear = True
	elif year % 100 == 0:
		leapYear = False
	elif year % 4 == 0:
		leapYear = True
	return leapYear


def main():
	monthList = ["jan", "feb", "mar", "apr", "may", \
	"jun", "jul", "aug", "sep", "oct", "nov", "dec"]

	month_dayList = {
	"jan": 31,
	"feb": 28,
	"mar": 31,
	"apr": 30,
	"may": 31,
	"jun": 30,
	"jul": 31,
	"aug": 31,
	"sep": 30,
	"oct": 31,
	"nov": 30,
	"dec": 31
	}

	wantDate = input("What is the desired date? \n \
		Use this format: DD MMM YYYY ... :")

	listOfWantDate = wantDate.split(" ")

	day = int(listOfWantDate[0])
	month = listOfWantDate[1].lower()
	year = int(listOfWantDate[2])

	if leapYear(year) == True:
		month_dayList["feb"] = 29
	
	nity = 0

	for i in monthList:
		if i == month:
			break
		else:
			nity += month_dayList[i]

	nity += day

	print(nity)

main()