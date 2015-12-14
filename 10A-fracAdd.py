"""fraction adder will consume a series of numbers to produce a 
rational number in simplest terms.
Created by Misha Kuzma on December 14, 2015"""

class Fraction:
	def __init__(self, numer, denomer):
		self.numer = numer
		self.denomer = denomer

def main():
	fracList = []
	firstInput = ""
	while firstInput != "0":
		firstInput=str(\
			input("Give an input like N/D (Use 0 to add them):"))
		splitInput = firstInput.split("/")
		if len(splitInput) == 1:
			fracList.append(Fraction(int(splitInput[0]), 1))
		else:
			fracList.append(Fraction(int(splitInput[0]), \
				int(splitInput[1])))

	baseFrac = Fraction(0, 1)
	for i in fracList:
		if baseFrac.denomer / i.denomer == 1:
			baseFrac = Fraction(baseFrac.numer + i.numer, \
				baseFrac.denomer)
		else:
			newDeno = baseFrac.denomer * i.denomer
			baseFrac = Fraction((baseFrac.numer*\
				(newDeno/baseFrac.denomer)) \
				+ (i.numer * (newDeno/i.denomer)), newDeno)

	for i in range((min(baseFrac.numer, baseFrac.denomer) + 1), 1,\
		-1):
		if baseFrac.numer % i == 0 and baseFrac.denomer % i == 0\
		and i != 1:
			baseFrac = Fraction(baseFrac.numer / i,\
			baseFrac.denomer / i)
		elif i == 1:
			break
		else:
			pass

	print(str(baseFrac.numer) + "/" + str(baseFrac.denomer))

main()
