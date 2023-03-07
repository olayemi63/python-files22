"""
SUBROUTINES



"""
"""
print("Hello, world!")
print("Welcome to Python Programming")
print("Have a nice day")
print("Goodbye world!")
"""

# Subroutines allow us to group and rescue code
# Creating a Subroutine
# Define an identifier
"""
#def identifier():
     code-block 
     code-block 
     code-block 
     code-block 
    code de-indented isn't part of the subroutine

     """
"""
def greeting():
    print("Hello World")
    print("Welcome to Python Programming")
    print("Have a nice day")    
    print("Goodbye world!")
# not inside the subroutine isn't part of the block

# Invoking the subroutine: Calling it. Running it Launching it.


greeting() # Invoke the greeting() subroutine.

greeting()

greeting()
"""
""" Subroutines with parameters

#def identifier(parameter1, parameter2, parameter3, parameterN)
     code-block 
     code-block 
     code-block 
     code-block 
    code de-indented isn't part of the subroutine

"""


def greeting2(name):
    print("Hello", name)
    print("Welcome to Python Programming")
    print("Have a nice day")    
    print("Goodbye world and take care", name)

greeting2("Rafael Nadal")