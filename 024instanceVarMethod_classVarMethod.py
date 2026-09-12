# Instance variable is a variable that belongs to a particular object (instance).
# Instance variable = variable whose value can be different for each object.
# self Creates/Accesses Instance Variables
# each object has its own instance variable and changing one object's doesnt change other object's

class Person:

    def __init__(self, name, age):
        self.name = name #here name is a paramter and self.name is an onstance variable
        self.age = age

p1 = Person("adnan", 25)
print(p1.name)
print(p1.age)

p2 = Person("asrar", 30)

#instance variables can also be created outside the class
p1.gender = "male" #it is not necessary for all objs to have same or same number of instance variables like p1 has gender but p doesnt
print(p1.gender) 




# A method is simply a function defined inside a class. When that method works with a particular object’s data, it is called an instance method.

class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def get_details(self): #this is an instance method >>> it uses self to know which obj is associated with it
        print(f"{self.model}: {self.color}")

    def change_details(self, new_color): #instance methods can recieve arguments like constructors
        self.color = new_color #Instance Method Can Modify Object Data


car1 = Car("BMW", "Red")
car1.get_details() #obj is calling instance method


#how python passes self >>> the object that calls the method is passed as the first argument. 
#like in above Car class the get_details method recieves self argument i.e the current object when the obj calls it like car1.get_details()


#NOTE: self is not a python keyword we can abc.var_name or xyz.var_name but it is conventional to use self in Python




#Class Attributes >>> A class attribute is a variable that belongs to the class itself, rather than to one particular object. Class attributes are shared by instances unless an instance provides its own attribute with the same name. Class attributes are useful when a value should be common/shared across objects.

class Car:

    car_name = "BMW" #class attribute

    def __init__(self, color):
        self.color = color

print(Car.car_name) #we dont need an obj to access class attribute

car1 = Car("Red")
car2 = Car("Yellow")

#two ways to access class attribute
print(Car.car_name)
print(car1.car_name)



#CHANGING A CLASS ATTRIBUTE

#if we change it like this
car1.car_name = "Ferrari" #this wont change the car_name class attribute but it will create an instance attribute car_namae

print(Car.car_name) #see it is the same
print(car1.car_name) #it is a new obj attribute

Car.car_name = "Mustang"

print(Car.car_name)
print(car1.car_name) #this will print Ferrari becoz it has an instance variable car_name so that will take the proirity
print(car2.car_name)



print()
print()



#class methods >>> A class method operates on the class itself rather than a particular object.

class Student:

    school = "ABC"

    @classmethod #decorator
    def change_school(cls, new_school): #cls here refers to current class like self refers to the current object ||| we can use class methods to change values of class attributes
        cls.school = new_school #class method can access class attributes

    def __init__(self, name):
        self.name = name

print(Student.school)
Student.change_school("XYZ")
print(Student.school)

#we can also use obj to call or access class methods
s1 = Student("Adnan")
print(s1.name)
print(s1.school)
s1.change_school("QWERTY") #here s1 wont pass itself(self) like it used while using instance variables but it will pass class
print(s1.school)


#class method cannot directly access object attributes but there is a way 
class Car:

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_details(cls, car_instance): #this takes obj as an argument
        print(car_instance.name) #now this can access the object attributes

car1 = Car("Maruti")
car1.get_details(car1)



#Q1 — Basic OOP Create a class called Employee with: * A class attribute company = "TechCorp * A constructor that accepts name and salary * Instance attributes name and salary * An instance method display() that prints the employee’s name, salary, and company Then: 1. Create two objects: * Adnan, 50000 * Rahul, 60000 2. Call display() for both objects.

class Employee:

    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"{self.name}, {self.salary}, {self.company}")

emp1 = Employee("Adnan", 50000)
emp2 = Employee("Rahul", 60000)

emp1.display()
emp2.display()


#Q3 

class Student:

    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age, self.school)

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


student1 = Student("Adnan", 26)
student2 = Student("Rahul", 24)

student3 = student1

student1.age = 27

Student.change_school("XYZ School")

student3.name = "Aman"

student1.display() #Aman, 27, XYZ School
student2.display() #Rahul, 24, XYZ School
student3.display()