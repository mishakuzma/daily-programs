"""Election winner checker. Consumes a set of percentages and produces the
winner by determining the person who holds the majority."""

def main():
	inListName = []
	inListPercent = []
	while True:
		i = str(input("Type: Name, percent(already *100 please) OR\
 0 to calculate."))
		if i == "0":
			break
		inListName.append(i.split(", ")[0])
		inListPercent.append(float(i.split(", ")[1]))

	totalPercent = 0
	for i in inListPercent:
		totalPercent += i

	if totalPercent > 100:
		raise ValueError("Total percent exceeds 100 percent")
	elif totalPercent < 100:
		raise ValueError("Total percent is less than 100 percent")

	tie = 1
	for i in inListPercent:
		if i > 50:
			print("Winner: " + inListName[inListPercent.index(i)] + \
	" with " + str(i) + " percent of the vote.")
			break
		elif i == 50 and len(inListPercent) == 2:
			print("Two Winners (tie @ 50%):")
			print("Winner 1: " + inListName[0])
			print("Winner 2: " + inListName[1])
			break
		elif i == 50:
			print("Winner: " + inListName[inListPercent.index(i)] + \
	" with " + str(i) + " percent of the vote.")
		elif inListPercent.index(i) + 1 == len(inListPercent):
			print("No winner")
		else:
			pass

main()