#METHOD OVERRIDING: the process in which a child class provides its own implementation of a method that is already defined in its parent class.

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog:
    def eat(self):
        print("Animal is eating")

dog = Dog()
dog.eat() #this ll execute the child's eat()

#this happen when the parent and the child class have a method with same name
#this happens becoz parent provides a general behaviour but the child provides a specific behaviour


# WHAT ACTUALLY HAPPENS

# Dog
#  ↓
# Does Dog have sound()? → YES
#  ↓
# Execute Dog.sound()

# Dog
#  ↓
# Does Dog have sound()? → NO
#  ↓
# Check Parent
#  ↓
# Does Parent have sound()? → YES
#  ↓
# Execute Parent.sound()


# NOTE: Method Overloading
# Traditionally means having multiple methods with the same name but different parameters.
# Python doesn’t support traditional method overloading in the same way as languages like Java/C++.


#super(): used inside a child class to access methods from its parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        super().sound() #this will call parents sound() method
        print("Dog barks")




#using super() to call parent constructor

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self,name, marks):
        super().__init__(name) #without this it will throw an error becoz parent __init__ will never get called as child constructor will override it
        self.marks = marks

stu = Student("adnan", 25)
print(stu.marks, stu.name)

#Case 1 — Child has no __init__() >>> Parent constructor is inherited.
#Case 2 — Child has its own __init__() >>> The parent constructor is not automatically called just because the child has its own constructor.
#Case 3 — Child has its own constructor + super() >>> like in the above example first child constructor will be called and then from inside of that parent constructor will be called





#Question 1 — Single Inheritance - Create a class Person with: * name attribute *age attribute *introduce() method that prints: My name is Adnan and I am 22 years old. Then create a child class Student that inherits from Person. Student should have its own method: study() which prints: Adnan is studying. Requirements: 1. Create a Student object with "Adnan" and 22. 2. Call the inherited introduce() method. 3. Call the child’s study() method.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

class Child(Person):
    def study(self):
        print(f"{self.name} is studying.")

s1 = Child("Adnan", 22)
s1.introduce()
s1.study()


#Question 2 — Method Overriding + super() - Create a parent class Animal with: make_sound() that prints Animal makes a sound Create a child class Dog that: * Inherits from Animal * Overrides make_sound() * Uses super() to call the parent’s make_sound() * Then prints: Dog barks

class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()
        print("Dog barks")

dog = Dog()
dog.make_sound()





