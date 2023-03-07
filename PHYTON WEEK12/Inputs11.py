"""

Exercise (20 Mins)

1.) Create 3 variables and take input: firstName, lastName, Age and let the user enter them.

2.) Display a welcome message: output their names and age back to the console

3.) Create a addition calculator: Take 2 numbers, add them and display the result back.


"""
"""

firstName = ("Yemi")
lastName =  ("Adio")
Variable3 = 45
Variable4 = 50
Variable5 = 60

print("Hello, World!")
print(firstName, lastName, Variable3) 
print(Variable4 + Variable5)


"""
"""
firstName = input("Enter your last Name:")
lastName = input("Enter your first Name:")
age = input("Enter your age:")

"""

# print("Hello World",  firstName, lastName, "You are", age)



Variable4 = input("Enter first Number:")
Variable5 = input("Enter second Number:")
print(Variable4 + Variable5)

# Converting Between Data Types


int()
float()
str()
bool()  

# Concatenating Strings


num1 = 7
num2 = 150
num3 = 3.56789000
num4 = 75
num5 = 800
num6 = 100
num7 = 1000
num8 = 900

print(num1 + num2) # Addition          +
print(num3 - num4) # Subtraction       -
print(num4 * num5) # Multiplication    *
print (num5 / num4) #D Division        /


print (num6 / num5)
print(num7 % num5) #Modulus Division % (Returns the remainder of a non-whole division)  
print (num8 ** num5) #Exponentiation ** (Raise a number of the other)



# FLOATS

myFloat = 94.38933333
print(myFloat)
print("%.2f" % myFloat) # Use the "%.nf to round the number to N significant figures

# Dividing numbers will always return them as a float
print(50 / 5)
print(type(50 / 5))



# List [Another data (type) Dat Structure]
# Allows us to store multiple datatypes in sa structure
# List is like a Variables: identifier
# Use square brackets to define a List


myList = [10, 34, 40, 50, 63, 72, 56] 

print(myList)
print(type(myList))

print(myList[4])

# Accessing Values in python
# We want to access 63:
print(myList[4]) #myList[4] = 63

# Adding a New Values to the list
# push, insert


myList.append(100)
print(myList)
myList.insert(0, 357)
print(myList)


# Removing values from a list

myList.remove(63)
print(myList)