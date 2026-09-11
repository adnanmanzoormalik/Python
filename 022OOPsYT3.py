#Encapsulation

#instance variable: variables whose value is diff for diff objects >>> obj_name.var_name
class Person:
    def __init__(self,name,country):
        self.name = name
        self.country = country

p1 = Person("adnan","India")
p2 = Person("asrar", "England")

class Atm:

    #constructor >>> a function inside the class but it is a special function as it doesnt need to be called 
    def __init__(self):
        self.pin = ''
        self.__balance = 0 #when we create a variable like this __balance  in class actually it doesnt take this name it becomes _Atm__balance
        # self.menu()

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Enter a correct value.")

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
        self.__balance = user_balance

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
            print(f"Your balance is: {self.__balance}")
        else:
            print("Wrong pin entered")
        self.menu()

    def withdraw(self):
        old_pin = input("Enter your pin: ")
        if old_pin == self.pin:
            amount = int(input("Enter withdrawl amount: "))
            if amount <= self.__balance:
                print(f"{amount} withdrawn successfully")
                self.__balance -= amount
            else:
                print("You dont have enough balance")
        else:
            print("Your password is incorrect")
        self.menu()
        

obj = Atm()

obj.__balance = 100000 #this wont make any change to our actual balance of the obj becoz #when we create a variable like this __balance  in class actually it doesnt take this name it becomes _Atm__balance

obj.set_balance(10000)
print(obj.get_balance())

#COLLECTION OF OBJECTS
class Person:

  def __init__(self,name,gender):
    self.name = name
    self.gender = gender

p1 = Person('nitish','male')
p2 = Person('ankit','male')
p3 = Person('ankita','female')

L = [p1,p2,p3]

for i in L:
    print(i) #this will print address of our objs becoz we havent used __str__
    print(i.name) #this will print
    print(i.gender) #this will print



#STATIC VARIABLES >>> class_name.var_name
# it is the variable of the class
# every variable has the same static variable 

class Atm:

    __counter = 1

    def __init__(self):
        self.pin = ''
        self.__balance = 0
        self.cid = Atm.__counter 
        Atm.__counter += 1

    #Utility methods
    @staticmethod #decorator
    def get_counter(self): #this self here is totally optional
        return Atm.__counter
    
    def get_balance(self):
        return self.__balance

    def set_balance(self, new_value):
        if type(new_value) == int:
            self.__balance = new_value
        else:
            print("Enter a correct value.")

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
        self.__balance = user_balance

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
            print(f"Your balance is: {self.__balance}")
        else:
            print("Wrong pin entered")
        self.menu()

    def withdraw(self):
        old_pin = input("Enter your pin: ")
        if old_pin == self.pin:
            amount = int(input("Enter withdrawl amount: "))
            if amount <= self.__balance:
                print(f"{amount} withdrawn successfully")
                self.__balance -= amount
            else:
                print("You dont have enough balance")
        else:
            print("Your password is incorrect")
        self.menu()

Atm.get_counter() #here we use class_name.method and this doesnt need an obj
        
c1 = Atm()
c2 = Atm()
c3 = Atm()

print(c1.cid)
print(c2.cid)
print(c3.cid)

