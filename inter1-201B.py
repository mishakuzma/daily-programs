import math, time

# main() asks a user to input a number. The number will be squared
# and the digits of the squared number will be summed. If the 
# sum of the squared numbers is the original number, true is 
# returned and false is returned otherwise.
def main():
	orig_num = int(input("Please input a number to test if it is \
a kaprekar number: "))
	sqr_num = str(orig_num ** 2)
	sum_num = 0

	for i in sqr_num:
		sum_num += int(i)

	if sum_num == orig_num:
		print(str(orig_num), "is a kaprekar number.")
	else:
		print(str(orig_num), "is NOT a kaprekar number.")

main()