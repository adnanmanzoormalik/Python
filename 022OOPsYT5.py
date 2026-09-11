# INHERITANCE >>> code reusablity

class User:     #parent class

    def __init__(self):
        self.name = "Adnan"

    def login(self):
        print("login")

class Student(User):  #child class

    def __init__(self):
        super().__init__() #
        self.roll_no = 12

    def enroll(self):
        return "Enrolled"

u = User()
s = Student()

print(s.name)
print(s.roll_no)
print(s.enroll())


#What gets inherited >>> Constructors, Non private attributes and Non private methods


#CONSTRUCTOR
class Phone:
    def __init__(self, price, brand, camera):
        print ("\nInside phone constructor")
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print ("Buying a phone")

class SmartPhone(Phone): #if a child class doesnt have its own constructor it calls parent constructor
    pass

s=SmartPhone(20000, "Apple", 13)
s.buy()

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, os, ram):
        self.os = os
        self.ram = ram
        print ("\nInside SmartPhone constructor")

s=SmartPhone("Android", 2)
# print(s.brand) #this will throw an error as parent constructor was never called



#ATTRIBUTES >>> child cant access private members of parent class

class Phone:
    def __init__(self, price, brand, camera):
        print ("\nInside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    #getter
    def show(self):
        print (self.__price)

class SmartPhone(Phone):
    def check(self):
        return self.__price

s=SmartPhone(20000, "Apple", 13)
# s.check() this will throw an error as it cnt access private member of parent
print(s.brand)
print(s.show())

