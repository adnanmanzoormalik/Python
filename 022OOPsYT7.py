#Polymorphism
# Method Overriding
# Method Overloading
# Operator Overloading

class Shape:

    def __init__(self):
        pass

    def area(self, radius):
        return 3.14*radius*radius

    def area(self, l, b):
        return l*b

shape = Shape()
# print(shape.area(10)) #this wont work, in python only the last same_named method is considered
print(shape.area(10, 10))

class Shape:

    def __init__(self):
        pass

    def area(self, a, b=None):
        if b == None:
            return 3.14*a*a
        else:
            return a*b

s = Shape()
print(s.area(12))
print(s.area(12,12))


#operator overloading
print("hello" + "world")
print(1+2)
print([1,2,3]+[4,5,6])