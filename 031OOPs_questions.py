#Q1 — Easy: Class + Constructor + Method
# Create a class Student.
# Requirements:
# The class should have a constructor __init__() that takes:
# name
# age
# course
# Store these values as instance attributes.
# Create a method display_info() that prints:
# Name: Adnan
# Age: 22
# Course: B.Tech CSE
# Create two Student objects with different information.
# Call display_info() for both objects.
# Expected concept tested:
# Class → Object → Constructor → self → Instance Attributes → Instance Method
# Don't worry about making it overly complicated. Write it yourself first.

class Student:

    def __init__(self, name, age, course):
        self.__name = name
        self.__age = age
        self.__course = course

    def display_info(self):
        print(f"Name: {self.__name}\nAge: {self.__age}\nCourse: {self.__course}")

s1 = Student("Adnan", 25, "B.Tech CSE")
print() #just to create a space in between
s2 = Student("Asrar", 30, "MBBS")

s1.display_info()
s2.display_info()



# Q2 — Easy: Class Method + Static Method
# Create a class Employee.
# Requirements:
# Create a class variable: company = "TechCorp"
# Create a constructor that takes: name salary
# Create an instance method: display() that prints: Name: Adnan Salary: 50000 Company: TechCorp
# Create a class method: change_company() that changes the company for all employees.
# Create a static method: is_valid_salary(salary) It should return True if salary is greater than or equal to 20,000, otherwise False.
# Create two employees.
# Change the company using the class method.
# Display both employees.
# Test the static method with: 15000 and 25000

class Employee:
    company = "TechCorp"

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def display(self):
        print(f"Name: {self.__name}\nSalary: {self.__salary}\nCompany: {Employee.company}")

    @classmethod
    def change_company(cls, new_company):
        Employee.company = new_company

    @staticmethod
    def is_valid_salary(salary):
        if salary >= 20000:
            print("True")
        else:
            print("False")

emp1 = Employee("Adnan", 50000)
emp2 = Employee("Asrar", 100000)

Employee.change_company("HCL")

emp1.display()
print()
emp2.display()

Employee.is_valid_salary(15000)
Employee.is_valid_salary(25000)

#Create a parent class BankAccount.
# 1. The BankAccount class should have: owner balance
# 3. Create an instance method deposit(amount) - Add the amount to the balance.
# 4. Create an instance method display() - Print the owner's name and current balance.
# 5. Create a child class SavingsAccount that inherits from BankAccount.
# 6. SavingsAccount should have an additional attribute: - interest_rate
# 7. Create a constructor for SavingsAccount that takes: - owner - balance - interest_rate
# 8. Override the display() method in SavingsAccount. It should print: - Owner - Balance - Interest Rate
# 9. Create a method add_interest(). Calculate interest using: interest = balance × interest_rate / 100 Add the calculated interest to the balance.
# 10. Create a SavingsAccount object: account = SavingsAccount("Adnan", 50000, 5)
# 11. Call: account.display() account.deposit(10000) account.add_interest() account.display()

class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print(f"Name of owner: {self.owner}\nBalance: {self.balance}")

class SavingsAccount(BankAccount):

    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def display(self):
        print(f"Name of owner: {self.owner}\nBalance: {self.balance}\nInterest Rate: {self.interest_rate}")

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest

account = SavingsAccount("Adnan", 50000, 5)
account.display()
account.deposit(10000) 
account.add_interest() 
account.display()



# Q4: Create a parent class Employee.
# 1. Add a class variable: company = "TechCorp"
# 2. Create __init__(name, salary).
# 3. Create an instance method display().
# 4. Create a child class Manager that inherits from Employee. Manager should have an additional attribute: department
# 6. Override display() in Manager.
# 7. Create another child class Developer that inherits from Employee. Developer should have an additional attribute: programming_language
# 9. Override display() in Developer.
# 10. Create a list containing - one Manager object - one Developer object and Use a for loop to call display() on every object.
# 12. Create a class method change_company() that changes the company name.
# 13. Change the company to "Google" and display both objects again.

class Employee:

    company = "TechCorp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company 

class Manager(Employee):

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary},Company: {Employee.company}, Department: {self.department}")

class Developer(Employee):

    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.programming_language = lang

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary},Company: {Employee.company} Programming Language: {self.programming_language}")

workers = [Manager("Adnan", 100000, "HR"), Developer("Asrar", 50000, "Python")]

for worker in workers:
    worker.display()

Employee.change_company("MicroSoft")

for worker in workers:
    worker.display()

print()



#Q5: 1. Create an abstract class Employee with: - name - salary
# 2. Create an abstract method calculate_bonus().
# 3. Create a class variable: company = "TechCorp" 
# 4. Create an instance method display() that prints: - Name - Salary - Company
# 5. Create a child class Developer. - Additional attribute: programming_language - Implement calculate_bonus() - Bonus = 10% of salary - Override display()
# 6. Create another child class Manager. - Additional attribute: team_size - Implement calculate_bonus() - Bonus = 20% of salary - Override display()
# 7. Create a class method change_company() - It should change the company name for all employees.
# 8. Create a static method is_valid_salary(salary) - Return True if salary >= 30000 - Otherwise return False.
# 9. Create: - One Developer object - One Manager object and Store both objects in a list.
# 11. Use a for loop to: - Display each employee - Print their calculated bonus.
# 12. Change the company name to "Google" using the class method.
# 13. Display both employees again.
# 14. Test is_valid_salary() with:  25000 and 50000

from abc import ABC, abstractmethod

class Employee(ABC):

    company = "TechCorp"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

    def dispaly(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}")

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    def is_valid_salary(salary):
        return salary >= 30000

class Developer(Employee):
    def __init__(self, name, salary, lang):
        super().__init__(name, salary)
        self.prog_lang = lang

    def calculate_bonus(self):
        bonus = 10/100 * self.salary
        print(f"Bonus: {bonus}")

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}, Programming Language: {self.prog_lang}")

class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def calculate_bonus(self):
        bonus = 20/100 * self.salary
        print(f"Bonus: {bonus}")

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company}, Team Size: {self.team_size}")

dev = Developer("Adnan", 100000, "Python")
mng = Manager("Asrar", 200000, 12)

workers = [dev, mng]

for worker in workers:
    worker.display()
    worker.calculate_bonus()

Employee.change_company("YAMAHA")

for worker in workers:
    worker.display()
    worker.calculate_bonus()

print(Employee.is_valid_salary(25000))
print(Employee.is_valid_salary(50000))