#CSV = Comma-Separated Values A CSV file stores data in rows and columns. they use .csv extension
# name,age,course
# Adnan,22,Python
# Ali,21,Java
# Sara,23,SQL

#Python provides a built-in csv module. >>> import csv


#csv.reader()
import csv
with open("040_students.csv","r") as file:
    data = csv.reader(file)
    for row in data:
        print(row)
#csv values are read as strings >>> so age : 20 will be read as "20" not 20 
#if we want them as number we can do
    # next(data, None) #to skip header row
    # for row in data:
    #     print(int(row[1]))



#csv.write() >>> mode="w" >>> replaces all the data with the new data
with open("040_students.csv", "w", newline="") as file: #newline helps prevent unwanted blank lines
    writer = csv.writer(file)
    writer.writerow(["name", "age", "course"])
    writer.writerow(["Asrar", 25, "Python"])
    writer.writerow(["omais", 22, "SQL"])

#we can also do it this way
rows = [
    ["abc", 24, "Java"],
    ["xyz", 28, "Python"]
    ]
with open("040_students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(rows)


# mode = "a" >>> add new data in the end of old data
with open("040_students.csv", mode="a", newline="") as file: 
    writer = csv.writer(file)
    writer.writerow(["Sara", 21, "Java"])
    writer.writerow(["Ali", 32, "JS"])


#csv.DictReader() >>> read every row as a dictionary
with open("040_students.csv", "r") as file:
    d_reader = csv.DictReader(file)
    for row in d_reader:
        print(row)

#csv.DictWriter()
with open("040_students.csv", "a", newline="") as file:
    fieldnames = ["name", "age", "course"]
    d_writer = csv.DictWriter(file, fieldnames=fieldnames)
    d_writer.writerow({
        "name" : "Jazz",
        "age" : 22,
        "course" : "AI"
        })

#headers >>> they describe the columns

#in csv.writer() >>> we simply make the header as >>> writer.writerow("name", "age", "course")

#in csv.DictWriter() >>> writer.writeheader() and NOTE: delimiter
with open("040_students1.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter="|")
    writer.writeheader()
    writer.writerow({
            "name": "Adnan",
            "age": 25,
            "city" : "Srinagar"
        })
    writer.writerow({
                "name": "Adnan",
                "age": 25,
                "city" : "Srinagar"
            })
    writer.writerow({
                "name": "Adnan",
                "age": 25,
                "city" : "Srinagar"
            })


with open("040_students1.csv", "r", newline="") as file:
    reader = csv.reader(file, delimiter="|") #this wont print delimiter it ll just treat | as a seperator between the columns
    for row in reader:
        print(row)


with open("040_students.csv", "r") as file:
    data = csv.reader(file, delimiter=";") #this wont do anything because in the csv file we have used commas so it ll just think that the whole row is 1 column
    for row in data:
        print(row)


#quotchar >>> sometimes we have data as Srinagar, Kashmir in a single column address so we use quotechar to help python understand that it is a single element 
# >>> reader = csv.reader(file, quotechar='"') we dont usually need to mention as it is default
# NOTE: Practice this once



#handling missing values
with open("040_students2.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
            "name": "Adnan",
            "age": 25,
            "city" : "Srinagar"
        })
    writer.writerow({
                "name": "Adnan",
                "city" : "Srinagar"
            })
    writer.writerow({
                "name": "Adnan",
                "age": 25,
                "city" : "Srinagar"
            })

with open("040_students2.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        if row["age"] == "":
            print("Age missing")

# or we can do it this way


with open("040_students2.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["age"] == "":
            row["age"] = "Unknown"
        print(row)


#Filtering CSV data
with open("040_students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["course"] == "Python":
            print(row["name"])


#updating csv data
rows = []
with open("040_students2.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["name"] == "Adnan":
            row["age"] = 30
        rows.append(row)

with open("040_students2.csv", "w") as file:
    fieldnames = ["name", "age", "city"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)



#You can convert CSV data into Python structures.

#list of dictionaries
students = []

with open("040_students2.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append(dict(row)) #without using dict it be a string
print(students)

# we can also do this
students1 = []
with open("040_students2.csv", "r") as file:
    reader = list(csv.DictReader(file))
    students1.extend(reader) #if we use append here it will become a nested list but extends breaks the inner list and puts values as dicts
print(students1)



#list of lists
# students2 = []
with open("040_students1.csv", "r") as file:
    reader = csv.reader(file, delimiter="|")
    global students2
    students2 = list(reader)
print(students2)


#large datasets
#we should not use >>> reader = list(csv.reader(file)) >>> it will process all the data at once and put pressure on the ram
#so we do this
with open("large.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader: #this will read one row at a time
        if row["age"]:
            age = int(row["age"])
            if age >= 18:
                print(row["name"])