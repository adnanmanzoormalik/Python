#CLOSURE >>> A closure is a function that retains access to variables from its enclosing scope even after the enclosing function has finished executing.

#nested functions >>> function inside a function

def outer():
    def inner(): #only defining a function doesnt call it 
        print("Inner function")
    inner() #without this inner() wont be called
    print("Outer function")
outer()
#inner() #we cant call it like this becoz inner local only inside outer()

#WHY do we use nested function why not just use inner() outside becoz sometimes a function is only useful inside another function. we might nt want it as a global variable

def calculator():
    def add(a, b):
        return a+b
    result = add(1, 2)
    return f"Value calculated: {result}"
print(calculator())


#NOTE: An inner function can access variables from its enclosing/outer function but outer() cannot access inner() variables

#nested functions can call each other

def outer():

    def inner1():
        print("Inner 1 starts and ends")

    def inner2():
        print("Inner 2 starts")
        inner1()
        print("Inner 2 ends")

    inner2()

outer()


#Lexical scope means that a function's access to variables is determined by the function's position in the source code.
# LEGB rule >>> when python encounters a variables it looks in this order Local -> Enclosing -> Global -> Built-in

#Local >>> in the function itself
def outer():
    x = 100
    def inner():
        x = 10
        print(x)
    inner()
outer() #this will print 10

#Enclosing >>> If Python doesn’t find the variable locally, it checks an enclosing function.
def outer():
    x = 100
    def inner():
        print(x)
    inner()
outer() #this will print 100

#Global >>> If Python doesn’t find x locally or in an enclosing function, it checks the global scope.
x = 1000
def outer():
    def inner():
        print(x)
    inner()
outer() #this will print 1000

# Built-in >>> if somthing is not found locally or in enclosing or in global scope it checks in builtin names
def length():
    print(len("adnan")) #we havent defined this len() function so python searched builtin names
length()


#   "nonlocal" keyword >>> The nonlocal keyword tells Python: I don’t want to create a new local variable. I want to use the variable from the nearest enclosing function.

x = 100
def num_out():
    x = 10
    def num_in():
        nonlocal x #this will consider it the closest non local variable i.e inside num_out()
        x=20
        print(x)
    num_in()
    print(x)
num_out()

#we use 'global' keyword when we want to use a variable of global scope and 'nonlocal' when we want to use a variable of enclosing scope
#NOTE: nonlocal cannot refer to a global scope variable

count = 0
def counter():
    global count
    count += 1
counter()
print(count)



#we can store a function in a variable without calling it
def greet():
    print("Greetings")
# a = greet() this will call the function to store we dont have to write the paranthesis
a = greet #now both greet and a refer to the same funtion
print(id(greet), id(a)) #this will print the same address
a() #>>> this will call greet()


#returning a function

def outer():
    def inner():
        print("Inner")
        print(id(inner))
    return inner # >>> this will return the whole inner function

    # return inner() >>> this will call the function and return whatever the inner() returns

x = outer() #>>> this way we can call the outer() and store inner in x
x() #this will call inner
print(id(x)) #this will be same as inner



#practicality of closures
def outer():
    message = "Hello"
    def inner():
        return message
    return inner
a = outer() #this way we can store the value of a variable which is inside outer() >>> The function remembers its enclosing environment. That’s the essence of a closure.
b = a()+" Adnan" #we can now use it as we want
print(b)


#1. Nested function
#         +
# 2. Inner function uses an enclosing variable
#         +
# 3. Inner function survives/escapes the enclosing function
#         =
#        CLOSURE


#closures can have different remembered data
def greet(name):
    def hello():
        print("Hello", name)
    return hello
greet_adnan = greet("Adnan")
greet_asrar = greet("Asrar")
#here we have created two different closure instances


#FUNCTION FACTORY >>> A function that creates customized functions is often called a function factory.

def multiplier(x):
    def multiply(y):
        return x*y
    return multiply
double = multiplier(2)
triple = multiplier(3)
quad = multiplier(4)

print(double(123))
print(quad(6))


# >>> closure with non local
def counter():
    count = 0
    def increment():
        nonlocal count 
        count += 1 #if we dont use nonlocal this will create a new count variable and use that
        return count
    return increment
a = counter()
print(a())




#EXAMPLE exponent
def power(exponent):
    def calculate(number):
        number = number**exponent
        return number
    return calculate

square = power(2)
cube = power(3)

print(square(2))
print(cube(2))

print(square.__closure__)
print(square.__closure__[0].cell_contents)
print(cube.__closure__[0].cell_contents)


#data hiding using closure
def account():
    balance = 1000
    def get_balance():
        return balance
    return get_balance
bal = account()
print(bal())


#validation
def valid_password():
    def length_check(password):
        return len(password) >= 8
    return length_check
password_checker = valid_password()
print(password_checker("12345678"))
print(password_checker("2351hbt"))



#NOTE: Every closure function is a nested function but every nested function is not a closure function

#USES OF CLORSURE FUNCTIONS
# 1. function factory >>> like we created multiplier or power
# 2. maintaining state >>> like we created a counter
# 3. data hiding >>> like account and balance
# 4. validation >>> like password_checker


#closure vs class
pass

