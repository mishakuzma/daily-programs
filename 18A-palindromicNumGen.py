""" Palindromic number generator - takes any single integer and
creates a number that is palindromic from the original number.
This is done by reversing the digits and adding the two numbers: the
original and the reversed digit number. If this sum is not palindromic,
this process is repeated."""

class PalindromicNum:
	def __init__(self, number):
		self.number = number

	def palindromize(self):
		testNum = self.number
		steps = 0
		while True:
			front = str(testNum)[0:]
			back = str(testNum)[::-1]
			if front == back:
				break
			else:
				steps += 1
				testNum = int(front) + int(back)
		return steps, testNum

	def printPalindrome(self):
		print(str(self.palindromize()[0]), "steps are used to get",
			str(self.number), "into the palindromic number",
			str(self.palindromize()[1]))

def main():
	inWord = PalindromicNum(int(\
		input("What number do you want to palindromize? ")))
	inWord.printPalindrome()

main()
