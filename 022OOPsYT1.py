# #the functions inside a class are called as methods
# L =[1,2,3]
# len(L) #function >>> outside the list class
# L.append("1") #method >>> inside the list class

# #MAGIC MEHTODS or DUNDER METHODS >>> special kind of methods ( __methodname__ )

# #constructor is a special method which doesnt needs to be called. Benefit: used to write code which should always run like configration code as it is always necessary to connect or link etc for which we do not need the user to do anything

# class Temp:
#     def __init__(self):
#         print("HELLO")
# obj = Temp()

# #GOLDEN RULE OF OOPs >>> attributes and methods of a class can be accessed by only objs of the class
# #self >>> [[self and the current obj are the same thing]] if we want a method to called another method or attrubute


# #CREATING OUR OWN DATA TYPE
# class Fraction:
#     def __init__(self, x, y): #parameterized constructor
#          self.numerator = x
#          self.denominator = y

#     def __str__(self):
#         # return '{}/{}'.format(self.numerator,self.denominator)
#         return f"{self.numerator}/{self.denominator}"

#     def __add__(self, other):
#         new_num = self.numerator* other.denominator + self.denominator* other.numerator
#         new_den = self.denominator * other.denominator
#         return f'{new_num}/{new_den}'

#     def __sub__(self, other):
#             new_num = self.numerator* other.denominator - self.denominator* other.numerator
#             new_den = self.denominator * other.denominator
#             return f'{new_num}/{new_den}'

#     def __mul__(self, other):
#          new_num = self.numerator * other.numerator
#          new_den = self.denominator * other.denominator
#          return f'{new_num}/{new_den}'

#     def __truediv__(self, other):
#         new_num = self.numerator * other.denominator
#         new_den = self.denominator * other.numerator
#         return f'{new_num}/{new_den}'

#     def convert_to_decimal(self):
#          return self.numerator/self.denominator




# frac = Fraction(7,2)
# print(frac)
# frac1 = Fraction(4,5)
# print(frac1)

# print(frac1+frac)
# print(frac-frac1)
# print(frac*frac1)
# print(frac/frac1)

# print(frac.convert_to_decimal())


#Write OOP classes to handle the following scenarios: A user can create and view 2D coordinate A user can find out the distance between 2 coordinate A user can find find the distance of a coordinate from origin A user can check if a point lies on a given line A user can find the distance between a given 2D point and a given line

class Point:

     def __init__(self, x, y):
          self.x_cod = x
          self.y_cod = y

     def __str__(self):
          return f"<{self.x_cod},{self.y_cod}>"

     def euclidean_distance(self, other):
          return ((self.x_cod-other.x_cod)**2 + (self.y_cod-other.y_cod)**2)**0.5

     def origin_distance(self):
        #   return ((self.x_cod)**2 + (self.y_cod)**2)**0.5
        return self.euclidean_distance(Point(0,0))

class Line():
     def __init__(self, A, B, C):
          self.A = A
          self.B = B
          self.C = C

     def __str__(self):
          return f"{self.A}x + {self.B}y + {self.C} = 0"

     def point_on_line(line, point):
          if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
               return "Lies on the line"
          else:
               return "Doesnt lie on the line"

     def shortest_distance(line, point):
          return abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**.5
          
     
p1 = Point(0,0)
print(p1)
p2 = Point(1,1)
print(p2)
print(p1.euclidean_distance(p2))
print(p1.origin_distance())
print(p2.origin_distance())

l1 = Line(1,1,4)
print(l1)
print(l1.point_on_line(p2))
print(l1.shortest_distance(p2))

#H/W >>> does two line segments intersect