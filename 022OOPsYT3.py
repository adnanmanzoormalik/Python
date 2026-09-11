#Encapsulation 

#instance variable: variables whose value is diff for diff objects
class Person:
    def __init__(self,name,country):
        self.name = name
        self.country = country

p1 = Person("adnan","India")
p2 = Person("asrar", "England")


