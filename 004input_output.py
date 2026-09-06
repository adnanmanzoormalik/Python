#OUTPUT
print(10)
name = "adnan"
print(name)
print("My name is ", name)
print(10, name, "Adnan")

#INPUT
name = input("Enter your name: ")
print(name)

#input always returns a string
age=input("Enter your age: ")
print(type(age))

#so we have to convert the string data into our datatype
age1 = int(input("Age: "))
print(type(age1))

rate = float(input("enter rate: "))
print(type(rate))
print(rate)

#WAYS TO PRINT VARIABLES
name = "adnan"
age = 26
print("My name is",name,"and my age is",age,".")
print(f"My name is {name} and my age is {age}") #fstring
print(f"My age is {age + 1}")#we can do calculations in fstring

#controlling print with "sep" NOTE
print("Adnan", "Malik")
print("Adnan", "Malik", sep="_")
print("Adnan","Malik",sep="-")
print(10,11,2026,sep="/")

#controlling print with "end" NOTE
print("Hello")
print("World")
print("Hello", end=" ")
print("World")

#escape characters
print("Hello\nWorld")
print("Hello\tWorld")
print("Hello \"World\"")