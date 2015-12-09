import os, time, sys

class Credential:
	"Holds a username and password, as well as information to\
 write and read a user and pass."

	def __init__(self, user, password):
		self.user = user
		self.password = password

	def writeInfo(self):
		os.chdir("C:\selfPrograms\dailyProg\outFiles")
		s = open("passInfo.txt", "w")
		s.write("User and Pass for 234A: \n")
		s.write("User: " + str(self.user) + "\n")
		s.write("Password: " + str(self.password))
		s.close()

""" main() will ask the user for a user and a pass. The user
has three attempts to open the program with the proper set of 
credentials (a user and a pass). If they fail to do so, the
program quits. If they succeed, the file is opened."""

def main():
	""" existPass() will check a folder for an existing document that 
contains a username and password. If one exists, the checked user
and pass will become the one that is checked by the program. If not,
user will be asked to write the user and pass."""
	def existPass():
		os.chdir("C:\selfPrograms\dailyProg\outFiles")
		try:
			s=open("passInfo.txt", "r")
			w = s.readline()
			while w != "":
				if "User: " in w:
					user = w[6:w.find("\n")]
				elif "Password: " in w:
					passW = w[10:]
				else:
					pass
				w = s.readline()
			newCred = Credential(user, passW)
			return newCred
		except FileNotFoundError:
			newCred = Credential(str(input("Please input a new user: ")), \
				str(input("Please input a new pass: ")))
			newCred.writeInfo()
			return newCred

	x = 0
	existPass()
	while x < 3:
		userAttempt = str(input("Please enter your Username: "))
		passAttempt = str(input("Please enter your Password: "))

		if userAttempt == str(existPass().user) and \
passAttempt == str(existPass().password):
			break
		else:
			x += 1
			print("You have " + str((3 - x)) + " attempts left.\n")

	if x == 3:
		print("Access denied")
		sys.exit()
	else:
		print("File opened")
		sys.exit()

main()