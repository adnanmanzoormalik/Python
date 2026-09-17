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


#returning value from a wrapper
def decorator(func):
    def wrapper():
        print("Before function")
        result = func()
        print("after function " + result)
        return result
    return wrapper

@decorator
def greet():
    return "Hello"

result = greet()
print(result)


print()

#MULTIPLE DECORATORS >>> we can apply more than one decorator to a function
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        return func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        return func()
    return wrapper

@decorator1
@decorator2
def greet():
    return "Hello"

a = greet()
print(a)




print()


#EXAMPLE >>> EXECUTION ORDER

def dec1(func):
    print("This is dec 1")
    def wrapper1():
        print("This is wrapper 1 start")
        result = func()
        print("This is wrapper 1 end")
        return result
    return wrapper1



#IMPORTANT EXAMPLE
def dec2(func):
    print("This is dec 2")
    def wrapper2():
        print("This is wrapper 2 start")
        result = func()
        print("This is wrapper 2 end")
        return result
    return wrapper2

@dec1 #this basically means dec1(dec2(greet))
@dec2
def greet():
    "This is greet function"
    print("Hello")
    return True

print(greet())



print()



def dec(func_arg):
    def wrap():
        "This is wrapper()" #docstring
        print("Wrapper")
        result = func_arg()
        return result
    return wrap

@dec
def func():
    "This is func()" #docstring
    return "Function"
a = func()
print(a)


#FUNCTION METADATA
# function.__name__ >>> this will return name of function
# function.__doc__  >>> this will return docstring of the function

print(func.__name__) #this will return wrap becoz after decoration func() becomes the wrapper class 
print(func.__doc__) #this will return "This is wrapper"


#functools.wraps
#When you decorate a function, you generally want the decorated function to look like the original function from the outside. That’s what functools.wraps helps us achieve.

from functools import wraps

def decorator(func):

    @wraps(func) #wraps is a decorator and we are using it decorate our wrapper
                 #so it tells python that this is a wrapper func so preserve the metadata from the function
    def wrapper():
        return func()
    
    return wrapper

@decorator
def greet():
    "This is docstring of greet()"
    print("This is greet()")

greet()

print(greet.__name__)
print(greet.__doc__)


print()

#__________EXAMPLES__________

#logging >>> means recording info about our function, useful when debugging applications

def log_function(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"calling ... {func.__name__}")
        print(f"args recieved: {args}")
        print(f"Keyword args: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Returned: {result}")
    return wrapper

@log_function
def add(a, b):
    return a+b

add(1, 2)





print()
#timing decorator
import time
from functools import wraps


def time_counter(func):
    @wraps(func)
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"Time taken to complete {func.__name__} = {end - start:.4f} seconds")
        return result
    return wrapper
@time_counter
def timing():
    time.sleep(2)
    print("timing function")

timing()

#timing functions are useful when we have to call APIs or work with database queries etc



#authentication decorator
from functools import wraps
current_user = None

def login(username):
    global current_user
    current_user = username

def authenticate(func):

    @wraps(func)
    def wrapper():
        if current_user is None:
            print("User doesnt exist")
            return None
        else:
            return func()
    return wrapper

@authenticate
def dashboard():
    print("Welcome to the dashboard")

dashboard()
print()
login("Adnan")
dashboard()






