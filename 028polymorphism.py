#POLYMORPHISM: The same method, function, or operator can behave differently depending on the object or data it is working with.

print(len("Adnan"))#prints the number of characters
print(len([10, 20, 30, 40])) #print number of items in the list
#len function behaves differently with different data types

#Why Do We Need Polymorphism? >>> Without polymorphism, we might have to write different code for every type.
# 1. method overriding
# 2. duck typing 
# 3. method overloading
# 4. operator overloading
#polymorphism doesnt always need inheritance like duck typing

#METHOD OVERRIDING
class Parent:
    def detail(self):
        print("This is parent")

class Child:
    def detail(self):
        print("This is child")

c = Child()
c.detail() #this will call child detail() and override parent detail()



#Duck typing: The type or class of an object is less important than the methods and behavior that the object provides.
#Duck typing gets its name from a famous idea called the Duck Test: “If it walks like a duck and quacks like a duck, then it can be treated like a duck.”

class Duck:
    def quack(self):
        print("Quack")

class Person:
    def quack(self):
        print("Imitate Quack")

def make_sound(animal):  
    animal.quack()

duck = Duck()
person = Person()
make_sound(duck)
make_sound(person)
#This is polymorphism as it has a single interface make_sound() but it behaves differently with diff data

#NOTE: Duck typing is different from overriding as overriding requires inheritance

#EAFP — Easier to Ask Forgiveness than Permission



print()
print()



#METHOD OVERLOADING

def add(a,b):
    pass
def add(a,b,c):
    pass
#NOTE: python doesnt support traditional method overloading like above becoz the second add() function will replace the first add() func

#But there a few ways we can achieve method overloading in python
# 1. Default arguments
# 2. Variable length arguments (*agrs)
# 3. conditional logic
# 4. functools.singledispatchmethod (advance topic)

#DEFAULT ARGUMENTS
class Calculator:
    def add(self,a,b,c=0):
        return a+b+c
c1 = Calculator()
print(c1.add(1,2))
print(c1.add(3,4,5))


class Student:
    def introduce(self, name, age=None):
        if age is None:
            print(f"My name is {name}")
        else:
            print(f"My name is {name} and I am {age} years old.")
student = Student()
student.introduce("Adnan")

#VARIABLE LENGTH ARGUMENTS
class Sum:
    def add(self, *args):
        return sum(args)
s = Sum()
print(s.add(1,2,3))
print(s.add(3,4,7,1,2,6,7))

#NOTE: we use default args when we know how many number args we can get known number of possible args like 2 or 3 or 4 etc and use *args when we have no idea how many args we will be recieving 1 or 1000 etc



#CONDITIONAL OVERLOADING    >>> overloading based on type
class DataType:
    def process(self, value):
        if isinstance(value, int):
            print("This is Integer")
        elif isinstance(value, str):
            print("This is a string")
        else:
            print("Data Type unknown")

dt = DataType()
dt.process(10)
dt.process("Adnan")
dt.process(3.22)



# singledispatchmethod 
pass
            


print()
print()

#OPERATOR OVERLOADING: allows an operator to behave differently for different types of objects.
print(1+2)
print("Adnan"+"Manzoor")
#here we can see that the same operator behaves differenly with diff data, this is operator overloading

#why do we need operator overloading >>> lets suppose we make our own class Student and we try to do stu1+stu2 python doesnt know what to add marks, name, age etc etc So we can define what + means for our class. this is operator overloading

class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self,other): #without this method python wont be able to understand what to do with n1(obj) + n2(obj)
        return self.num + other.num


n1 = Number(1)
n2 = Number(2)
print(n1+n2) #this is same as print(n1.__add__(n2))



#points example (a,b)

class Point:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Point(self.a + other.a, self.b + other.b) #this will return a Point obj so it can access Point methods as well

    def __str__(self):
        return f"({self.a}, {self.b})" #with this methods help we can print a point

p1 = Point(1,2)
p2 = Point(3,4)
print(p1+p2)
#operator overloading can return an object

#operator overloading isnt limited to __add__ we can do __mul__, __sub__ etc etc
#operator overloading is polymorphism as a single operator can behave differently with different data






