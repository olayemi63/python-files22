# List Comprehension



squareNums = []


# Type it in
# Iteration: for loop
# Comprehension: concise, easier way

x  = 100

for i in range(x):
    squareNums.append(i * i)
    # squareNums.append(1 ** 2) # Exponentiation Operator (x ** power)
    print(squareNums)


# Building a List with List Comprehension
"""Syntax

list = [(expression)(for)]

"""
print("\nUsing List Comprehension:")

seq = [i for i in range(x)]
print(seq)

squareNums2 = [(i ** 2) for i in range(1, x)]
print(squareNums2)


seq2 = [((i + 10) * 2) * i for i in range(x)]
print(seq2)

seq3 = [i for i in range(20) if i > 10]
print(seq3)


# Example with 2 lists: Find Common Items between the lists

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
listB = [5, 6, 7, 8, 9, 10, 11, 12, 13]

listCommonsAB = [a for a in listA if a in listB]
print(listCommonsAB)


listC = [(a, "apples") for a in listA]
print(listC)

listD = [["apple", "banana", "cranberry"] for a in range(20)]
print(listD)