import string, sys, math

# tooHigh(top, bottom) consumes 2 numbers called top and bottom
# in order to produce a single number which is produced by flooring
# the average of top and bottom
def guessAdjust(top, bottom):
	guess = math.floor((top + bottom) / 2)
	asker(guess, top, bottom)


# asker(guess, top, bottom) asks if the computer's guess is correct.
# If so, the program closes. If the user says too high, than top and
# bottom are fed into guessAdjust(guess, bottom) to get another response
# if user says too low, than top and bottom fed into guessAdjust(top, guess).
def asker(guess, top, bottom):
	print("My guess is: " + str(guess))
	opinion = raw_input("Is that correct?");
	while True:
		if (opinion == "right"):
			print("Yay, I win!")
			sys.exit()
		elif (opinion == "high"):
			print("Hmm, let me think.")
			guessAdjust(guess, bottom)

		elif (opinion == "low"):
			print("Okay, let me try again.")
			guessAdjust(top, guess)

		else:
			print("You didn't enter a correct statement.")

# start() prints instructions to the user on startup
def start():
	top = 100
	bottom = 1
	print("Welcome to guessr! Think of a number between 1 and 100")
	print("I'll print a number, and you tell me if it's high, low, or right!")
	asker(50, top, bottom)

start()