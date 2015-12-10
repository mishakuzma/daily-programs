""" Morse to english translator (and vice versa)
Created by Misha Kuzma on December 10, 2015
Reddit Daily Programmer Challenge #7 """

class MorseTrans:
	"Class that defines several aspects of morse code, including\
 methods of translating between english and morse code."
 
#dictionary morseString defines what a morse signal converts to in\
#english, and dictionary stringMorse converts english into morse by \
#swapping the keys and values of morseString."""
	
	morseString = {
		".-.-.-" : ".",
		"--..--" : ",",
		"---..." : ":",
		"..--.." : "?",
		".----." : "\'",
		"-....-" : "-",
		"-..-." : "/",
		".-..-." : "\"",
		".--.-." : "@",
		"-...-" : "=",
		".-" : "A",
		"-..." : "B",
		"-.-." : "C",
		"-.." : "D",
		"." : "E",
		"..-." : "F",
		"--." : "G",
		"...." : "H",
		".." : "I",
		".---" : "J",
		"-.-" : "K",
		".-.." : "L",
		"--" : "M",
		"-." : "N",
		"---" : "O",
		".--." : "P",
		"--.-" : "Q",
		".-." : "R",
		"..." : "S",
		"-" : "T",
		"..-" : "U",
		"...-" : "V",
		".--" : "W",
		"-..-" : "X",
		"-.--" : "Y",
		"--.." : "Z",
		"-----" : "0",
		".----" : "1",
		"..---" : "2",
		"...--" : "3",
		"....-" : "4",
		"....." : "5",
		"-...." : "6",
		"--..." : "7",
		"---.." : "8",
		"----." : "9"
	}

	stringMorse = dict((value,key) for key, value in\
	 morseString.items())

	#define a class instance with the string 
	def __init__(self, trans):
		self.trans = trans

	#translate from morse to english
	def morse_Eng(self):
		listofNew = self.trans.split(" / ")
		newString = ""
		for i in listofNew:
			listofAlmostProd = i.split(" ")
			for t in listofAlmostProd:
				newString += self.morseString[t]
			if  listofNew.index(i) == len(listofNew):
				newString += "."
			else:
				newString += " "
		print(newString)

	#translate from english to morse
	def eng_Morse(self):
		newString = ""
		listofNew = self.trans.split(" ")
		for i in listofNew:
			for t in i:
				newString += self.stringMorse[t]
				newString += " "
			newString += " / "

		print(newString)

# main() asks user what way they wish to translate, along with
# the string they want translated, and produces the translated version
# of the input.
def main():
	while True:
		choice = str(input("What way do you want to translate?\
(m to translate morse to english and e for english to morse.) :"))
		inp = MorseTrans(str(input("Enter the string to translate:")))
		if choice == "m":
			inp.morse_Eng()
			break
		elif choice == "e":
			inp.eng_Morse()
			break
		else:
			print("You have to choose e for english->morse or\
	 m for morse->english")

main()