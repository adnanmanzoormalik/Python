import csv
with open("040_students2.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["age"] == "":
            row["age"] = "Unknown"
        print(row)