# Function calculator and printer
# Will perform calculations and print them to a file called "function_output.txt"
# Misha Kuzma Oct 20, 2015

import string
import os

whileOn = 1
os.chdir("C:\Users\Misha Kuzma\Programs\dailyProg\outFiles")
f = open("function_output.txt", "w", 0)

while whileOn == 1:
	animal_amount = input("How many aminals are there?" )
	f.write("#_of_Animals: " + str(animal_amount) + "\n")
	animal_consum = input("How much does this animal eat? ")
	f.write("Ani_Consumpt: " + str(animal_consum) + "\n")
	food_cost = input("How much does that food cost? ")
	f.write("food_cost: " + str(food_cost) + "\n")
	product = food_cost * animal_amount * animal_consum
	print("The animals cost : " + str(product) + ".")
	f.write("The animals cost : " + str(product) + "." + "\n")
	whileOn = input("Type 1 in order to continue")