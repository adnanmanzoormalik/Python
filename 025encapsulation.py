#Encapsulation >>> Encapsulation is the practice of bundling data and the methods that operate on that data inside a class, while controlling how that data is accessed or modified.

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

account = BankAccount(10000)
#we dont someone to do account.balance = 0 >>> Encapsulation helps us to control the access of data

#Public attributes can be accesed directly from outside the class like balance 
account.balance = 20000

#Protected Convention >>> Python doesn’t have strict protected access modifiers like some languages. Instead, Python uses a convention: (singleunderscore + variable name) _varname >>> this means This attribute is intended for internal/subclass use. Please don’t access it directly unless you know what you’re doing. we can still access it directly like public attrubutes but we shldnt access it directly

#Private attibutes >>> __varname >>> we cant access private attributes directly outside class instead we access them using methods of the class

class Car:

    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    def get_details(self):
        print(f"{self.__color} {self.__name}")

car1 = Car("BMW", "White")

# print(car1.__color) >>> we cnt do this
car1.get_details()


#name mangling  >>> this means that python changes the private attributes names from __varname to _ClassName__varname and we can access it using this name
print(car1._Car__name)

#NOTE: This means Python doesn’t provide absolute private attributes like some languages. Instead, name mangling makes accidental access/name collisions much harder.


#GETTER >>> A getter is a method used to retrieve/read a private attribute.
#SETTER >>> A setter is a method used to modify/update a private attribute.

class Person:

    def __init__(self, age):
        self.__age = age

    def get_age(self):
        print(self.__age)

    def set_age(self, new_age):
        if new_age>=0:
            self.__age = new_age
        else:
            print("Invalid age")

p1 = Person(25)
p1.get_age()
p1.set_age(26)
p1.get_age()
p1.set_age(-10)

#Above example shows encapsulation + validation >>> we can control what happens to the data like now we cant give any negative value in age


print()




#@property >>> this allows a method to act like an attribute
class Student:

    def __init__(self, age):
        self.__age = age

    @property
    def get_age(self):
        return self.__age

s1 = Student(25)

print(s1.get_age) #we have a method get_age() but we can access it like an attribute thts what @property decorator does


#@property + getter and setter

class Car:
    def __init__(self, name):
        self.__name = name

    @property #provides controlled reading.
    def car_name(self):
        return self.__name

    @car_name.setter #provides controlled modification.
    def car_name(self, name):
        if name:
            self.__name = name
        else:
            print("Invalid name")

car1 = Car("Ferrari")

print(car1.car_name)
car1.car_name = "BMW"
print(car1.car_name)

#Q1 — Encapsulation Basics. Create a class BankAccount with: * account_holder → public * _account_type → protected convention * __balance → private Then: 1. Create an object with "Adnan", "Savings", and 50000. 2. Print the public attribute. 3. Print the protected attribute. 4. Try to access __balance directly. 5. Access __balance using name mangling.

class BankAccount:

    def __init__(self, account_holder, account_type, balance):
        self.account_holder = account_holder
        self._account_type = account_type
        self.__balance = balance

acc1 = BankAccount("Adnan", "Savings", 50000)

print(acc1.account_holder)
print(acc1._account_type)
# print(acc1.__balance) >>> this will cause an error
print(acc1._BankAccount__balance)


#Q2 — Getters, Setters & @property 🔥 Create a class Student with: * name → publi * __marks → private Use @property to get the marks and @marks.setter to set them. Rules: * Marks must be between 0 and 100 * If valid → update marks. * If invalid → print "Invalid marks".

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, marks):
        if marks >= 0 and marks <=100:
            self.__marks = marks
        else:
            print("Invalid marks")

student = Student("Adnan", 85)

print(student.name)
print(student.marks)

student.marks = 95
print(student.marks)

student.marks = 150






