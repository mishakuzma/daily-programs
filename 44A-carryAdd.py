""" Carry adder - accepts a series of inputs (int or float) and 
returns the sum of the inputs, as well as the amount of carrying that
had to occur for that particular adding. (carrying is when the sum of
two digits is greater than 10, so one is added to the digit to the left)
For instance: 23 + 9 + 66 = 98, with a carry of ten (since the ones
digits had a total of 18, so the 10 of the 18 is carried onto the tens)"""

class CarryAdd:
	def __init__(self, listOfNum):
		self.listOfNum = listOfNum

	def carryAdd(self):
		#define variables that will be altered
		newList = []
		carryValue = 0
		#turn all elements of input into strings
		stringList = [str(i) for i in self.listOfNum]

		#represent each digit of input as multiples of 10
		for i in stringList:
			for t in range(0, len(i)):
				newList.append(int(i[t] + (str(0) * \
					(len(i) - 1 - t))))

		looperValue = 1
		while True:
			addList = []
			for t in range(0, len(newList)):
				if len(str(newList[t])) == looperValue:
					addList.append(newList[t])
			if addList != []:
				total = 0
				for i in addList:
					total += int(i)
				if len(str(total)) > looperValue:
					carryValue += int(str(total)[0] \
						+ (str(0) * looperValue))
				looperValue += 1
			else:
				break
		return carryValue

	def printCarry(self):
		total = 0
		for a in self.listOfNum:
			print(a)
			total += a
		print("___________")
		print(total)
		print("___________")
		print(self.carryAdd())

#enter an input to use the program
def main():
	testIn = CarryAdd([int(x) for x in 
	str(input("Enter numbers seperated by spaces: ")).split(" ")])
	testIn.printCarry()
main()

