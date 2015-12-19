""" Duplicate integer solver. Takes in an input that is an array of 
integers and outputs an element of the array that is repeated 
(assuming that only one integer is repeated).
Created by Mykhaylo Kuzma on Dec. 18, 2015"""

def main():
	inInit = str(input("Give your array of numbers as a row of\
 integers, seperated by spaces: "))
	looperList = []
	inProc = inInit.split(" ")
	for i in inProc:
		if i in looperList:
			print(i + " is the duplicate integer.")
			break
		else:
			looperList.append(i)
	
main()