#Inheritance is a mechanism where one class acquires the properties and methods of another class.

class Animal: #parent class or base class or superclass

    def eat(self):
        print("Animal is eating")

class Dog(Animal): #child class or derived class or subclass ........ Dog(Animal) >>> this means Dog inherits from Animal
    pass

dog = Dog()
dog.eat()

#inheritance : IS-A relation like dog is an animal, student is a Person, car is a Vehicle 
#it cant be like car is a engine or engine is a car that is a HAS-A relation 



#in the below example we can see that we have sleeping and eating common in dog and cat thats why we inherit them from Animal class otherwise we have to write it again and again
class Animal:

    def __init__(self, legs):
        self.legs = legs #child can access parent attributes also

    def sleep(self):
        print("Animal is sleeping")

    def eat(self):
        print("Animal is eating")

class Dog(Animal):

    def bark(self):
        print("Dog is barking")

class Cat(Animal):

    def meow(self):
        print("Car is meowing")



d1 = Dog(4)
c1 = Cat(4)

d1.sleep()
d1.eat()
d1.bark()
print(f"dog has {d1.legs} legs")

c1.sleep()
c1.eat()
c1.meow()
print(f"dog has {c1.legs} legs")


print()
print()



#TYPES OF INHERITANCE
# 1. SINGLE
#     A
#     ↓
#     B


# 2. MULTILEVEL
#     A
#     ↓
#     B
#     ↓
#     C

# 3. MULTIPLE

#    A     B
#     \   /
#      \ /
#       C

# 4. HIERARCHICAL

#        A
#       / \
#      B   C

# 5. HYBRID

#        A
#       / \
#      B   C
#       \ /
#        D



#SINGLE INHERITANCE: When one child class inherits from one parent class

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog = Dog()
dog.eat()
dog.bark()

print()




#Multilevel Inheritance: When inheritance occurs in multiple levels
# child -> parent -> grandparent

class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Puppy(Dog): #Now Puppy can access methods from both Dog and Animal.
    def play(self):
        print("Puppy is playing")

pup = Puppy()
pup.eat()
pup.bark()
pup.play()

print()

#Multiple Inheritance: When one child class inherits from multiple parent classes, it is called Multiple Inheritance.

class Father:
    def f_prop(self):
        print("This is father's property")

class Mother:
    def m_prop(self):
        print("This is mother's property")

class Child(Father, Mother):
    def c_prop(self):
        print("This is child's property")

c1 = Child()
c1.c_prop()
c1.f_prop()
c1.m_prop()

#if there is a method with name among child and Father and Mother and if the child calls that method it will call its own method. lets suppose only the Father and the Mother has method of same name only Fathers will be called becoz it is inherited before the Mother like this Child(Father, Mother)


print()


#Hierarchical Inheritance: When multiple child classes inherit from the same parent class
class Animal:
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

cat = Cat()
dog = Dog()

cat.meow()
cat.eat()

dog.bark()
dog.eat()


print()


#Hybrid inheritance: Combination of two or more types of inheritance.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

#above contains hierarchical and multiple inheritance


