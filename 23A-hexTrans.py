""" silicon valley hex translator - takes in a hexadecimal value and
returns a string that represents how that value would be pronounced
using Bachman's pronounciation key from the HBO show 'Silicon Valley'"""

spec_hex = {
	"A" : "atta",
	"B" : "bibbity",
	"C" : "city",
	"D" : "dickety",
	"E" : "ebbity",
	"F" : "fleventy",

	"1" : "one",
	"2" : "two",
	"3" : "three",
	"4" : "four",
	"5" : "five",
	"6" : "six",
	"7" : "seven",
	"8" : "eight",
	"9" : "nine",
	"0" : ""	
}

hex_str = {
	"A" : "ayy",
	"B" : "bee",
	"C" : "cee",
	"D" : "dee",
	"E" : "eey",
	"F" : "eef",

	"1" : "one",
	"2" : "two",
	"3" : "three",
	"4" : "four",
	"5" : "five",
	"6" : "six",
	"7" : "seven",
	"8" : "eight",
	"9" : "nine",
	"0" : ""
}

def main():
	processPart = str(input("What hex value do you want pronounced? 0x"))
	pronounce = ""

	for i in range(0, len(processPart)):
		if i == 2:
			pronounce += " bitey "
		if (i+1)%2 != 0:
			pronounce += spec_hex[processPart[i]] + "-"
		else:
			pronounce += hex_str[processPart[i]] + " "
	print(pronounce)

main()