""" b-sad cycle determiner - takes in a base b and a starting number
n and produces a list of numbers that represent the b-sad cycle of
the sequence."""

class SadCycle:
	def __init__(self, base, startNum):
		self.base = base
		self.startNum = startNum

	def sadCycleCalc(self):
		repeatList = []
		inList = [int(i) for i in str(self.startNum)]
		while True:
			totalList = 0
			for t in inList:
				totalList += t ** (self.base)
			if totalList in repeatList:
				break
			else:
				repeatList.append(totalList)
				inList = [int(i) for i in str(totalList)]
		return repeatList[repeatList.index(totalList):]

def main():
	inMain = SadCycle(int(input("Input a base: ")), \
		int(input("Input a start number: ")))
	print(inMain.sadCycleCalc(), "is the", str(inMain.base) +\
		"-sad cycle with start number", str(inMain.startNum)+".")

main()
		
