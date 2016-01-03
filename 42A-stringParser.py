""" String parser - takes in a string literal and returns the parsed
version of the string OR the type of error that occurs with the string"""

class Parser:
	def __init__(self, inString):
		self.inString = inString

	def printString(self):
		return(self.inString[1:len(self.inString)-1])
	def parse(self):
		backTest = False
		for i in range(0, len(self.inString)):
			if backTest == True:
				backTest = False
				pass
			elif i == 0 and self.inString[i] != "\"":
				print("String is not initiated properly")
				raise ValueError
			elif i == len(self.inString)-1 and self.inString[i] =="\"":
				return(self.printString())
				break
			elif i == len(self.inString)-1 and self.inString[i] !="\"":
				return("String does not end.")
			elif self.inString[i] == "\\":
				backTest = True
				pass
			else:
				pass



def main():
	inTest = Parser(str(input("Input string (Include end quotes): ")))
	print(inTest.parse())

main()