#Dataclasses: 


#we normally write
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
emp1 = Employee("Adnan", 25)
emp2 = Employee("Adnan", 25)
print(emp1.name)
print(emp1.age)



#we using dataclass we do it in a much cleaner way
from dataclasses import dataclass

@dataclass
class Student:
    name : str #Inside a dataclass, we define fields using type annotations, These annotations describe what type of data the field is expected to contain.
    age : int 
    #this is writing the same as def __init__(self, name, age):
                                #       self.name = name
                                #       self.age = age
                                # also __repr__() and __eq__()
    #python writes the remaining code for us

s1 = Student("Asrar", 30)
s2 = Student("Asrar", 30)
print(s1.name)
print(s1.age)



print(emp1) #this will print: <__main__.Employee object at 0x104992900>
print(s1) #this will print: Student(name='Asrar', age=30) becoz @dataclass automatically generates __repr__() method

print(emp1 == emp2) #this will print False
print(s1 == s2) #this will print True becoz @dataclass automatically creates an __eq__() method that compares the fields


#Default values
from dataclasses import dataclass

@dataclass
class Person:
    name : str
    age : int
    city : str = "Srinagar" #fields without defaults must come before fields with defaults

p1 = Person("Adnan", 25)
print(p1)

#NOTE: Dataclass doesn’t mean “better class in every situation.” Use a dataclass when the main purpose of the class is to represent/store structured data. But if your class has complex behavior, lots of custom logic, inheritance, validation, etc., a normal class may sometimes be more appropriate.


#COMPARISON EXAMPLE

class Cars:

    def __init__(self, brand, t_spd, color):
        self.brand = brand
        self.t_spd = t_spd
        self.color = color

    def __repr__(self):
        return f"Cars(brand='{self.brand}', t_spd={self.t_spd}, city='{self.color}')"

    def __eq__(self, other):
        return (
            self.brand == other.brand and
            self.color == other.color and
            self.t_spd == other.t_spd
        )

car1 = Cars("BMW", 300, "Blue")
car2 = Cars("BMW", 300, "Blue")
print(car1)
print(car1==car2)


from dataclasses import dataclass

@dataclass
class Cars:
    brand : str
    t_spd : int
    color : str

car3 = Cars("Ferrari", 350, "Red")
car4 = Cars("Ferrari", 350, "Red")
print(car3)
print(car3 == car4)



#we cant keep mutable objects >>> list or dictioanries as default values in dataclasses.
#lets say we try to keep a list as a default value it ll throw an error >>> ValueError: mutable default <class 'list'> for field subjects is not allowed >>> becoz Because Python doesn’t want multiple objects accidentally sharing the same mutable default object.
#suppose we make 2 objs as s1 and s2 with a list 'subs' as default value and we make changes in s1 as s1.subs.append("DSA") >>> but since both the objects share the same list, changes will also be made in s2

#field(default_factory=...) >>> this is how we solve this problem >>> 

from dataclasses import dataclass, field

@dataclass
class Student:
    name : str
    age : int
    subjects : list = field(default_factory = list) #this way each obj gets a seperate list

s1 = Student("Adnan", 25)
s2 = Student("Asrar", 30, {"java"})
print(s1)
print(s2)

s1.subjects.append("Python")
print(s1)

#default_factory with dictionaries
@dataclass
class Person:
    name : str
    marks : dict = field(default_factory = dict)

p1 = Person("Adnan", {"Python":98})
p2 = Person("Asrar")

print(p1)
print(p2)
p2.marks["Java"] = 78
print(p2)

@dataclass
class Phone:
    name : str
    size : float

ph1 = Phone("Nokia", 6.0)
print(ph1)
ph1.name = "Motorola" #this shows out object data is mutable
print(ph1)

#lets suppose we make changes to it which we didnt want >>> like we want to create an immutable object

#FROZEN Dataclasses >>> when we create an obj we wont be able to make changes after that

@dataclass(frozen=True)
class Printer:
    name : str
    model : int

pr1 = Printer("Epson", 3041)
print(pr1)
# pr1.name = "Canon"    >>> this will throw an error "FrozenInstanceError"


#Frozen dataclasses are useful when you want objects representing data that should not change.

@dataclass(frozen=True)
class Point:
    x : int
    y : int

point1 = Point(2, 3)
#point1.x = 10 >>> we wouldnt accidently want this to happen, The frozen dataclass prevents that reassignment.


from dataclasses import dataclass, asdict, astuple

@dataclass
class Person:
    name : str
    age : int
    course : str

p1 = Person("Adnan", 25, "CSE")

data_as_dict = asdict(p1) #this is useful when working with JSON, APIs, databases etc
#we can convert out dict in json data
import json
json_data = json.dumps(data_as_dict)
print(json_data)


data_as_tuple = astuple(p1)

print(data_as_dict)
print(data_as_tuple)