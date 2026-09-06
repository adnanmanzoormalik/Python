# *args >>>  *args allows a function to accept any number of positional arguments. Inside the function, args is a tuple. args is just a commonly used name. The * is what makes it special.

def numbers(*nums):
    print(nums)
numbers(1,2,3)
numbers(1,2,3,4,5)

def squared_nums(*nums):
    for num in nums:
        print(num**2)
squared_nums(1,2,4,5,6,7)
squared_nums(2,5,9,1,5)



# **kwargs >>> **kwargs allows a function to accept any number of keyword arguments. Inside the function, kwargs is a dictionary.

def names(**nm):
    print(nm)
names(first_name = "adnan", middle_name = "manzoor", last_name="malik")

def name_age(**n_a):
    for name, age in n_a.items():
        print(f"{name}: {age}")
name_age(name = "age", adnan = 26, asrar=30)



#local and global variables

#local variables >>> a local variable is a variable which is created inside a function and is accessible inside that funcion only
def greet():
    name = "adnan" #cant be accessed outside of greet()
    return name
print(greet())

#global variable >>> is a variable which is created outside a function and be accessed from inside a function
name = "asrar"
def greet1():
    return name
print(greet1())


#updating global variable inside a function
count = 0
def counter():
    global count #if we dont write global keyword it wont work and will throw an error as it ll consider global as a new varible 
    count += 1
counter()
print(count)


#LAMBA FUNCTIONS >>> lamba function is a small anonymous function

#normal function
def square(num):
    return num**2
print(square(5))

#lambda function
square1 = lambda number: number**2
print(square1(5))

cube = lambda number: number*number*number
print(cube(5))

add = lambda a,b : a+b
print(add(1,2))

odd_even = lambda number: "Even" if number%2==0 else "Odd"
print(odd_even(4))


#Q1. *args - Create a function called find_max() that accepts any number of numbers using *args and returns the largest number.
def find_max(*nums):
    max=nums[0]
    for i in range((len(nums))):
        if nums[i] > max:
            max=nums[i]
    return max
print(find_max(0,1,-1,4,2,3))

#Q2. **kwargs Create a function called show_profile() that accepts any number of keyword arguments and prints them in this format: name: Adnan age: 26 city: Srinagar
def show_profile(**data):
    for key,value in data.items():
        print(f"{key}: {value}")
show_profile(name="adnan", age=26, city="srinagar")

#Q3. Scope - What will the following code print? Try predicting the output before running it.
# x = 10
# def change_value():
#     x = 20
#     print("Inside function:", x)
# change_value()
# print("Outside function:", x)
# Then modify the code so that the global x actually becomes 20.

# output before modifying: 
# Inside function: 20 
# Outside function: 10

x = 10
def change_value():
    global x;
    x = 20
    print("Inside function:", x)
change_value()
print("Outside function:", x)

#Q4. Lambda - Create lambda functions for: Squaring a number. Adding two numbers. Checking whether a number is positive, negative, or zero.

square = lambda number: number**2
print(square(5))

add = lambda a,b: a+b
print(add(2,3))

pos_neg_zero = lambda a: "Positive" if a>0 else "Negative" if a<0 else "Zero"
print(pos_neg_zero(4))
print(pos_neg_zero(-1))
print(pos_neg_zero(0))
