""" String remover. Consumes two strings, and produces a string where 
letters from the second string are removed from the first string"""

def main():
	originalIn1 = str(input("What is your first string? "))
	originalIn2 = str(input("What is your second string? "))
	newString = ""

	for i in originalIn1:
		if i in originalIn2:
			pass
		else:
			newString += i
			
	print(newString)
main()