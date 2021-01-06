#1
musicians = ["Music 1",
             "Music 2",
             "Music 3"]


#2
locationA = (1,1)
locationB = (2,2)
locationC = (3,3)

mylocations = [locationA,
                locationB,
                locationC]


#3
attributes = {"height":
              "6'1''",
              "favorite color":
              "blue",
              "favorite author":
              "Charles Dickens"}


#4
n = input("Enter height, favorite color, or favorite author: ")

if n in attributes:
    attr = attributes[n]
    print(attr)
else:
    print("Not found in attributes.")

#5
song1 = ["A1", "B1", "C1"]
song2 = ["A2", "B2", "C2"]
song3 = ["A3", "B3", "C3"]

musiciansongs = {musicians[0]:
                   song1,
                   musicians[1]:
                   song2,
                   musicians[2]:
                   song3}


#6
"""
SETS

-Sets are used to store multiple items in a single variable
-Sets are immutable and unordered
-Sets cannot be accessed by index, unlike lists and tuples

-When should you use a set?
    -To remove duplicate values from a collection
    -Sets are highly optimized for checking whether a
     a specific element is contained in a set


https://www.w3schools.com/python/python_sets.asp

https://www.geeksforgeeks.org/sets-in-python/
"""

