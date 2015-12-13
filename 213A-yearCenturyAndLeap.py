class CenturyYear:
 	def __init__(self, year):
 		self.year = year

 	"""leapY() takes in a year and returns a boolean depending on whether
 a year is a leap year or not"""
 	def leapY(self):
 		if self.year % 4 != 0:
 			return("No")
 		elif self.year % 100 != 0:
 			return("Yes")
 		elif self.year % 400 != 0:
 			return("No")
 		else:
 			return("Yes")

 	""" century() takes in a year and reports what century that year
 belongs to."""
 	def century(self):
 		i = 1
 		while self.year/i > 100:
 			i += 1
 		return(str(i))

def main():
	inP = CenturyYear(int(input("Enter year: ")))
	print("Century: " + inP.century())
	print("Leap Year: " + inP.leapY())

main()
