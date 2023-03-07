# ERROR HANDLING
# EXCEPTION HANDLING

import logging 

# To Do Exception handling we use:

"""
try:
    block code
    block code 
    block code
    block code
except
    block code
    block code
    


    Attempt 
    """

print("Rafael Nadal")




try:
    x = 10
    y = int(input("Enter a Number to add"))
    print(x + y)
except ValueError as err:
    print("You can't type a number with a string")
except ZeroDivisionError as err2:
    print("You can't Divide by zero") 
except Exception as err:
    print("Another error has occurred")




print("here is the rest of the Code")
print("Goodbye World")