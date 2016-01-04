""" letters in alphabetical order - takes in a string and returns a 
string that tells if the input has it's letters in alphabetical
order. Ex: Almost = true, Cereal = false """

class AlphaString:
	def __init__(self, inString):
		self.inString = inString

	def checkOrder(self):
		for i in range(0, len(self.inString)):
			if i == 0:
				pass
			elif i == (len(self.inString)-1) and ord(self.inString[i]) \
				>= ord(self.inString[i-1]):
				return True
			elif ord(self.inString[i]) < ord(self.inString[i-1]):
				return False
			else:
				pass

	def checkReverseOrder(self):
		for i in range(0, len(self.inString)):
			if i == 0:
				pass
			elif i == len(self.inString)-1 and ord(self.inString[i]) \
				<= ord(self.inString[i-1]):
				return True
			elif ord(self.inString[i]) > ord(self.inString[i-1]):
				return False
			else:
				pass

def main():
	inTest = AlphaString(str(input("Enter a string: ")))
	print(inTest.checkOrder())
	print(inTest.checkReverseOrder())
main()