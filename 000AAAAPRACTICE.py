def greet_student(name, greet="Hello", *points, **marks):
    print(greet, name)
    print(f"You have {points} points and {marks} marks")
greet_student("Adnan", "Good Morning", 1,2,3,4, eng=90, maths=91)
