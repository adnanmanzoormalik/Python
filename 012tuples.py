#tuples >>> main diff between tuples and lists is unlike lists tuples are immutable, we use tuples when we dont want our data to change

colors = ("adnan", "asrar", "zaira")
items = ("adnan", 1, True)

fruit = ("mango") #NOTE: this is not a tuple, a single item like this is treated as string
fruits = ("mango",) #NOTE: this is a tuple with single item


#accesing tuple items
print(colors[0])
print(colors[-1])


#slicing
print(colors[:2])
print(colors[1:])


numbers = (1,3,2,5,2,6,1,7,8)

#count
print(numbers.count(2))

#index() >>> finding where an item is in a tuple
print(numbers.index(3)) #if we write an element which is nt in the tuple it will throw an error
print(colors.index("adnan"))

#checking if an item exists in a tuple >>>returns a boolean
print("adnan" in colors)
print(9 in numbers)
print(0 not in numbers)


#tuple unpacking
person = ("Adnan", 26, "Srinagar")
name, age, place = person #NOTE: vairables need to match the number of values of the tuple other wise there will be an error
print(name, " ", age, " ", place)


#conversion between list and tuple
tuple_a = (1,2,3,4)
tuple_a = list(tuple_a) #converts a tuple into a list and now we can append it if we want to
print(type(tuple_a))

list_a = [1,2,3,4]
list_a = tuple(list_a)
print(type(list_a))


#joining tuples
tuple_1 = (1,2,3)
tuple_2 = (4,5,6)
combined = tuple_1 + tuple_2
print(combined)

#repeating tuples
tuple_3 = (1,2,3)
print(tuple_3 * 3)

#Q1. Student Information Create a tuple containing: Name, Age, City, Course. Then: Print the first and last values. Print the total number of values. Use tuple unpacking to store all four values in separate variables. Print the name and course.
tuple_student = tuple(input("Enter name, age, city, course: ").split()) 
#NOTE: here we needed age as an int
# name = input("Enter name: ")
# age = int(input("Enter age: "))
# city = input("Enter city: ")
# course = input("Enter course: ")
# tuple_student = (name, age, city, course)
print(tuple_student[0])
print(tuple_student[-1])
print(len(tuple_student))
name, age, city, course = tuple_student
print(name, " ", course) #we dont need to add a space here as args in print automatically do so

#Q2. Number Tuple Start with: numbers = (10, 20, 30, 20, 40, 20, 50) Perform the following: Print how many times 20 appears. Print the index of 40. Check whether 100 exists in the tuple. Print the first three values using slicing. Print the last three values using slicing.
numbers = (10,20,30,20,40,20,50)
print(numbers.count(20))
print(numbers.index(40))
if 100 in numbers:
    print("yes 100 exists in numbers")
else:
    print("no 100 doesnt exist in numbers")
print(numbers[:3])
print(numbers[-3:])

#Q3. Modify an Immutable Tuple Start with: languages = ("Python", "Java", "SQL") Perform the following: Convert the tuple into a list. Add "JavaScript". Remove "Java". Convert the list back into a tuple. Print the final tuple.
languages = ("Python", "Java", "SQL")
languages = list(languages)
languages.append("JavaScript")
languages.remove("Java")
languages = tuple(languages)
print(languages)