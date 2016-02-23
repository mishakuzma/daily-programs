# input is string of format "NdM" where N is the number of times that a 
# M sided dice is rolled and returns a list of numbers that correspond
# to the sides that are produced by rolling the M sided dice N times.

import random

class RollDice:
	def __init__(self, times, sides):
		self.times = times
		self.sides = sides

	def rollMDiceNTimes(self):
		testList = []
		for i in range(0, self.times):
			testList.append(random.randint(1, self.sides))
		return testList

def main():
	firstIn = str(input("What is the dice format? (NdM) (replace capitals)"))
	processIn = firstIn.split("d")
	inClass = RollDice(int(processIn[0]), int(processIn[1]))
	print(inClass.rollMDiceNTimes())

main()