"""
Iteration
Looping, repeating code

for loops

for variable in range():
     indented-code which will repeat a number of times

while loops

"""
"""
print("Hello World")

for i in range(10):
    print("Hello World, i")
    print(i)
"""

for i in range(5, 10, 2):
    print("hello world", i)


#Iterating through a collection (list) [range]
# For element in collection
    basket = ["orange", "apple", "melon", "papaya"]

    for element in basket:
        print(element)  


    """ While loops
# Indefinite Iteration

While condition:
      indented code-block


    """

x = 0

while x <= 10: # while loops can possibly run forever
    x = x + 1
    print("Hello World", x)
    x = x + 1

# Ex 1.) String Repeater: create a program that will repeat print a number of times: 
# let the user input both the string and the number of times they'd like to repeat it. 
# # Ex 2.) Create a program that will ask the user to guess a pass-code.
# # should keep on asking continuously until they get it right.
# # set a pass-code variable# let the user enter a guess at the pass-code
# # check if they got it right or wrong: loop continuously until they get it right.



i = 5
for i in range(1, 5):
    print("King Rafa Nadal ")


userString = input("Enter a string to repeat: ")
repeater = int(input("How many times would you like to repeat?"))
               
for i in range(repeater):
        print(userString)



userInput = ""
passcode = "pass123"

while userInput != passcode:
     userInput = input("Enter the passcode: ")

print("access granted")


String = input("Come on over")
int = input(55)
repeat = input(5) 
i = i + 1
print("Come on over", "55", i)
