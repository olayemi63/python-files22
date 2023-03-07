# Collections
# Tuples, Dictionaries and Sets

# List
"""
myList = [10, 20, 30, 40, "bread", "rice"]

# Tuple (Immutable)
# Defined by a round bracket.

myTuple = (10, 20, 30, 49, 50, 60)

myList.append("Test")

print(myList)

print(len(myTuple))


len() - returns the length
min()
max()




print(min(myTuple))
print(max(myTuple))

# Dictionary
# Are similar to Objects in JavaScript
# Key-Value pairs
# Key: Value



object = {firstName: "Rafael", lastName: "Nadal"}

dictionary = {
     key: value
}
"""

person = {"firstName": "Rafael",
      "lastName": "Nadal",
       "age": 25,
       "bio": "A Straight-Forward and Effective Man"
 }

# Outputting a Dictionary
print(person)

# Accessing the dictionary

# How to access firstName

# Access a dictionary like you would other collection; list [index], tuple[index] dict [key]person["firstName"]
print(person["firstName"])
print(person["lastName"])
print(person.get("firstName"))
print(person.get("age", "10 Pivot Lane"))

person ["age"] = 26
# remove then rewrite


# Updating values
person["age"] = 26
person.update({"age" : 26})

print(person)

# Removing Values from the dictionary
# Adding/Removing Values

person.pop("bio")
print(person)

person.update({1: "Test"})
print(person)

# Removing 

del person["age"]

print(person)


# SETS
# Unordered / Unindexed / Unchangeable / Unique
# Unique: Will eliminate Duplicate Values
# Unordered / Unindexed

mySet = {"a", "b", "c", 10, 23, 40, 10, 40, "a", "b", "c", 10}
print(mySet)


# Accessing Sets
# You can't access a set directly

print("a" in mySet)

findItem = "a"
if findItem in mySet:
    print("This is true")


# Add/remove items from sets.

    mySet.add(20424094)
    #mySet.discard(10)

mySet.pop() # remove the "last item from the set, but Sets are random
mySet.pop()
mySet.pop()
mySet.pop()
mySet.pop()

print(mySet)

