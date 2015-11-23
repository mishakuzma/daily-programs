import string, os

os.chdir("C:\selfPrograms\dailyProg\outFiles")
s = open("string_rev.txt", "w")

# rev(raw_in) consumes a string called raw_in to produce a text file
# that contains a string with raw_in reversed.
def rev(raw_in):
	start = raw_in[0]
	product = ""
	
	for i in range(1, len(raw_in)):
		product += raw_in[-i]

	product += start

	return product

# main() asks user for input in the form of a string, and prints that 
# string reversed in a text file called "string_rev.txt"
def main():
	raw_in = input("What string do you wish to be reversed? ")
	s.write(rev(raw_in))
	s.close()

main()