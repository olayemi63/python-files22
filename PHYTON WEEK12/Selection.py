# If Statements
# Selection of Statements
# Control the flow of code in our progress
# If a condition is true, the we execute some code

"""
if condition:
    indented-codeblock
    indented-codeblock
    indented-codeblock
    indented-codeblock
norma de-indented code
normal de-indented code
normal de-indented code
normal de-indented code

This is javascript If statement
if (condition) {
        codeblock

}


Conditional Operators
use these to build a condition.
>   Greater than
<   Less than
==  Equal to
<=  Less than or equal
"""


"""
x = 30

if 30 > 10:
    print("Hello, World!")

    print("Some more lines of code here")
"""



"""
    If-Else Statement

    If the condition isn't met then we can run some alternative code

    

    If condition:


    


    IF-Elif (If-Else-If) Statement
    If the condition isn't met, then we can run some alternative code

    If condition:
       indented-codeblock
    elif condition:
       indented-codeblock, if the initial condition isn't met   

    "Elif" is short for "else if"

    """

"""
y = 5
if y > 10:
    print("Python is Dope")

else:
    print("Goodbye, Python")



num = 0

if num > 0:
     print("This is a positive number")
elif num == 0:
    print("This is Zero")
else:
    print("This is a negative number")

"""
# 3 Exercises (25 mins) 
# Create a program that lets a user input their age, checks if they are old enough to vote (over 18)
# Create a program that lets a user enter 2 numbers. Compare them and print to the user:
# if the first is greater the other ,
# if the second is greater then the other
# or if they are both equal# Create a program that lets a user enter their score between 0 and 100 and it will grade the score
# A: 80 - 100
# B: 60 - 79
# C: 40 - 59
# D: 20 - 39
# E: 0 - 19
#Extension: print if they've given an invalid score





userAge = int(input("Enter your age:"))
if userAge >= 18:
        print("You are Old enough to vote")
else:
        print("You are not old enough to vote")


num1 = int(input("Enter your first Number:"))
num2 = int(input("Enter your second Number:"))

if num1 > num2:
     print("Your first number", num1, "is greater than the second number", num1)
else:
             print("Number", num1, "and", num2, "are equal.")


userScore = int(input("Enter your score (0-100): "))

if userScore >= 80:
    grade = "A"
elif userScore >= 60:
      grade = "B"
elif userScore >= 40:
      grade = "C"
elif userScore >= 20:
      grade = "D"
elif userScore >= 0:
      grade = "E"

print("Your final grade is: " + grade)


"""
Nested If statements

if condition:
    code
    code

  code
  code
  code

  """
userScore = int(input("Enter your score (0-100): "))
grade = "A" 
  
if userScore > 100 or userScore < 0:
    print("invalid entry.")
    if userScore >= 80:
       grade = "A"
elif userScore >= 60:
       grade = "B"
elif userScore >= 40:
       grade = "C"
elif userScore >= 20:
       grade = "D"
elif userScore >= 0:
       grade = "E"








