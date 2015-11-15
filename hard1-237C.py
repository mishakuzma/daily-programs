import time, sys, os

# Note: Figure out how to make directories for other users
os.chdir("C:\selfPrograms\dailyProg\outFiles")
f = open("stopwatch.txt", "w", 1)

# stop_watch() finds the number of elapsed seconds by subtracting 
# the number of seconds from when the timer started from the number
# of seconds when the timer finished. If the user wishes to lap,
# the first time is replaced by the second time, and the sequence is
# looped until the stopwatch is stopped.
def stop_watch():
	firstTime = time.time()
	n = 1
	sumTime = 0
	while True:
		while True:
			print("2: Stop stopwatch")
			print("3: Lap")
			choice = str(input("Enter your choice: "))
			if (choice == "2" or choice == "3"):
				break

		if (choice == "2"):
			secondTime = time.time()
			print("That was " + str(secondTime - firstTime) + " seconds. \n")
			sumTime += (secondTime - firstTime)
			print("Total time: " + str(sumTime) + " seconds.")
			f.write("Total time:" + str(sumTime) + " seconds.")
			break
		elif (choice == "3"):
			secondTime = time.time()
			print("That was " + str(secondTime - firstTime) + " seconds")
			f.write("Lap " + str(n) + ": " + str(secondTime - firstTime) + " seconds. \n")
			sumTime += (secondTime-firstTime)
			firstTime = secondTime
			n += 1

	f.close()


# main() will give the user the ability to start the stop watch or
# quit the program.
def main():
	print("1: Start stopwatch")
	print("Any: Quit")

	if (input("Enter your choice: ") == "1"):
		stop_watch()
	else:
		sys.exit()

main()