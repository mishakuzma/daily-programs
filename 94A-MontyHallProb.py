""" Monty hall problem simulator
Consumes an integer and returns the probability of staying with one door
or switching doors returning the prize.
Created by Misha Kuzma on Dec 13, 2015"""

import random

class Doors:
	def __init__(self, attempts):
		self.attempts = attempts

	def setUp(self):
		dictMain = {
			1 : 0,
			2 : 0,
			3 : 0
		}

		listofNum = [1, 2, 3]

		dictMain[random.randint(1, 3)] = 1

		selection = random.randint(1, 3)
		removeSel = random.randint(1, 3)

		while removeSel == selection or dictMain[removeSel] == 1:
			removeSel = random.randint(1, 3)

		listofNum.remove(removeSel)
		listofNum.remove(selection)
		switchSel = listofNum[0]

		return(dictMain[selection], dictMain[switchSel])

	def tally(self):
		stayTot = 0
		switchTot = 0
		for x in range(0, self.attempts):
			stay, switch = self.setUp()
			stayTot += stay
			switchTot += switch
		return(stayTot, switchTot)

	def outResult(self):
		stayNom, switchNom = self.tally()
		stayChance = (stayNom / self.attempts) * 100
		switchChance = (switchNom / self.attempts) * 100
		print("Monty Hall Problem:")
		print("Attempts: " + str(self.attempts))
		print("Chance of winning by staying: " + \
			str(stayChance))
		print("Chance of winning by switching: " + \
			str(switchChance))

def main():
	attempts = int(input("How many times do you want the problem to recurse? "))
	problem = Doors(attempts)
	problem.outResult()

main()
