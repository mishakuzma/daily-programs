import sys, time
from sympy import *

# derive() asks user for a function to derive and what to derive in
# terms of. The answer is given, then the menu is called.
def derive():
	tester = input("What is the right side of the expression (remember that it's interms of ): ")
	
	x = Symbol('x')
	print(diff(tester, x))
	time.sleep(10)
	main()


# menu(option) takes in a integer parameter called option and calls a 
# function based on option. If option is not a valid number, then 
# main() is recalled so that the user can select a new option.
def menu(option):
	if (option == "1"):
		derive()
	elif (option == "2"):
		about()
	elif (option == "3"):
		sys.exit()
	else:
		print("You need to enter an option from 1 - 3.")
		main()

# about() displays information to the user about the program, then 
# redirects them to the menu
def about():
	print("Welcome to the basic derivative calculator v0.5.")
	print("This program will calculate a derivate that uses these rules:")
	print("Product rule, quotient rule, constant")
	print("Stay tuned for more updates!")
	main()

def main():
	print("1: Derive this for me!")
	print("2: About this program!")
	print("3: Quit")
	option = input("Select an option: ")
	menu(option)

main()