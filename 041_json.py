# # JSON = JavaScript Object Notation >>> JSON is a text-based data format used to store and exchange structured data. 
# # {
# #     "name": "Adnan",
# #     "age": 22,
# #     "course": "Python"
# # }
# #commonly used in databases, APIs, web apps etc

# # >>> JSON is built around a few basic data types. 

# #1. Json Object >>>A JSON object is basically a collection of key-value pairs. >>>looks like a python dictionary
# {
#     "name": "Adnan",
#     "age": 22
# }
# #keys must be strings
# #we can access them as data["name"] and we can also modify them like data["name"] = "Asrar" and also add a new value dta["city"] = "Srinagar"

# #2. JSON array >>> looks like a python list
# [
#     "Python",
#     "Java",
#     "C++"
# ]



# #array can contain strings, numbers, objects
# [
#     10,
#     20,
#     30
# ]

# [
#     {
#     "name": "Adnan",
#     "age": 22
#     },
#     {
#     "name": "Adnan",
#     "age": 22
#     }
# ]

# #Diff between JSON and python objects
# #object - dict, array - list, number - int/float, true - True, false - False, null - None
# # this is JSON:
# # {
# #     "name": "Adnan",
# #     "age": 22,
# #     "active": true,
# #     "phone": null
# # }

# #this is Python:
# {
#     "name": "Adnan",
#     "age": 22,
#     "active": True,
#     "phone": None
# }


# import json

# #json.load() >>> json.load() reads JSON from a "file" and converts it into a Python object.
# with open("041_students.json", "r") as file:
#     file = json.load(file) 
#     print(file)
#     print(type(file))
#     print(file["name"])



# #json.loads() >>> json.loads() converts a JSON string into a Python object.
# data = '{"name": "adnan", "age": 25}'
# student = json.loads(data)
# print(student)
# print(type(student))
# print(student["name"])



# student = {
#     "name": "Adnan",
#     "age": 22,
#     "course": "Python"
# }

# #json.dump() >>> It converts a Python object into JSON and writes it to a file.
# with open("041_students1.json", "w") as file:
#     json.dump(student, file, indent=4) #indent here is used to create spaces in front of the vaues and the number means how many spaces

# #json.dumps() >>> json.dumps() converts a Python object into a JSON string.
# json_string = json.dumps(student)
# print(json_string)
# print(type(json_string))


# #NESTED JSON >>> 041_students2.json
# with open("041_students2.json", "r") as file:
#     data = json.load(file)
#     print(data)
#     print(data["name"])
#     print(data["address"]["city"])

# #list of dicts
# with open("041_students3.json", "r") as file:
#     students = json.load(file)
#     for student in students:
#         print(student["name"], student["age"])




# #example >>> 041_students4.json
# with open("041_students4.json", "r") as file:
#     students = json.load(file)
#     for student in students["students"]:
#         print(student["name"])

# try:
#     with open("students.json", "r") as file:
#         data = json.load(file)
#         print(data)
# except FileNotFoundError:
#     print("File Not Found")
# except json.JSONDecodeError:
#     print("Invalid Json")


# #Processing API style JSON
# with open("041_apiStyleJson.json","r") as file:
#     data = json.load(file)
#     if data["status"] == "success":
#         print("Users...")
#         for user in data["users"]:
#             print(user["name"])
#         for user in data["users"]:
#             if user["age"] >= 18:
#                 print(f"{user["name"]} is an Adult")

# #Q1 - in students.json
# # 1. Imports the json module.
# # 2. Opens student.json in read mode.
# # 3. Uses json.load().
# # 4. Prints the student’s name.
# # 5. Prints the student’s course.
# # 6. Prints the student’s marks.
# # 7. Prints whether the student passed or failed.
# # 8. The student passes if marks are 50 or above.

# import json
# with open("students.json", "r") as file:
#     data = json.load(file)
#     print(f"Name: {data["name"]}")
#     print(f"Age: {data["age"]}")
#     print(f"Course: {data["course"]}")
#     print(f"Marks: {data["marks"]}")


# #Q2 - Update JSON students.json manually
# # 1. Opens the file using json.load().
# # 2. Finds the student named Ali.
# # 3. Changes Ali’s marks from 62 to 80.
# # 4. Adds a new key "result" to every student.
# # 5. If marks are 50 or above, set "result" to "Pass".
# # 6. Otherwise, set "result" to "Fail".
# # 7. Writes the updated data back to students.json using json.dump().
# # 8. Use indent=4 when writing the JSON.
# import json
# with open("students.json", "r") as file:
#     data = json.load(file)

#     for d in data:
#         if d["name"] == "Ali":
#             d["marks"] = 80
#         if d["marks"] >= 50:
#             d["reslut"] = "Pass"
#         else:
#             d["reslut"] = "Fail"

# with open("students.json", "w") as file:
#     json.dump(data, file, indent=4)


#Q3 - employees.json
# 1. Uses json.load() to read the file.
# 2. Prints the company name.
# 3. Prints the name of every employee.
# 4. Prints only employees belonging to the IT department.
# 5. Calculates the total salary of all employees.
# 6. Finds the employee with the highest salary.
# 7. Calculates the total salary of only the IT employees.
# 8. Prints all employees who have "Python" in their skills.
# 9. Prints the average salary of all employees.


    