#ABSTRACTION: Abstraction means hiding implementation details and showing only the essential functionality.

#An abstract class is a class that is designed to be a blueprint for other classes. It generally defines what subclasses must do, without providing all the implementation itself.

from abc import ABC, abstractmethod
class Animal(ABC): #ABC is abstract base class inheriting it means Animal is an abstract class

    @abstractmethod #>>> this is a decorator that tells python Every concrete child class must provide an implementation of this method. An abstract method is a method that is declared in the abstract class but is intended to be implemented by child classes. it tell us that every concrete base class must implement sound method
    def sound(self):
        pass

    def eat(self): #abstract class can have normal methods as well
        print("Animal eats")


class Dog(Animal):
    def sound(self): #if we dont implement sound() here it will throw a typeError
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

#we can also do this >>> polymorphism i think
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()
    animal.eat()

#NOTE: Encapsulation hides the data and abstraction hides the implementation complexity

#USES
#1. Reduces complexity
#2. Forces consistency
#3. Makes code easier to maintain
#4. Supports polymorphism
#5. Helps large projects

#EXAMPLE
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class Upi(Payment):
    def pay(self, amount):
        print(f"{amount} paid successufully using UPI")

class Card(Payment):
    def pay(self, amount):
        print(f"{amount} paid successfully using card")

upi1 = Upi()
card1= Card()

upi1.pay(4000)
card1.pay(3500)


#Q4 — Abstraction with Abstract Class ⭐
# Create an abstract class Shape.
# Requirements:
# 2. The Shape class should have an abstract method called area().
# 3. Create a child class Circle that inherits from Shape.
# 4. Circle should have a radius attribute.
# 5. Implement the area() method in Circle using the formula:
#     π × radius²
# 6. Create another child class Rectangle that inherits from Shape.
# 7. Rectangle should have length and width attributes.
# 8. Implement the area() method in Rectangle using the formula:
#     length × width
# 9. Create one Circle object and one Rectangle object.
# 10. Call the area() method for both objects.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        c_area = 3.14 * self.radius**2
        print(f"Area of circle: {c_area}")

class Rectangle(Shape):

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        r_area = self.length * self.breadth
        print(f"Area of rectangle: {r_area}")

c1 = Circle(5)
r1 = Rectangle(2,4)
c1.area()
r1.area()


# Q5 — Abstraction + Polymorphism
# Using the Shape, Circle, and Rectangle classes from Q4:
# 1. Create one Circle object.
# 2. Create one Rectangle object.
# 3. Store both objects inside a list called shapes.
# 4. Use a for loop to iterate through the list.
# 5. Call the area() method on each object inside the loop.
# 6. The program should calculate and display the area of both the circle and rectangle.

c2 = Circle(9)
r2 = Rectangle(4,9)
shapes = [c2, r2]  #>>>or we can do shapes = [Circle(5), Rectangle(4,9)]

for shape in shapes:
    shape.area()