# Daily programmer Easy 1 (cell 238A)
# Misha Kuzma on October 19, 2015

import string
import os

os.chdir("C:\Users\Misha Kuzma\Programs\dailyProg\outFiles")
#!/usr/bin/python

# Varibles that control name, age and username

name = raw_input("Please input your name: ")
age = raw_input("Please input your age: ")
user = raw_input("Please input your reddit username: ")

print("Your name is " + name + ", you are " + age + " years old, and your username is " + user)

# Outputs a text file with the output of the above function
file = open("user_Data.txt", "w", 0)
file.write("Your name is " + name + ", you are " + age + " years old, and your username is " + user);
file.close()
