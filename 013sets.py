#SETS >>> collection of unique items 1. Sets do not allow duplicate values. 2. Sets are unordered.

fruits = {"apple", "mango", "banana"}
numbers = {1,2,3,4,5}
mixed_set = {1,2,"adnan"}

#numbers_0 = {} >>> this is not an empty set
number_0 = set() #>>>this is an empty set


#Taking input for a set
input_set = set(input("Enter set items: ").split()) #will take strings as input
input_int_set = set(map(int,input("Enter integer elements: ").split()))

nums = set([1,2,3,4]) #creating set from a list
nums1 = set((1,2,3,4)) #creating set from a tuple
print(nums)
print(nums1)

#duplicate values are automatically removed from a set
set_0 = {1,2,2,3,3,4,4,5,5,6}
print(set_0)


#so if we have to remove duplicates from a list we can do this
list_a = [1,2,2,3,3,4,4,5,6]
print(list_a)
list_a = set(list_a)
list_a = list(list_a)
print(list_a)


#NOTE: Since sets are unordered we cnt using indexing



fruits = {"apple", "mango", "orange"}
print(fruits)

#ADDING ITEMS IN A SET
fruits.add("kiwi") #adds only one item at a time
print(fruits)

fruits.update(["grapes", "banana", "melon"]) #update adds multiple items at a time
print(fruits)

fruits1 = {"tomato", "blueberries"}
fruits.update(fruits1) #we can also add another set to a set
print(fruits)


#REMOVING ITEMS FROM A LIST
fruits.remove("blueberries") #NOTE: if the items doesnt exist it will throw an error
print(fruits)

fruits.discard("orange") #NOTE: if the item doesnt exist it wont throw an error it will simple do nothing
print(fruits)

fruits.pop() #it will remove any random element from the list since indexing doesnt work
print(fruits)

fruits.clear() #removes all the elements from the set
print(fruits)


numbers1 = {1,2,3,4,5,6,7,3,1}

#checking if an item is in the set
print(4 in numbers1)

#length of a set
print(len(numbers1)) #if there are any duplicate values it wont count them

#NOTE:THIS IS WHERE SETS BECOME REALLY USEFUL
#we can perform various operations like union, intersection, difference, symmertric difference

set1 = {1,2,3,4}
set2 = {3,4,5,6}

# union() or | >>>combines both sets and removes duplicates NOTE:order of writing doesnt matter
print(set1 | set2)
print(set1.union(set2))

#intersection() or & >>>returns only values present in both sets NOTE:order of writing doesnt matter
print(set1 & set2)
print(set1.intersection(set2))

#difference() or - >>>returns values present in first set but not in second NOTE:order of writing matters
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)
print(set2.difference(set1))

#symmetric difference ^ >>>returns values that are nt common in both sets NOTE:order of writing doesnt matter
print(set1 ^ set2)


#converting a set into a list or a tuple NOTE: but there is no guarantee of that we will get items in a particular order
set3 = {1,2,3,4,5,6}
print(set3)
set3 = list(set3)
print(set3)
set3 = tuple(set3)
print(set3)


#Q1. Remove Duplicates Ask the user to enter several numbers separated by spaces. For example: Enter numbers: 1 2 2 3 4 4 5 Then: Convert the input into a list. Convert the list into a set to remove duplicates. Print the set. Print the number of unique values.
numbers = [1,2,2,3,4,4,5]
numbers = set(numbers)
numbers = list(numbers)
print(numbers)
print(len(numbers))

#Q2. Set Modifier - Start with: colors = {"red", "blue", "green", "yellow"} Perform the following: Add "black". Add "white" and "orange" together. Remove "green". Try removing "purple" without causing an error. Print the final set.
colors = {"red", "blue", "green", "yellow"}
colors.add("black")
colors.update(["white", "orange"])
colors.remove("green")
colors.discard("purple")
print(colors)

#Q3. Common and Different Values - Start with: set1 = {1, 2, 3, 4, 5} set2 = {4, 5, 6, 7, 8} Print: All unique values from both sets. Values common to both sets. Values present in set1 but not set2. Values present in either set but not both.
set1 = {1, 2, 3, 4, 5} 
set2 = {4, 5, 6, 7, 8}
print("unique values:",set1 | set2)
print("common in both sets:", set1 & set2)
print("values in set1 but not in set2:", set1 - set2)
print("values in either but not both:", set1 ^ set2)