#Abstraction
#abstract class is a class which has atleast one abstract method (abstract method means which has no code and has a decorator) and inherits from ABC

from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
        print("connected to database")

    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):

    def mobile_login(self):
        print("login into mobile")

    def security(self):
        print("mobile security")

# obj = MobileApp()  #this wont work until we dont make a security method in child class

obj = MobileApp()
obj.security()
obj.database()