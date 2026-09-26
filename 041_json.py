# JSON = JavaScript Object Notation >>> JSON is a text-based data format used to store and exchange structured data. 
# {
#     "name": "Adnan",
#     "age": 22,
#     "course": "Python"
# }
#commonly used in databases, APIs, web apps etc

# >>> JSON is built around a few basic data types. 

#1. Json Object >>>A JSON object is basically a collection of key-value pairs. >>>looks like a python dictionary
{
    "name": "Adnan",
    "age": 22
}
#keys must be strings
#we can access them as data["name"] and we can also modify them like data["name"] = "Asrar" and also add a new value dta["city"] = "Srinagar"

#2. JSON array >>> looks like a python list
[
    "Python",
    "Java",
    "C++"
]



#array can contain strings, numbers, objects
[
    10,
    20,
    30
]

[
    {
    "name": "Adnan",
    "age": 22
    },
    {
    "name": "Adnan",
    "age": 22
    }
]

#Diff between JSON and python objects
#object - dict, array - list, number - int/float, true - True, false - False, null - None
# this is JSON:
# {
#     "name": "Adnan",
#     "age": 22,
#     "active": true,
#     "phone": null
# }

#this is Python:
{
    "name": "Adnan",
    "age": 22,
    "active": True,
    "phone": None
}


import json

#json.load() >>> json.load() reads JSON from a "file" and converts it into a Python object.
with open("041_students.json", "r") as file:
    file = json.load(file) 
    print(file)
    print(type(file))
    print(file["name"])



#json.loads() >>> json.loads() converts a JSON string into a Python object.
data = '{"name": "adnan", "age": 25}'
student = json.loads(data)
print(student)
print(type(student))
print(student["name"])



student = {
    "name": "Adnan",
    "age": 22,
    "course": "Python"
}

#json.dump() >>> It converts a Python object into JSON and writes it to a file.
with open("041_students1.json", "w") as file:
    json.dump(student, file, indent=4) #indent here is used to create spaces in front of the vaues and the number means how many spaces

#json.dumps() >>> json.dumps() converts a Python object into a JSON string.
json_string = json.dumps(student)
print(json_string)
print(type(json_string))


#NESTED JSON >>> 041_students2.json
with open("041_students2.json", "r") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["address"]["city"])







