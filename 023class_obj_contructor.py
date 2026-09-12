# Python Day 4 Part 1 Classes, objects, constructors, reference variable

#class >>> blueprint of an object >>> we used PascalCase naming convention for classes like Student, CarDetails, AdnanManzoor
class Student:
    pass

#object >>> an actual instance of a class
stu = Student() #>>> this () means create obj of this class and stu is a variable which stores refrence of the object created

#NOTE: The class defines the general structure. The objects are individual instances created from that class.

#The class defines the general structure.The objects are individual instances created from that class.
stu.name = "Adnan"
stu.age = 25 #With objects, we also use . to access things belonging to the object. This is called dot notation

#Objects don't just contain data. They can also have behavior. In OOP, functions defined inside a class are called methods.


#refrence variable
stu1 = Student() #Student() creates an obj and stu1 stores the refrence value of the object
stu2 = stu1 #we can have various ref vars >>> stu1 and stu2 both point to the same object


#CHECKING TYPE OF AN OBJECT
print(type(stu1)) #this will return stu1 refers to the object of class Student


#Checking Whether Something is an Instance
print(isinstance(stu,Student))


print()
print()


#CONSTRUCTOR >>> A constructor __init__ is a special method (magic method) that is used to initialize an object when it is created. It doesnt need to be called, it is called automaically. It is also called as dunder init

class Car:

    def __init__(self):
        print("inside contructor")

car1 = Car()


#Parameterized constructor
class Car:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_details(self):
        print(self.name, self.color)

car1 = Car("BMW", "Red")
print(car1.color)
print(car1.name)
car1.get_details()


#self 
class Car:
    def __init__(self, name, color):
        self.name = name    #self refers to the current object >>> lets say we make an object obj1 at that time self will refer to obj1 and while using obj2 self will refer to obj2
        self.color = color

obj1 = Car("Ferrari", "Red") #>>> when we create this object it send some values to the constructor which has parameters self, name, color >>> but we are sending only two name and color but here obj1 is sent as self 

#in the constructor we cant use name = name instead of self.name = name it will not create obj attributes it ll b just a local variable


#Constructor with default values: 

class Person:

    def __init__(self, name="User", greet="Hello"):
        self.name = name
        self.greet = greet

    def get_details(self):
        print(f"{self.greet}, {self.name}")

p1 = Person("Adnan", "Good Morning")
p2 = Person()

p1.get_details()
p2.get_details()

#NOTE: __init__ doesnt create an obj it initializes an already created obj


#Q: Basic Constructor Create a class called Car. The constructor should accept: brand model price Store them as object attributes. Then create: Car 1 → Toyota, Camry, 3000000 Car 2 → Honda, City, 1500000 Print all attributes of both objects.

class Car:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_details(self):
        print(f"{self.brand}, {self.model}, {self.price}")

car1 = Car("Toyota", "Camry", 3000000)
car2 = Car("Honda", "City", 1500000)

car1.get_details()
car2.get_details()