
"""

# 2D LIST
# TWO-DIMENSIONAL LIST

# Is basically a List within a List





a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

2DList = [a, b, c]

Method 2


twoList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]


]

# Accessing Number 5

twoList[1][1]
print(twoList[1][1])


twoList.append[1][2] = 60
print(twoList[1][2])


"""
### Exercise 1
# "Given TupleA, find the occurences of 20"
# TupleA = (10, 20, 30, 40, 20, 30, 10, 10)
#print(TupleA.?????(20))
"""
TupleA = (10, 20, 30, 40, 20, 30, 10, 10)
for i in range(20):
    print(TupleA[i + i ])

TupleA = (10, 20, 30, 40, 20, 30, 10)
print(TupleA.count(20))


### Exercise 2

#Given the Dictionary:

# Do a.) and b.) below"
"""
"""
person = {
  "firstName": "George",
  "lastName": "Johnson",
  "Age": 24,
  "Bio": "A Laid back person.",
 	1: "Some First data",
  2: "Some Secondary Data",
  3: 50000
}
# a.) Delete the Keys 1, 2, 3.
# b.) Add an Address to the Person
print(person[1])

del person[1]
del person[2]
del person[3]
print(person)

person.update({"Address:1 Pelican Gardens London SE1 2TD:"})
print(person)
"""

### Exercise 3
## Given setA, verify that Adam and Amy are inside the set."

setA = {21, 6.9, -6, "Adam", "Danielle", "Pauline", 200, "Amy", "Third"}

# print("a" in mySet)

findItem0 = "Adam" 
findItem1 = "Amy"
if findItem0 in setA:
    print("This is true")
if findItem1 in setA:
    print("This is true")



# print("a" in setA)

"""
print("Adam" in setA)
print("Amy" in setA)

if "Amy" in setA:
    print("Amy is in the set")

#Exercise 4
# Access and Print the values from the 2D list, stated below"

"""
"""
twoList = [
  [12, 43, 7523],
  [2467, 31, 553],
  [53, 32, 43]
]
# Access 12
# Access 53
# Access 31

twoList[0][0]
print(twoList[0][0])

twoList [2][0]
print(twoList[2][0])

twoList [1] [1]
print(twoList[1][1])

"""
"""
### Exercise 5
## "Use List Comprehension to Generate a sequence of the first 10 Cubed Numbers"

"""
"""
print("\nUsing List Comprehension:")

# squareNums = [i * i for i in range(10)] # i ** 2
cubeNums = [(i * i * i) for i in range(10)] # ** 3

print(cubeNums)
"""



### Exercise 6
## Given a List namesA, Use List Comprehension to generate a new list with the Length of Each Word."

namesA = ["Ryan", "Lucy", "Kim", "Xin Zhao", "George", "Jake", "Oliver"]

namesB = [i*2 for i in namesA]

# LC = [(expression)(for loop)]

print("\nName Length List:")
print(namesB)

 
namesALength = [len(i) for i in namesA]

# print("Name List")
# print(namesA)

print("\nName Length List:")
print(namesALength)

print(len)  

