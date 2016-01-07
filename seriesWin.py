""" Program will produce the chance that a team will win an x-game series
given x and the chance that the team will win. """

def main():
	inSeries = int(input("How many games are in the series? "))
	inChance = float(input("What is the chance of the team winning? "))
	otherChance = 1 - inChance
	teamDict = {
		"l" : inChance,
		"c" : otherChance
	}
	startList = ["l", "c"]
	endList = []

	for game in range(0, inSeries + 1):
		for possibility in startList:
			if game != inSeries:
				if possibility.count("l") >= inSeries / 2:
					startList.remove(possibility)
				elif possibility.count("c") >= inSeries / 2:
					endList.append(possibility)
					startList.remove(possibility)
				else:
					startList.append(possibility + "c")
					startList.append(possibility + "l")
					startList.remove(possibility)
			else:
				if possibility.count("c") >= inSeries / 2:
					endList.append(possibility)

	print(endList)

	chanceOfWin = 0
	for match in endList:
		chanceOfWin += ((otherChance ** (match.count("l")))\
			* (inChance ** (match.count("c"))))
	print(chanceOfWin * 100)

main()
			
