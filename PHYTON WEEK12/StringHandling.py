"""
# String Handling
# Making Strings Variables

userString = "string" # Single-line Strings

"""

firstName = "Rafael"
lastName  = "Nadal"

"""
# Multi-line String
myMulti
# This will hold Multiple Lines
# Returns in.
# The Return "\\n" is invisible in this function

print(myMultiLine0)

"""
"""
myMultiLine1 = "This is a Single Line String. \nBackslash N will make a new line"


myString = "This is a String with \"Double Quotes\" in it"
myString = 'This is a String with "Double Quote" in it'

print(myString)

firstName = "Rafael"
lastName  = "Nadal"
Age = 45
sentence = "Hello my name is ", firstName, "  and my last name is ", lastName, ""

print("using multiple arguments of print")
print(type(sentence))

print("using concatenation")
sentence = "Hello my name is " + firstName + " and my last name is " + lastName + "."


print("using string formatting")
sentence = f"Hello my name is {firstName} and my last name is {lastName}."

print(sentence)

# String Methods
#
myString = "Hello World"

# Finding the length of the string using length

print(f"the length of  {myString} is: {len(myString)}")

print(myString.upper())

print(myString.lower())

#String Slicing

myString
myString[0] 
print(myString[0])

myString[3]
print(myString[3])

# Use the : colon sign to slice Strings
# 
print(myString[3:]) # start at index 4 returns everything else infront

print(myString[:4]) # from the beginning upto (but  not including) 4

print(myString[:5]) # from beginning upto (but not including)
print(myString[1:5])
print(myString[-1])
print(myString[-2]) # d
print(myString[-2:]) # ld
print(myString[-6:]) # World



long = "This another sentence. i can continue typing right away"
print(long[-11:]) # right away

"""

# Exercises
#1] Copy and Paste this sentence into a variable: "The quick brown fox jumps over the lazy dog"- 
# Use Slicing to Return the word "jumps".- Use Slicing to return the words only "quick" and "fox". 
# Combine them into one string.- Turn the combined String into Upper Case.- 
# Let the user enter their FirstName, LastName and Age. 
# Using f-String Formatting, print their names and age in a welcome/greeting sentence.- 
# Display the Full Name as Captalized Initials. Example: Oliver Rimmington > O. R

#1
myString = "The quick brown fox jumps over the lazy dog"
print(myString[20:25])

#2
combined = f"{myString[4:9]} {myString[16:19]}"
print(combined)

#3

print(combined.upper())

#4
fName = input("Enter your firstName:")
lName = input("Enter your lastName:")
age = input("Enter your age:")

greeting = f"Welcome {fName} {lName} you are {age} years old. have a nice day."
print(greeting)


#5
print(fName[0])
print(lName[0])

initials = f"{fName[0].upper()}. {lName[0].upper()}"
            























