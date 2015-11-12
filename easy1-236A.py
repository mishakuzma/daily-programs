# Simple caesar cipher created for daily programmer entry 2/11/2012
# Start date: Nov. 11/ 2015 by Mykhaylo Kuzma
import string, sys, time


# encry() uses a caesar cipher to take each letter of a string
# and insert a letter that is one space forward on the alphabet. 
# z is replaced with a, and only lower-case is accepted.
def encry():
	querie = str(input("What do you wish to encrypt? :"))
	new_string = ""
	for i in querie:
		appender = str(chr(ord(i) + 1))
		new_string = new_string + appender
	print(new_string)
	time.sleep(10)
	main()


# decry() uses a caesar cipher to take each letter of a string
# and insert a letter that is one space back on the alphabet.
# a is replaced with z, and only lowercase is accepted.
def decry():
	querie = str(input("What do you wish to encrypt? :"))
	new_string = ""
	for i in querie:
		appender = str(chr(ord(i) - 1))
		new_string = new_string + appender
	print(new_string)
	time.sleep(10)
	main()

# main() presents user with the list of options, including encrypting,
# decrypting, and exiting. Error proofing is included in main()
def main():
	print("1: Encrypt this string: ")
	print("2: Decrypt this string: ")
	print("3: Quit")
	choice = int(input("Please select now: "))

	# Error proofing decides if choice is between 1 - 3 (and also a int)
	while True:
		if (choice in range(1, 4)):
			break
		else:
			print("You need to pick a number between 1 and 3.")
			choice = int(input("Please choose now: "))

	if (choice == 1):
		encry()
	elif (choice == 2):
		decry()
	else:
		sys.exit()



main()