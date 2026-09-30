# # Debugging is the process of finding, understanding, and fixing errors (bugs) in a program.
# # A bug is a problem in your program that causes it to:
# # * crash
# # * produce an incorrect result
# # * behave unexpectedly
# # * stop working at a particular point

# # Error: Something is wrong with your program.
# # Debugging: The process of finding and fixing that problem.



# #types of errors: 

# # 1. Syntax error: A syntax error occurs when Python cannot understand the structure/syntax of your code. A syntax error usually prevents the program from starting properly.
# # if True <missing :>
# #   print(10)
# # print(10 <missing )>


# # 2. Runtime Errors: A runtime error occurs while the program is actually running. The syntax is valid, so Python can start the program. But something goes wrong during execution.
# # print(10/0) >>> division by zero error
# # age = int("Hello") >>> invalid conversion
# # l = [1,2,3]
# # print(l[10]) >>> index out of bounds


# # 3. Logical errors are often the hardest type of error because the program runs without crashing. The code is syntactically valid. The program executes. But the result is wrong.
# a = 10
# b = 20
# print(a+b) # >>> this will execute but we wanted a-b



# #Reading traceback: When Python encounters a runtime error, it usually gives you a traceback. A traceback is Python’s report showing: How the program got to the point where the error occurred and what error happened.

# # def divide(a, b):
# #     return a / b
# # def calculate():
# #     result = divide(10, 0)
# #     print(result)
# # calculate()
# #the above code will print this in terminal>>>
# # Traceback (most recent call last):
# #   File "/Users/adnanmanzoor/Python/047_debugging.py", line 42, in <module>
# #     calculate()
# #   File "/Users/adnanmanzoor/Python/047_debugging.py", line 40, in calculate
# #     result = divide(10, 0)
# #   File "/Users/adnanmanzoor/Python/047_debugging.py", line 38, in divide
# #     return a / b
# # ZeroDivisionError: division by zero


# #print() Debugging

# #basic code
# def calculate(a, b):
#     print(a+b)
# calculate(2,3)

# #lets say we suspect a bug >>> we ll do this
# def calculate(a,b):
#     print("calculate() started...")
#     print(f"a = {a}")
#     print(f"b = {b}")
#     print("result: ", a+b)
#     print("calculate() ended...")

# print("calling calculate()...")
# calculate(2,3)
# print("program ended...")



# #pdb >>> Python Debugger. It’s Python’s built-in interactive debugger. Unlike print(), pdb allows you to pause the program and inspect it while it is running. 
# # You can pause execution, inspect variables, execute the next line, enter functions, leave functions, continue execution
# # p variable: Print/inspect variable
# # n: Next line
# # c: Continue execution
# # q: Quit debugger
# # l: Show surrounding source code
# # s: Step into function
# # r: Continue until current function returns

# import pdb

# x = 10
# y = 20
# # pdb.set_trace()
# result = x+y
# print(result)

# #this is terminal example
# # > /Users/adnanmanzoor/Python/047_debugging.py(83)<module>()
# # -> result = x+y
# # (Pdb) p x
# # 10
# # (Pdb) p y
# # 20
# # (Pdb) n
# # > /Users/adnanmanzoor/Python/047_debugging.py(84)<module>()
# # -> print(result)
# # (Pdb) p result
# # 30



# #breakpoint() : A breakpoint is a point where you tell the debugger: “Pause the program here.” Instead of running the entire program at once, execution stops at the breakpoint so you can inspect what’s happening.
# # Imagine a program with 500 lines. Something goes wrong around line 350. You don’t want to inspect every line manually. You can place a breakpoint around the suspicious area. and then inspect the area

# # Breakpoints in VS Code >>> red dot on left side of line >>> When you run the debugger, execution pauses there.
## ▶ Continue
## ↷ Step Over
## ↓ Step Into
## ↑ Step Out

# a = 10
# b = 20
# breakpoint()
# result = a+b
# print(result)

# #Step Over: Once your program is paused, you can execute one line at a time. This is called Step Over.
# #it wont enter the function >>> n
# # Step Into means: Enter the function being called and debug it line by line. >>> s
# # Step Out means: Finish the current function and return to the line where the function was called. >>> r

# def cal(a, b):
#     res = a+b
#     return res
# a = 10
# b = 20
# breakpoint()
# print(cal(a, b))


# name = "Adnan"
# age = 22
# scores = [80, 90, 75]
# breakpoint()
# average = sum(scores) / len(scores)
# #inspecting variables: (Pdb) p variable
# #inspecting expressions: (Pdb) p len(scores)
# #                       (Pdb) p sum(scores)
# #                       (Pdb) p sum(scores)/len(scores
# #inspecting types: (Pdb) p type(age)




## 14. DEBUGGING FUNCTIONS
## When debugging a function, check:
## 1. Function arguments
## 2. Argument data types
## 3. Intermediate variables
## 4. Return value
## 5. How the returned value is being used

# # Example:
# def calculate_total(price, quantity):
#     total = price + quantity
#     return total
# # The code runs, but the logic is wrong.
# # Correct:
# def calculate_total(price, quantity):
#     total = price * quantity
#     return total

# # Useful debugging:
# # print(price)
# # print(quantity)
# # print(type(price))
# # print(type(quantity))
# # print(total)

# # Using breakpoint():
# def calculate_total(price, quantity):
#     breakpoint()
#     total = price * quantity
#     return total
# calculate_total(100, 10)
# # Inside pdb:
# # p price
# # p quantity
# # p type(price)
# # n



# 15. DEBUGGING FILE OPERATIONS
# Common file-related problems:
# - Wrong filename
# - Wrong file path
# - File doesn't exist
# - Wrong file mode
# - Incorrect encoding
# - Unexpected file contents
# - Incorrect data type after reading

# Example:
with open("039_data.txt", "r") as file:
    numbers = file.readlines()

# Debug:
# print(numbers)
# print(type(numbers))
# print(len(numbers))

# For checking a path:
#Using os
import os
print(os.path.exists("039_data.txt"))
# Using pathlib:
from pathlib import Path
path = Path("039_data.txt")
print(path.exists())

# Important: Data read from a file is usually a string.
# Example:
path = "039_data.txt"
from pathlib import Path
path_exists = Path(path)
print(path)
with open("039_data.txt", "r") as file:
    number = file.read()
# print(number)
# print(type(number))

# If the file contains: 25
# Python reads it as: "25"
# Convert it if necessary: number = int(number)

