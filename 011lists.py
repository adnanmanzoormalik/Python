#LISTS

fruits = ["mango", "orange", "apple", "kiwi"]
list0 = ["adnan", 10, True, 12.22] #lists can take various data_types

print(fruits[2]) #lists use indexing like strings
print(fruits[-1])

print(fruits)
for fruit in fruits:
    print(fruit)

#taking input in a list
names_list = input("Enter names: ").split()
print(names_list)

nums_list = input("Enter numbers: ").split() #this will take input as a string
print(nums_list)

nums_list1 = list(map(int,input("Enter nums: ").split())) #important
print(nums_list1)

#unlike strings lists are mutable
fruits[0] = "banana"
print(fruits[0])

#list slicing
print(fruits[0:2])
print(fruits[1:])
print(fruits[-2:])

names = ["adnan", "asrar", "omais", "rayhan", "zainab"]
print(names)

#adding items to a list
names.append("zaira") #adds items to the end of a list
print(names)
names.insert(1,"saad") #adds items at a specific position
print(names)
names.extend(['jazz', 'khushi'])
print(names)

#removing elements from a list
names.remove("asrar") #removes a specific value and can raise an error if the value isnt present
print(names) 
names.pop(1) #removes item at a specific position
print(names)
names.pop() #we if dont give an index here, it will remove the last element
print(names)

#we can also return the removed item using pop
poped = names.pop()
print(poped)
print(names)

vegs = ["tomato", "potato", "onion", "carrot", "peas"]
del vegs[1] #deletes item at a specific position, can raise an error
print(vegs)
del vegs[:2] #we can del multiple items using slicing
print(vegs)

del vegs #we can remove whole list


list1 = ['a','b','c','d']
print(len(list1)) #finding length of a list
print("a" in list1)
print("c" not in list1)

nums = [1,3,2,4,5,7]
print(nums)
nums.sort()#sorting in ascending order
print(nums)
nums.sort(reverse=True) #sorting in descending order
print(nums)

alpha = ['a','f','r','c','e','d','c']
alpha.reverse() #gives the reverse of the actual list
print(alpha)
alpha.sort() #sorts in alphabetical order
print(alpha)

#finding position of an item
print(alpha.index("f"))

#find the count of an item
print(alpha.count('c'))

#joining lists
list_a = [1,2,3]
list_b = [4,5,6]
list_c = list_a + list_b
print(list_c)

#copying a list

list_d = [1,2,3,4]
list_e = list_d #NOTE: these 2 variables now point at the same list no new list is created
print(list_d)
print(list_e)
list_e.append(5) #this appends the list and thus both variables get appended
print(list_e)
print(list_d)

#creating a seperate list
list_f = [1,2,3,4]
list_g = list_f.copy() #creates a seperate list
list_f.append(5) #just appends list_f
print(list_f)
print(list_g)


# Important List Methods Summary
# append()	Add to the end
# insert()	Add at a specific index
# remove()	Remove a specific value
# pop()	Remove using index / last item
# sort()	Sort the list
# reverse()	Reverse current order
# index()	Find item's index
# count()	Count occurrences
# copy()	Create a copy

#Q1. Favourite Things: Create a list containing 5 of your favourite things. Then: Print the first and last item. Change the third item to something else. Add one new item to the list. Remove one item from the list. Print the final list and its length.
fav_things = input("Enter your 5 fav things: ").split()
print(fav_things[0] + " " + fav_things[-1])
fav_things[2] = "glass"
fav_things.insert(0,"cricket")
fav_things.pop()
print(fav_things)
print(len(fav_things))

#Q2. Number Manager- Start with: numbers = [12, 5, 8, 12, 20, 3, 12] Perform the following: Print how many times 12 appears. Add 15 to the list. Remove 5. Sort the list in ascending order. Print the final list. Print the index of 20.
numbers = [12,5,8,12,20,3,12]
print(numbers.count(12))
numbers.append(15)
numbers.remove(5)
numbers.sort()
print(numbers)
print(numbers.index(20))

#Q3. List Copy Challenge - Start with: original = ["Python", "SQL", "Java"] Create a copy of original called courses. Add "JavaScript" to courses. Remove "Java" from courses. Print both lists. Make sure original remains completely unchanged.
original = ["Python", "SQL", "Java"]
courses = original.copy()
courses.append("JavaScript")
courses.remove("Java")
print(original)
print(courses)

