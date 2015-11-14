import math, string, time, random

# pass_gen(lengths_list) takes a list of integers called 
# lengths_list to produce a list of 
# strings with randomly generated passwords of length lengths_list.
def pass_gen(lengths_list):
	pass_list = []
	x = 0
	for i in lengths_list:
		current_pass = []
		for d in range(0, lengths_list[x]):
			current_pass.append(chr(random.randint(97, 122)))
		str1 = "".join(current_pass)
		pass_list.append(str1)
		x += 1

	return pass_list




# main() asks the user for the lengths of each password as a list.
# This list is given to pass_gen(lengths_list) in order to create the list
# of passwords.
def main():
	while True:
		print("Enter the length of your desired passwords, with spaces indicating a new password.")
		lengths = input("What length would you like for your passwords?")
		lengths_list = [int(a) for a in lengths.split()]

		print(pass_gen(lengths_list))

		if (input("Would you like to make another set of passwords?") == "y"):
			pass
		else:
			break


main()