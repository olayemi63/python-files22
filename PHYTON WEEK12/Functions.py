"""
FUNCTIONS
A FUNCTION IS SIMPLY A SUBROUTINE WITH A RETURN STATEMENT

CREATING A FUNCTION
#def identifier():
     code-block 
     code-block 
     code-block 
     code-block 
     RETURN STATEMENT  # Output


    code de-indented isn't part of the function

"""
"""
def myFunction():
    return "Hello World" # The evaluation of a function

myFunction() # "Hello World"
print(myFunction()) # Print "Hello World")

variable1 = myFunction() # "Hello World"
print(variable1)


def squareNumber(x):   #Parameters act like an input
    result = x * x     #Code acts as the process
    return result      #Return acts as the Output

myNum = squareNumber(7) #

print(myNum)

Write a function that will Cube a Number. Take a single parameter and return the cube (x^3)
- Write a function that will add 2 numbers together. the function will take 2 parameters and return the sum of them.
- write a function that will find the average of 3 numbers. the function should take 3 parameters and then return the average (sum / 3)
- Write a function that takes a list of numbers, iterates through it and finds the total sum of the list.


"""
def cubeNumber(x):
    result = x * x * x
    return result
myNum = cubeNumber(7)
print(myNum)             #343


def addNumbers(x, y):
    result = x + y
    return result
mNum = addNumbers(7, 7)
print(myNum)             #14




def findAverageOf3(x, y, z):
    total = x + y + z
    result = total / 3
    return result
print(findAverageOf3(45, 90, 180))


myList = [30, 342, 4, 21, 53, 523, 66, 21]

def totalSumList(listin):
    total = 0
    for num in listin:
        total = total + num
    return total

print(totalSumList(myList))