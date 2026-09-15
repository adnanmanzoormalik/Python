#MAGIC METHODS >>> becoz we dont usually directly call them they can be called using +, _, *, /, //, is, print() etc etc
#like when we do print(10) is works as 10.__str__() 
#__init__ __add__ __sub__ __len__ __eq__
#also called as dunder methods becoz they have double underscore


#   __init__    >>> it is usually taught as a constructor

class Person:
    def __init__(self):
        pass
# __new__() creates the object >>> p = Person() is same as p = Person.__new__(Person)
# __init__() initializes the object



# __str__ >>> it tells python how to print the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self): #this tells python how to print the object without it print(p) will throw an error
        return f"{self.name}, {self.age}" # __str__ must always return a string

p = Person("adnan", 25)
print(p) # this works like this p.__str__()



# __repr__() >>> It is related to how an object is represented, especially for debugging/developer-facing output.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student: {self.name}, {self.age}"

p = Person("adnan", 25)
print(repr(p))
#__str__ is human friendly while as __repr__ is developer/debugging friendly


#   __len__

print(len("Adnan")) #this works as "adnan".__len__()


class Person:
    def __init__(self, name):
        self.name = name

    def __len__(self): #must always return an integer
        return len(self.name) 

p = Person("adnan")
print(len(p))



#   __add__() >>> this works with + operator
#   __sub__() >>> this works with - operator
#   __mul__() >>> this works with * operator
#   __truediv__() >>> this works with / operator


class Point:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"({self.a}, {self.b})"

    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Point(self.a - other.a, self.b - other.b)
    
    def __mul__(self, other):
        return Point(self.a * other.a, self.b * other.b)
        
    def __truediv__(self, other):
        return Point(self.a / other.a, self.b / other.b)

    def __floordiv__(self, other):
        return Point(self.a // other.a, self.b // other.b)

p1 = Point(6, 12)
p2 = Point(3, 4)

print(p1)
print(p2)

print(p1+p2)
print(p1-p2)
print(p1*p2)
print(p1/p2)
print(p1//p2)


#COMPARISON MAGIC METHODS
# == __eq__() #when we write == between two objs of our class python doesnt know what to compare so we use __eq__() to tell python what to compare
# != __ne__()
# < __lt__()
# > __gt__()
# <= __le__()
# >= __ge__()

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return self.name != other.name or self.age != other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

p1 = Person("adnan", 26)
p2 = Person("asrar", 30)
p3 = Person("adnan", 26)
p4 = Person("adnan", 27)

print(p1==p2)
print(p1>p3)
print(p3<=p2)
print(p1!=p2)
print(p1==p3)
print(p1>p2)


#   __contains__() >>> this controls the behaviour of "in"
#   __getitem__() >>> this uses indexing to return somthing
#   __setitem__() >>> used to update value of an item using index
class Team:
    def __init__(self, players):
        self.players = players

    def __contains__(self, player):
        return player in self.players

    def __getitem__(self, index): 
        return self.players[index]

    def __setitem__(self, index, player):
        self.players[index] = player

team = Team(["Adnan", "Asrar", "Rayhan"])

print("Adnan" in team)
print(team[2])
team[0] = "Malik"
print(team.players)



# __call__() >>> if we want an object to behave like a function

class Car:
    def __call__(self):
        print("Car is running")

def car():
    print("This is a function")

car() # >>> we havent created the obj of class Car yet so this will call the function car()

car = Car()
car() # NOTE: his treats obj as a function and will take priority over function call()
# we can say this is another form of polymorphism


#   __iter__ and __next__
pass




#   __bool__()  >>>this tells us what happens when an object is used as boolean context

class Student:
    def __init__(self, marks):
        self.marks = marks

    def __bool__(self):
        return self.marks >= 40

s1 = Student(10)
if s1:
    print("Student Passed")
else:
    print("Student Failed")

# Why Magic Methods Are So Powerful >>> They allow your custom classes to feel like native Python objects.

# SUMMARY
# obj() __call__()
# print(obj) __str__()
# repr(obj) __repr__()
# len(obj) __len__()
# obj + other __add__()
# obj - other __sub__()
# obj * other __mul__()
# obj / other __truediv__()
# obj == other __eq__()
# obj != other __ne__()
# obj < other __lt__()
# obj > other __gt__()
# obj[index] __getitem__()
# obj[index] = x __setitem__()
# x in obj __contains__()
# if obj: __bool__()
# for x in obj: __iter__()



#Q1 — Method Overriding + Polymorphism ⭐ Create a parent class Animal with: * name attribute * sound() method that prints: Animal makes a sound Create two child classes: Dog Override sound(): Dog barks Cat Override sound(): Cat meows Then: 1. Create one Dog object and one Cat object. 2. Store both objects in a list. 3. Use a for loop to call sound() on each object.

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

dog = Dog("doggy")
cat = Cat("kitty")

L = [dog, cat]

for animal in L:
    animal.sound()


#Q2 — Duck Typing ⭐⭐ Create three unrelated classes: Dog Robot Person Each class should have a method: speak() They should print different messages: Dog → Woof Robot → Beep Person → Hello There should be no inheritance between the classes. Then create: The function should call the object’s speak() method. make_speak(Dog()) make_speak(Robot()) make_speak(Person())

class Dog:
    def speak(self):
        print("Woof")

class Robot:
    def speak(self):
        print("Beep")

class Person:
    def speak(self):
        print("Hello")

def make_speak(obj):
    obj.speak()

make_speak(Dog()) 
make_speak(Robot()) 
make_speak(Person())
