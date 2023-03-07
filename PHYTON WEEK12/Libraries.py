"""
LIBRARIES
SOME GFunctions that we'd like to use, need to be imported
We can import modules/functions from the Python Standard Library 

Use the "import" and from keyword to import module from the standard library
[FROM TIME IMPORT SLEEP]

# Asterisk (*) will import everything from that module

Sleep is a function that will pause the execution of the code

randint(0, 10) will return a random number within the range given (0, 10) 
"""

"""
from time import sleep
from random import randint, random, shuffle, choice #use comma to import multiple things
from math import sqrt




print("Hello world")
sleep(2)
input("Press Enter to continue...")

print("Welcome to Python Programming")
sleep(2)
print("Have a nice day")    
print("Goodbye world")


print(sqrt(49)) 
"""

"""
Exercises (15 mins) till the end# 

1.] import math square root function(). let the user input a number and print the square root of it.
2.] import random randint(x, y) let the user input 2 numbers, generate a number between the range of those 2 numbers given.
3.] Take a name from the user and generate a random number: make a concatenating their name and a random generated number.

"""

from math import sqrt

"""
userString = input(77)
print(sqrt(77))
"""

userNum = int(input("EnterNumber to square root"))
answer = sqrt(userNum)
print("The Square Root of", userNum, "is", answer)


from random import randint, random
"""
Num1 = int(input(1))
Num2 = int(input(10))

print(randint(Num1,Num2)) 
""" 



userName = input("Enter your UserName")
randnum = randint(100, 999)

print(userName + str(randnum)) 
