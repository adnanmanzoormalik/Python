#FUNCTIONS >>> A function is a reusable block of code that performs a specific task.

def greet(): #creating a function
    print("Hello World")
greet() #calling a function

#function with parameters
def greet1(name): #here name is parameter
    print(f"Hello, {name}")
greet1("Adnan") #here "Adnan" is argument >>> The values we pass while calling the function are called arguments.
greet1("Asrar")

#multiple parameters
def add(num1, num2, num3):
    print("ADD:", num1+num2+num3)
add(1,2,3)
add(3,4,5)

#The return statement sends a value back from a function.

def add_nums(a,b):
    return a + b
print(add_nums(1,2))

def square(a):
    return a**2
sq_2 = square(2)
print(sq_2)

#function can return different data types almost any python value
def str1():
    return "Adnan"
print(str1())

def list1():
    return [1,2,3,4,5]
print(list1())

def dict1():
    return {
        "adnan" : "name",
        "age" : 26
    }
print(dict1())


#returning multiple values
def cal(a, b):
    return a+b, a-b
addition, subtraction = cal(3,2)
print(addition, subtraction)

# return stops a function
def stop():
    print("before")
    return "done"
    print("after")
print(stop())

#Default Arguments: A default argument gives a parameter a value that will be used automatically if you don't provide an argument.
def def_arg(name, greet="Hello, "):
    print(greet, name)
def_arg("adnan")
def_arg("adnan", "good morning")
#NOTE: def args always come after reqd args

def def_arg1(name="User", greet="Hello"):
    print(greet, name)
def_arg1()
def_arg1("Adnan", "Good Morning")
def_arg1("adnan")

#POSITIONAL ARGS and KEYWORD ARGS
def func1(name, age, city):
    print(name, age, city)
func1("Adnan", 26, "Srinagar") #positional args

def func2(name, age, city):
    print(name, age, city)
func2(age=26, name="Adnan", city="Srinagar") #keywords args

def func3(name="adnan", age=26, city="sgr"):
    print(name, age, city)
func3("asrar", city="sgr") #NOTE: positional args are needed to be put before keyword args

# *args >>>allows a function to take any number of positional args
def args1(*numbers):
    print(numbers) # *args are printed as a tuple
args1(1,2,3,4)
args1(3,6,8,9)

# **kwargs >>>allows a function to take any number of keyword args
def kwargs1(**data):
    print(data) # **kwargs are printed as a dict
kwargs1(name="Adnan", age=26)
kwargs1(name="Adnan", city="srinagar", age=26)

def kwargs2(**data):
    for key, value in data.items():
        print(key,":",value)
kwargs2(name="adnan", age=26)

def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
args_kwargs(1,2,3,4,5,name="adnan", age=26, city="srinagar")

#NOTE: when we use diff types of parameters >>> this is the paramter order
def example(required, default="value", *args, **kwargs):
    pass

def example1(name, age=26, *points, **marks):
    print("Hello",name,age,"Points:",points,marks)
example1("Adnan",2,3,4, py=20, java=100)

#local and global variable >>>local only works inside function, global works outside as well as inside function but if we want to change/update it inside function use keyword "global" otherwise a new variable will be created
name = "adnan"

def local_var():
    name = "asrar"
    print(name)
local_var()
print(name)

def local_var():
    global name 
    name = "asrar"
    print(name)
local_var()
print(name)

# a function can call other functions as well

def func_a(a):
    return a*a
def func_b(b):
    print(func_a(b)*b)
func_b(4)

# Q1. Student Introduction Function - Create a function called student_info() that: Accepts name, age, and city Has a default value of "Python" for a parameter called course Returns a sentence containing all the information Then: Store the returned value in a variable Print the variable Call the function once using keyword argument
def student_info(name, age, city, course="Python"):
    return (f"{name} is {age} years old lives in {city}, and is learning {course}")
var1 = student_info(name = "adnan", city="srinagar", age=26)
print(var1)

# Q2. Flexible Number Calculator Create a function called calculate_sum() that: Accepts any number of positional arguments using *args Returns their total using sum() Example: calculate_sum(10, 20, 30) Should return: 60 Also try calling it with different numbers of arguments.
def calculate_sum(*nums):
    return sum(nums)
print(calculate_sum(10,20,30))
print(calculate_sum(3,4,2,1,7))

#Q3. Flexible Profile Creator Create a function called create_profile() that: Accepts a required name parameter Accepts any number of additional keyword arguments using **kwargs Prints the name Uses a loop to print all additional details
def create_profile(name, **data):
    print(name)
    for key,value in data.items():
        print(key,":",value)
create_profile("Adnan", Age="26", City="Srinagar")