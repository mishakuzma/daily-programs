"""Standard deviation calculator - takes a series of numerical inputs
and returns the standard deviation of the values"""

class StandardDeviation:
	def __init__(self, inList):
		self.inList = inList

	def standardDev(self):
		totalSum = 0
		valueNum = 0
		for i in self.inList:
			valueNum += 1
			totalSum += i
		averageInList = totalSum / valueNum
		totalDiff = 0
		for i in self.inList:
			totalDiff += (i - averageInList) ** 2
		variance = totalDiff / valueNum
		standDev = variance ** (1/2)
		print("Number of values:", str(valueNum))
		print("Average:", str(averageInList))
		print("Variance:", str(variance))
		print("Standard Deviation:", str(standDev))

def main():
	inList = []
	while True:
		try:
			inAtt = int(input("Which value do you want to add to a\
 list to calculate standard deviation? ('None number values to exit'):"\
))
			inList.append(inAtt)
		except ValueError:
			break
	stanDevMain = StandardDeviation(inList)
	stanDevMain.standardDev()

main()