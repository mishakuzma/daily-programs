
def main():
	num_Letter = {
		"a" : "2",
		"A" : "2",
		"b" : "2",
		"B" : "2",
		"c" : "2",
		"C" : "2",
		"d" : "3",
		"D" : "3",
		"e" : "3",
		"E" : "3",
		"f" : "3",
		"F" : "3",
		"g" : "4",
		"G" : "4",
		"h" : "4",
		"H" : "4",
		"i" : "4",
		"I" : "4",
		"j" : "5",
		"J" : "5",
		"k" : "5",
		"K" : "5",
		"l" : "5",
		"L" : "5",
		"m" : "6",
		"M" : "6",
		"n" : "6",
		"N" : "6",
		"o" : "6",
		"O" : "6",
		"p" : "7",
		"P" : "7",
		"q" : "7",
		"Q" : "7",
		"r" : "7",
		"R" : "7",
		"s" : "7",
		"S" : "7",
		"t" : "8",
		"T" : "8",
		"u" : "8",
		"U" : "8",
		"v" : "8",
		"V" : "8",
		"w" : "9",
		"W" : "9",
		"x" : "9",
		"X" : "9",
		"y" : "9",
		"Y" : "9",
		"z" : "9",
		"Z" : "9"
	}
	newString= ""
	inP = str(input("Enter a telephone number with letters (make\
 sure the telephone number is valid with hyphens and is a 1-800 number: "))
	for i in inP:
		if i == "-" or inP.index(i) == 1 or \
		inP.index(i) == 5:
			newString += "-"
		else:
			try:
				if int(i) in range(0, 10):
					newString += i
			except ValueError:
					newString += num_Letter[i]
	print(newString)

main()
