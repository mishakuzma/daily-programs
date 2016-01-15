# Program takes in a file as input and produces both the 
# number of lines and number of words in the document.
import os

class Word:
	def __init__(self, fileX):
		self.fileX = fileX

	def countLines(self):
		countLine = 0
		while True:
			if self.fileX.readline() != "":
				countLine += 1
			else:
				break
		return countLine

	def countWords(self):
		total = 0
		while True:
			testLine = self.fileX.readline()
			if testLine == "":
				break
			else:
				wordList = str(testLine).split(" ")
				total += len(wordList)
		return total

	def countLettersSanSpace(self):
		total = 0
		for i in self.fileX.read().split(" "):
			for t in i:
				total += 1
		return total
	def countLettersAndSpaces(self):
		return len(self.fileX.read())



def main():
	inFile = open(input("What is the file in its path?:"), "r")
	inClass = Word(inFile)
	print("Lines: ", inClass.countLines())
	print("Words: ", inClass.countWords())
	print("Letters (no space):", inClass.countLettersSanSpace())
	print("Letters: ", inClass.countLettersAndSpaces())
	inFile.close()

main()