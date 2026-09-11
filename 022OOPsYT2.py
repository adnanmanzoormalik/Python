class Person:
    def __init__(self):
        self.name = "Adnan"
        self.gender = "Male"

Person() #without a ref var

#Refrence variable Reference variables hold the objects We can create objects without reference variable as well An object can have multiple reference variables Assigning a new reference variable to an existing object does not create a new object
p = Person() # >>>p is not the object p is the refrence variable which contains address of the object created
#so we can do this
q = p #multiple refrences

print(id(p))
print(id(q))

print(p.name)
print(q.name)

q.name = "Asrar"
print(q.name)
print(p.name)

#PASS BY REFRENCE

class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

#function ---- not method
def greet(person):
    print(f'Hi my name is {person.name}, and i am a {person.gender}')
    p2 = Person("asrar", "male")
    return p2 #A function can return an obj

p1 = Person("adnan", "male")

x = greet(p1)
print(x.name, x.gender)


#object mutablitiy
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(person):
    person.name = "Asrar"
    print(person.name)
    print(id(person))

p1 = Person("adnan", "male")
print(id(p1))
greet(p1)
print(id(p1))
print(p1.name)
#objects are mutable like lists, sets etc so when we make a change in an obj the address doesnt change
