import math

def about():
	print "Welcome to the basic derivative calculator v0.5."
	print "This program will calculate a derivate that uses these rules:"
	print "Product rule, quotient rule, constant"
	print "Stay tuned for more updates!"
	main()

def main():
	print "1: Derive this for me!"
	print "2: About this program!"
	print "3: Quit"
	menu(raw_input("Select an option: "))