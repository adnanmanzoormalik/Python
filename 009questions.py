# #Q1. Create a program that stores your: Name, Age, City. Then print a sentence using an f-string, such as: My name is Adnan, I am 20 years old and I live in Srinagar.

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")
# print(f"My name is {name}, I am {age} years old and I live in {city}")

# #Q2. Simple Calculator: Take two numbers from the user and print: Addition, Subtraction, Multiplication, Division, Remainder

# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(f"Addition: {num1 + num2}")
# print(f"Subtraction: {num1 - num2}")
# print(f"Multiplication: {num1 * num2}")
# print(f"Division: {num1 / num2}")
# print(f"Remainder: {num1 % num2}")

# #Q3. Data Type Explorer: Create five variables containing: A string, An integer, A float, A Boolean, None. Print the value and data type of each variable.
# str1 = "Adnan"
# int1 = 10
# float1 = 10.22
# boolean1 = True
# Nonetype1 = None

# print(str1)
# print(type(str1),"\n")

# print(int1)
# print(type(int1),"\n")

# print(float1)
# print(type(float1),"\n")

# print(boolean1)
# print(type(boolean1),"\n")

# print(Nonetype1)
# print(type(Nonetype1),"\n")

# # Q4. Even or Odd: Ask the user for a number and determine whether it is even or odd.
# num1 = int(input("Enter a number: "))
# if num1 % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

# # Q5. Positive, Negative, or Zero: Ask the user to enter a number. Print whether the number is: Positive, Negative, Zero
# num1 = int(input("Enter a number: "))
# if num1>0:
#     print("Positive")
# elif num1<0:
#     print("Negative")
# else:
#     print("Zero")

# #Q Smart Calculator: Create a calculator that: Takes two numbers from the user. Shows this menu: 1. Addition, 2. Subtraction, 3. Multiplication, 4. Division, 5. Remainder, 6. Power, Ask the user to select an operation., Use match-case to perform the operation., Handle invalid choices., Prevent division by zero.

# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Remainder \n6. Power")

# opt_num = int(input("Select a number to perform the operation: "))

# match opt_num:
#     case 1:
#         print(a+b)
#     case 2:
#         print(a-b)
#     case 3:
#         print(a*b)
#     case 4:
#         if b != 0:
#             print(a/b)
#         else:
#             print("Cant be divided by zero")
#     case 5:
#         print(a%b)
#     case 6:
#         print(a**b)
#     case _:
#         print("Invalid selection")