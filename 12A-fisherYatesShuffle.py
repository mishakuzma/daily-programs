""" list shuffler - inputs a list of data and outputs a list with
the elements of the input arranged in a different order. The order 
is different with every run, as a Fisher-Yates shuffle is used.
https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle"""

import random

class fisherYatesShuffle:
	def __init__(self, listInput):
		self.listInput = listInput

	def shuffle(self):
		indexList = [i for i in range(0, len(self.listInput))]
		newList = []
		while True:
			try:
				newChoice = random.choice(indexList)
				newList.append(self.listInput[newChoice])
				indexList.remove(newChoice)
			except IndexError:
				break
		return newList

	def printShuffle(self):
		print("Original list:", self.listInput)
		print("New list:", self.shuffle())

def main():
	test = str(input("Input a list (seperate by space): ")).split(" ")
	tester = []
	for x in test:
		tester.append(int(x))
	testerAgain = fisherYatesShuffle(tester)
	testerAgain.printShuffle()
main()
