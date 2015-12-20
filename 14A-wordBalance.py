class WordBalance:

# wordValue is a dictionary that associates all the capital letters
# of the alphabet with an increasing value (A = 1,... Z = 26)
	wordValue = {
		"A" : 1,
		"B" : 2,
		"C" : 3,
		"D" : 4,
		"E" : 5,
		"F" : 6,
		"G" : 7,
		"H" : 8,
		"I" : 9,
		"J" : 10,
		"K" : 11,
		"L" : 12,
		"M" : 13,
		"N" : 14,
		"O" : 15,
		"P" : 16,
		"Q" : 17,
		"R" : 18,
		"S" : 19,
		"T" : 20,
		"U" : 21,
		"V" : 22,
		"W" : 23,
		"X" : 24,
		"Y" : 25,
		"Z" : 26
	}

	def __init__(self, firstW):
		self.firstW = firstW

# sideWeight(wordIn, direction) consumes a string called wordIn and a
# string called direction and produces the weight of that particular
# direction and that string. If a direction is left, then the left-
# most characters get a higher multiplier to their value. The reverse
# relationship exists for a direction of right.
	def sideWeight(self, wordIn, direction):
		if direction == "right":
			multiplier = 1
			total = 0
			for i in wordIn:
				valueOfWord = multiplier * self.wordValue[i]
				total += valueOfWord
				multiplier += 1
			return total
		elif direction == "left":
			multiplier = len(wordIn)
			total = 0
			for i in wordIn:
				valueOfWord = multiplier * self.wordValue[i]
				total += valueOfWord
				multiplier -= 1
			return total


# balance(self) takes the input firstW of this class, and returns that 
# word in its balanced form (if possible)
	def balance(self):
		rightWeight = 0
		leftWeight = 0
		for i in range(0, len(self.firstW)):
			leftWord = self.firstW[0: i]
			rightWord = self.firstW[i + 1: len(self.firstW)]
			balanceWord = self.firstW[i]
			leftWeight = self.sideWeight(leftWord, "left")
			rightWeight = self.sideWeight(rightWord, "right")

			if leftWeight == rightWeight:
				print(leftWord, balanceWord, rightWord, " - " +\
				 str(leftWeight))
				break
			elif i == len(self.firstW) - 1:
				print(self.firstW, "does not balance.")
		
def main():
	wordIn = WordBalance(str(input("What word do you want \
to balance (caps only): ")))
	wordIn.balance()

main()
