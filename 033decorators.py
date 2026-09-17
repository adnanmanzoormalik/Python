#_________________________DECORATORS_________________________

#function are firstclass objects in python i.e function can be treated as an object in python
# Store a function in a variable
# Pass a function as an argument
# Return a function from another function
# Store functions in lists/dictionaries/etc.

#Storing a function in variable
def greet():
    return "Hello"
a = greet
print(a())


#functions are objects
print(type(greet)) #this prints <class 'function'> that means greet belongs to class function so it is an object


#passing functions as arguments
def exec(func):
    print(func())
exec(greet)


#another example
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def calculate(a, b, func):
    print(func(a,b))

calculate(1,2, add)
calculate(3,2,sub)


#there is a difference between calling and pass a function
#exec(func)     >>> this is pass a function as an argument
# exec(func())     >>> this is calling the function func and the value it returns is passed to exec()

#a function can also return another function >>> we studied this in closures
def func1():
    def func2():
        return "This is func2"
    return func2
a = func1()
print(a())


#COMBINE PASSING AND RETURNING A FUNC
def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

def greet():
    print("HELLO")

a = decorator(greet)
a()


print()

#A decorator is a function that takes another function, adds or modifies behavior, and returns a function that replaces the original function. The decorator usually wraps the original function rather than changing its source code.


def checking(func):
    def check():
        print("Processing....")
        func()
        print("Process completed\n")
    return check

def log_in():
    print("User logged in")

def log_out():
    print("User logged out")

login = checking(log_in)
logout = checking(log_out)

login()
logout()


#example >>> manually calling a decorator
def decorator(func):
    def wrapper():
        func()
        print("How are you\n")
    return wrapper

def m_greet():
    print("Good morning")

m_greet = decorator(m_greet)
m_greet()




#decorator syntax
@decorator #if we use this we dont have to write e_greet = decorator(e_greet)
def e_greet():
    print("Good Evening")
e_greet()






# *args in a decorator
def greeter(func):
    def wrapper(*args): #if we dont use *args here python will give error that wrapper accepts 0 positional args but 1 was given
        func(*args)
        print("How are you?")
    return wrapper

@greeter
def greet(name):
    print(f"Hello, {name}")

greet("Adnan")

#Multiple positional arguments
def calculator(func):
    def wrapper(*args):
        print("Processing...")
        result = func(*args)
        print(result)
    return wrapper

@calculator
def add(a, b):
    return(a+b)

add(1,2)





# **kwargs
def greeter(func):
    def wrapper(**kwargs):
        func(**kwargs)
        print("How are you?")
    return wrapper

@greeter
def greet(name, id):
    print(f"Hello, {name} ({id})")

greet(name="Adnan", id=12213125)



# *args and **kwargs together

def decor(func):
    def wrap(*args, **kwargs):
        print("processing")
        func(*args, **kwargs)
    return wrap

@decor
def add(a,b, type):
    print(f"{type} sum: {a+b}")

add(1, 2, type="Integer")


