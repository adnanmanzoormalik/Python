# L =[1,2,3]
# print(L.upper()) 

# S = "HELLO"
# S.append('x')

#in python almost everything is an object

#OOPs >>> generality to specificity
#using oop we can make our own data types

#OOPs object, class, polymorphism, encapsulation, inheritance, abstraction

#CLASS class is a blueprint      1. Builtin      2. User defined

L = [1,2,3]
print(type(L)) #Lists, strings, tuple etc etc are classes and when we make a variable of a class lets say L tht is an object

 #class has two things >>> data or attribute or property and functions or behaviour
 #object is an instance of a class

 #syntax to create an object
 #obj_name = classname()

#object literal >>> An object literal is a way to create an object directly in your code by writing its properties and values.
L =[1,2,3]

#actually this happens
L1 = list()

#we use PascalCase for writting class name
class Atm:

    #constructor >>> a function inside the class but it is a special function as it doesnt need to be called 
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""
Hi How can I help you?
1. Press 1 to create pin
2. Press 2 to change pin
3. Press 3 to check balance
4. Press 4 to withdraw
5. Anything else to exit
            """)

        if user_input == '1':
            self.create_pin()
        elif user_input == '2':
            self.change_pin()
            pass
        elif user_input == '3':
            self.check_balance()
            pass
        elif user_input == '4':
            self.withdraw()
            pass
        else:
            exit()

    def create_pin(self):
        user_pin = input("Enter your pin: ")
        self.pin = user_pin

        user_balance = int(input('Enter balance: '))
        self.balance = user_balance

        print("pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter existing pin: ")
        if old_pin == self.pin:
            new_pin = input("Enter new pin: ")
            self.pin = new_pin
            print("Pin changed successfully")
        else:
            print("Old pin is wrong")
        self.menu()

    def check_balance(self):
        old_pin = input("Enter old pin: ")
        if old_pin == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Wrong pin entered")
        self.menu()

    def withdraw(self):
        old_pin = input("Enter your pin: ")
        if old_pin == self.pin:
            amount = int(input("Enter withdrawl amount: "))
            if amount <= self.balance:
                print(f"{amount} withdrawn successfully")
                self.balance -= amount
            else:
                print("You dont have enough balance")
        else:
            print("Your password is incorrect")
        self.menu()
        

obj = Atm()
# print(type(obj))


#we can represent a class using a diagram
# NOTE: learn this



         
 



