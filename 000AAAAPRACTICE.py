import json

student = {
    "name": "Adnan",
    "age": 20,
    "course": "Python"
}

with open("041_students.json", "w") as file:
    json.dump(student, file, indent=4)

data = json.dumps(student)
print(type(data))