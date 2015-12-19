import math

def main():
	before = 0
	after = int(input("Input a number: "))
	while before != after:
		before = after
		after = math.cos(after)
	print(str(after) + " is the dottie number.")

	before = 0
	after = 2
	while before!=after:
		before = after
		after = after - math.tan(after)

	print(str(after) + " is the result of recursing x - tan(x).")
	before = 0
	after = int(input("Pick a starting number: "))
	while before != after:
		before = after
		after = 1 + 1/after
	print (str(after) + " is the result of recursing 1+1/x.")



main()