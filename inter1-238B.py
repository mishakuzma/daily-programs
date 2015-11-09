import sched, string, time, sys

s = sched.scheduler(time.time, time.sleep)

def add():
	# add() will add a new event when the user wishes for it to
	# be added
	new_time = input("At what time is the event?: ")
	s.enterabs(new_time, 1, time.time)
	menu()

def mod():
	# mod() will delete an event and replace it with a new event of the
	# user's choice
	new_time = input("Which time do you want to modify? ")
	new_action = input("What do you want that event to do?")
	s.cancel(new_time)
	s.enterabs(new_time, 1, new-action)
	menu()

def dele():
	# dele() will delete an event that is occuring at the time that 
	# the user specifies that it will occur
	new_time = input("Which event do you want to cancel?")
	s.cancel(new_time)
	menu()

def view():
	# view() shows the event chart to the user
	s.queue
	menu()


def main(menu_opt):
	# function main will call upon four other seperate functions
	# which dictate actions on the event calendar, before returning
	# the menu
	if (menu_opt == 1):
		add()
	elif (menu_opt == 2):
		mod()
	elif (menu_opt == 3):
		dele()
	elif (menu_opt == 4):
		view()
	else:
		sys.exit()

def menu_failsafe():
	# function menu_failsafe checks if the user entered a valid input
	while True:
		try:
			menu_opt = int(raw_input("Please select an object: "))
			return menu_opt
			break
		except ValueError:
			print "You must select an integer between 1 and 4."
	return menu_opt


def menu():
	#Present user with a series of numbers which they select in
	#order to select an action
	print("Welcome to event scheduler V0.1. Please select an option:")
	print("1: Add an event")
	print("2: Modify an event")
	print("3: Delete an event")
	print("4: View your calendar")

	menu_failsafe()
	main(menu_opt)

menu()