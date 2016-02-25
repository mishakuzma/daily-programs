# word unscrambler - will unscramble words that are in a file according
# to a wordlist 

def main():
	inScram = open(input("What is the address for the scrambled file?"))
	inWordList = open(input("What is the address of the word list?"))

	listScram = inScram.readline().split(" ")
	listWords = inWordList.readline().split(" ")
	preListDict = []
	for i in listWords:
		for t in i.split(":"):
			preListDict.append(t)

	
main()