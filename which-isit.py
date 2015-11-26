import tkinter, os

os.chdir("C:\selfPrograms\dailyProg\inFiles")
s = open("age_input.txt", "r")

# main() asks user for number of years old they are
# and will produce the number of months, days (excluding leap years),
# hours, minutes
def main():
	age_in = int(s.readline())

	while type(age_in) is int:
		month = age_in * 12
		day = age_in * 365
		hours = day * 24
		minutes = hours * 60
		os.chdir("C:\selfPrograms\dailyProg\outFiles")
		r = open("age_output.txt", "w")
		r.write("Months: {} Days: {} Hours: {} Minutes: {}".format(month, day, hours, minutes))
		if type(s.readline()) is int:
			age_in = int(s.readline())
		else:
			break

	r.close()
	s.close()

main()







