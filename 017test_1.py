 #Question 1 — Student Performance Analyzer ⭐
# Write a Python program that takes the following input:
# • Student name
# • Marks in 5 subjects
# The program should:
# 1. Calculate the total marks.
# 2. Calculate the average percentage.
# 3. Determine the grade:
# • 90+ → A
# • 80–89 → B
# • 70–79 → C
# • 60–69 → D
# • Below 60 → F
# 4. Print whether the student Passed or Failed. A student passes only if:
# • Average ≥ 40
# • AND marks in every subject ≥ 35
# 5. Display the result in a clean format.
# Example Input
# Name: Jasleen
# Enter marks: 85 72 91 66 78
# Expected Output
# Student: Jasleen
# Total: 392
# Average: 78.4
# Grade: C
# Result: PASS

name = input("Enter yoou name: ")
marks = list(map(int,input("Enter marks: ").split()))

print(f"Student: {name}")
total_marks = 0
for mark in marks:
    total_marks += mark
print("Total:",total_marks)

avg_marks_percentage = total_marks/len(marks)

if avg_marks_percentage>90:
    print("Grade: A")
elif avg_marks_percentage>=80:
    print("Grade: B")
elif avg_marks_percentage>=70:
    print("Grade: B")
elif avg_marks_percentage>=60:
    print("Grade: B")
elif avg_marks_percentage<60:
    print("Grade: B")

good_marks = True
for mark in marks:
    if mark < 35:
        good_marks = False
        break

if avg_marks_percentage >= 40 and good_marks:
    print("Result: Pass")
else:
    print("Result: Fail")

