#DICTIOANRIES >>> stores values as key value pairs

student = {
    "name": "Adnan",
    "age": 20,
    "city": "Srinagar"
}

print(student)

#accesing element of a dictionary
print(student["name"])
print(student["age"]) #NOTE: this can throw an error if the key doesnt exist

#Safer way to access elements
print(student.get("age"))
print(student.get("course")) #will return None


#Adding a value
student["course"] = "CSE"
print(student.get("course"))

#updating a value
student["age"] = 26
print(student.get("age"))

#updating multiple values
student.update({
    "state" : "srinagar",
    "college" : "LPU"
})

print(student)


#TAKING DICTIONARY AS INPUT

input_dict = {}
input_dict["name"] = input("Enter name: ")
input_dict["age"] = int(input("Enter age: "))
print(input_dict)


#using a loop
data = {}
number = int(input("Enter number of items: "))
for i in range(number):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value
print(data)



#Removing values from a dictionary

#pop()
student.pop("age") #this doesnt work like a list pop() which uses index, this uses a key
print(student.get("age"))

#del
del student["city"]
print(student.get("city"))

del student #NOTE: we can use del to remove whole dictionary as well
#print(student) NOTE: will throw an error



student = {
    "name": "Adnan",
    "age": 20,
    "city": "Srinagar"
}

#DICTIONARY METHODS
print(student.keys()) #will give all the keys of a dict
print(student.values()) #will give all the values of a dict
print(student.items()) #will give both keys and values


#checking if a key exists in a dict
print("age" in student) #by default this checks keys
print(20 in student.values()) #checks values


#length of a dict
print(len(student)) #checks key-value pairs


#copying a dict

student1 = {
    "name" : "adnan",
    "age" : 20
}
student2 = student1 #this means both variables refer to the same dict
student2["city"] = "srinagar" #this change will be made in both

print(student1)
print(student2)

#creating a seperate copy
student_a = {
    "name" : "adnan",
    "age" : 20
}
student_b = student_a.copy() #will create a seperate copy of the dict
student_b["city"] = "srinagar" #changes will be only in student_b dict
print(student_a)
print(student_b)

#NESTED DICTIONARIES
dict_1 = {
    "book1" : "python",
    "books" : {
        "book2" : "Java",
        "book3" : "CSS"
    }
}

print(dict_1["books"]["book2"])
print(dict_1.get("books").get("book2"))



student = {
    "name": "Adnan",
    "age": 20,
    "city": "Srinagar"
}

#looping through a dict
for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, ": ", value)

# Task	        Code
# Access value	    student["name"]
# Safe access	    student.get("name")
# Add/change	    student["city"] = "Srinagar"
# Remove	        student.pop("age")
# Keys	            student.keys()
# Values	        student.values()
# Both	            student.items()
# Check key	        "name" in student
# Check value	    "Adnan" in student.values()
# Copy	            student.copy()

#Q1. Personal Information - Create a dictionary containing: name age city course Then: Print the value of name. Change the value of age. Add a new key called hobby. Print all keys. Print all values. Print the final dictionary.
data = {
    "name" : "Adnan",
    "age" : 26,
    "city" : "Srinagar",
    "course" : "CSE"
}
print(data.get("name"))
data["age"] = 25
data["hobby"] = "Football"
print(data.keys())
print(data.values())
print(data)

#Q2. Student Marks Start with: marks = { "Python": 85, "SQL": 90, "Excel": 80 } Perform the following: Print the marks for "SQL". Add "Power BI" with marks 88. Change "Python" marks to 92. Remove "Excel". Check whether "Java" exists as a subject. Print the final dictionary.
marks = {}
num = int(input("Enter number of key-value pairs: "))
for i in range(num):
    key = input("Enter subject: ")
    value = int(input("Enter marks: "))
    marks[key] = value
print(marks.get("SQL"))
marks["Power BI"] = 88
marks["Python"] = 92
marks.pop("Excel")
print("Java" in marks)
print(marks)

