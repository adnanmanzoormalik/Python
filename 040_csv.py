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
        if row["age"].strip() == "":
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


#Q1 : Write a Python program that: >>> on students.csv
# 1. Imports the csv module.
# 2. Opens students.csv in read mode.
# 3. Uses csv.reader().
# 4. Skips the header.
# 5. Prints each student’s name, age, and course in this format:
# Adnan - 22 - Python
# Ali - 21 - Java
# Sara - 23 - SQL

import csv
with open("students.csv","r") as file:
    reader = csv.reader(file)
    next(reader, None)
    for row in reader:
        print(f"{row[0]} - {row[1]} - {row[2]}")

#Q2 — Filter CSV Data >>>employees.csv
# Write a Python program that:
# 1. Uses csv.DictReader().
# 2. Reads the CSV file.
# 3. Finds employees whose department is IT.
# 4. Prints their names.
# 5. Calculates and prints the total salary of IT employees.
# Output: 
# Adnan
# Sara
# Total IT Salary: 110000

import csv
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    salary = 0
    for row in reader:
        if row["department"] == "IT":
            print(row["name"])
            salary += int(row["salary"])
    print(f"Total IT Salary: {salary}")


#Write a Python program that: >>> students.csv
# 1. Reads the CSV using csv.DictReader().
# 2. Finds the student named Ali.
# 3. Changes Ali’s marks from 62 to 80.
# 4. Stores the modified rows.
# 5. Rewrites the same CSV file using csv.DictWriter().
# 6. Preserves the header and all other student records.
#>>> after update: 
# name,age,marks
# Adnan,22,75
# Ali,21,80
# Sara,23,88
# John,22,55

students = []
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["name"] == "Ali":
            row["marks"] = 80
        students.append(row)

with open("students.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "marks"]
    writer = csv.DictWriter(file, fieldnames= fieldnames)
    writer.writeheader()
    writer.writerows(students)

#Q4 - Write a Python program that: >>> sales.csv
# 1. Uses csv.DictReader().
# 2. Reads every row.
# 3. Calculates the total value of each product: price × quantity
# 4. Prints each product and its total value.
# 5. Calculates the total sales value of all products.
# 6. Finds the product with the highest total value.
# 7. Calculates the total sales value for the Electronics category only.


with open("sales.csv", "r") as file:
    reader = csv.DictReader(file)
    sales = 0
    elec_sales = 0
    highest_value = 0
    for row in reader:
        total_value = int(row["price"]) * int(row["quantity"])
        print(f"{row["product"]} - {total_value}")
        if highest_value < total_value:
            hvp = row["product"]
            highest_value = total_value
        sales += total_value
        if row["category"] == "Electronics":
            elec_sales += total_value
    print(f"Total Sales: {sales}")
    print(f"Highest Value Product: {hvp}")
    print(f"Electronic sales: {elec_sales}")