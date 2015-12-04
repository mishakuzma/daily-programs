# Pythagorean triple finder
# Accepts a number that the sum of A,B,C must equal and tells user
# the combinations of A,B,C that have that sum.
# For instance, if 240 is input, then (15,112,113),(40,96,104), 
# (48,90,102), and (60, 80, 100) are returned.
# Started on December 4, 2015 by Misha Kuzma
import math, os

os.chdir("C:\selfPrograms\dailyProg\outFiles")
s = open("Pythagorean Triples.txt", "w")
# potentialSet(sumAll) consumes a positive integer and returns a list
# containing lists of three numbers that sum to sumAll.
# potentialSet: Int -> (listof (listof Num Num Num))
# requires:     sumAll is a positive integer
def potentialSet(sumAll):
	setPotentials = []

	for start in range(1, sumAll+1):
		for mid in range(1, sumAll+1):
			for end in range(1, sumAll+1):
				if (start+mid+end) == sumAll:
					setPotentials.append([start,mid,end])
				elif (start+mid+end) > sumAll:
					break

	return setPotentials

# pyth_trip_find(setPotentials) consumes a list of lists of three
# integerscalled setPotentials and returns a list of lists of three 
# numbers where each element of the list is a tuple where the three 
# numbers are pythagorean triples and are integers.
# pyth_trip_find: (listof (listof Num Num Num))
def pyth_trip_find(setPotentials):
	pythagTripList = []

	for listElement in setPotentials:
		if ((listElement[0] ** 2) + (listElement[1] ** 2)) == (listElement[2] ** 2):
			pythagTripList.append(listElement)
			s.write(str(listElement) + "\n")
		else:
			pass

	return pythagTripList


# main() asks user for an integer input and gives that input to another
# function in order to find a set of pythagorean triples.
def main():
	sumAll = int(input("What should the sums of the non-squared \
A, B, and C be? Make sure a positive integer is inputted. :"))
	s.write("Sum of A B C:" + str(sumAll) + "\n")
	print(pyth_trip_find(potentialSet(sumAll)))
	s.close()

main()