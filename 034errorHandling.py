#ERROR HANDLING
#>>>there are two imp types of errors 1. Syntax Error 2. Exceptions
#Syntax error: A Syntax Error happens when Python cannot understand the structure/rules of your code. happens before the code can execute
#print("Hello" or a = 

#Exceptions: An exception happens while Python is executing a syntactically valid program. An exception is an event that interrupts the normal flow of program execution because something unexpected or invalid happened.
# print(10/0) #>>> the syntax is correct but division by zero is not allowed

#age = int(input("Enter age: ") >>> and we enter age as abc it will give value error and may stop unless we handle that exception.

#this is where error handling comes in

try:
    age = int(input("Enter age: "))
    print(age)
except:
    print("Invalid data type")



#ValueError: occurs when a function receives a value of the correct general type, but the value itself is inappropriate.
try:
    age = int(input("Age: "))
    print("Age is ", age)
except ValueError:
    print("Please enter a integer.")


# TypeError: happens when you perform an operation using an inappropriate data type.
try:
    int1 = 10
    str = "str"
    print(int1 + str)
except TypeError:
    print("Invalid data types")


#IndexError: happens when you try to access a list/sequence index that doesn’t exist.
list = [1,2,3]
try:
    print(list[4])
except IndexError:
    print("Index not found")

# KeyError: commonly happens when you try to access a dictionary key that doesn’t exist.
dict1 = {
    "name" : "adnan",
    "age": 19
}
try:
    print(dict1["course"])
except KeyError:
    print("Key not found")

# NameError: occurs when Python encounters a name/variable that hasn’t been defined.
# try:
#     print(adnan)
# except NameError:
#     print("Variable not defined")

#ZeroDivisionError: happens when you try to divide a number by zero.
try:
    print(10/0)
except:
    print("Division by zero not allowed")


# FileNotFoundError: This happens when Python tries to open a file that doesn’t exist.
try:
    open("adnan.txt")
except FileNotFoundError: 
    print("File not found")

# AttributeError: occurs when you try to access an attribute or method that an object doesn’t have.
name = "adnan"
try:
    name.append(" Malik")
except AttributeError:
    print("Append doesnt work on strings")


#multiple except blocks
try:
    amount = int(input("Enter amount: "))
    denom = int(input("Enter denom: "))
    print(amount/denom)

except ValueError:
    print("Enter correct value.")

except ZeroDivisionError:
    print("Cant divide by zero")

#NOTE: Python checks the except blocks from top to bottom and executes the first matching one.



# Catching Multiple Exceptions in One Line
try:
    amount = int(input("Enter amount: "))
    denom = int(input("Enter denom: "))
    print(amount/denom)

except (ValueError, ZeroDivisionError):
    print("Invalid Input")


#"except Exception as e" >>> You can capture the actual exception object using it
try: 
    print(10/0)
except Exception as e: #this is used to handle a boarder range of errors when we dont know what error can come or there are chances of many errors to occur
    print("Something went wrong: ",e)
    print(type(e)) #like this we can also print error type(class)

try:
    print(10+"art")
except Exception as e: 
    print(e)
    print(type(e))


#else block >>> The else block runs only if the try block succeeds without an exception.
#finally block >>> used when you want some code to execute regardless of whether an exception occurred or not.
try:
    num = int(input("Enter a number: "))
except:
    print("Enter a valid number")
else:
    print("Number: ", num)
finally:
    print("Code ran successfully")


#another example
try:
    num = int(input("Enter a number: "))
    result = 100/num
except ValueError:
    print("Enter a valid number.")
except ZeroDivisionError:
    print("Division by zero not allowed")
else:
    print("Result: ",result)
finally:
    print("Code executed")


#raise >>> this helps us raises custom exception messages

age = 10
if age<18:
    raise ValueError("Age cant be less than 18")

try:
    age = int(input("Enter age: "))
    if age<0:
        raise ValueError("Age cant be negative")
    if age<18:
        raise ValueError("Age cant be less than 18")
except ValueError as e:
    print(e)
else:
    print("Age: ", age)


#in raise we used ValueError which is builtin now we will create our own custom exceptions
#A custom exception is simply a class that inherits from Exception.

class InsufficientBalance(Exception):
    """Error class for insufficient balance"""
    pass
balance = 1000
withdraw = 10000

# if withdraw>balance:
#     raise InsufficientBalance("You dont have sufficient balance.")
# print(balance) #this wont be printed becoz there is an exception happening which we need to handle

try:
    if withdraw>balance:
        raise InsufficientBalance("You dont have sufficient balance")
except Exception as e:
    print(e)
else:
    print("remaining balance: ", balance-withdraw)



class InsufficientBalance(Exception):
    def __init__(self, balance, withdraw):
        self.balance = balance
        self.withdraw = withdraw

        super().__init__(
            f"Balance: {balance}, Withdraw: {withdraw}"
        )

withdraw = 100
balance = 50

try:
    if withdraw>balance:
        raise InsufficientBalance(balance, withdraw)
    balance -= withdraw
    print(balance)
except InsufficientBalance as e:
    print("Error: ", e)



class BankError(Exception):
    pass

class InsufficientBalanceError(BankError):
    pass

class InvalidAmountError(BankError):
    pass

amount = -500

try:

    if amount <= 0:
        raise InvalidAmountError("Amount must be greater than zero")

except InvalidAmountError as e:
    print("Error:", e)


#Q1 — Basic Exception Handling -  Create a program that asks the user for two numbers and divides the first number by the second.
# 1. Take two numbers using input().
# 2. Convert them to integers.
# 3. Perform division.
# 4. Handle: * ValueError → "Please enter valid numbers."  * ZeroDivisionError → "Cannot divide by zero."
# 5. If there is no exception, use else to print: Result: <result>
# 6. Use finally to print: Program finished

try:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    result = num1/num2
except ValueError:
    print("Please enter valid numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result: ", result)
finally:
    print("Program finished.")


#Q2 — Validation + raise - Create a program that takes a student’s marks.
# 1. Take marks from the user.
# 2. Convert them to int.
# 3. If marks are: * less than 0, OR * greater than 100 manually raise: ValueError("Marks must be between 0 and 100")
# 4. Catch the error using except ValueError as e.
# 5. Print the error message.
# 6. If the marks are valid, use else and print: Valid marks: <marks>
# 7. Use finally to print: Validation completed.

try:
    marks = int(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")
except ValueError as e:
    print("Error: ", e)
else:
    print("Valid marks: ", marks)
finally:
    print("Validation complete")


## Q3 — Custom Exception + Multiple Exceptions Build a bank withdrawal system.

# 1. Create a custom exception: InsufficientBalanceError It should inherit from Exception.
# 2. Start with: balance = 5000
# 3. Ask the user for a withdrawal amount.
# 4. Handle invalid input:
#       If the user enters something like "abc",
#       handle ValueError and print:
#       "Please enter a valid amount."
# 5. If the withdrawal amount is 0 or negative,
#    raise:
#       ValueError("Withdrawal amount must be greater than 0")
# 6. If withdrawal > balance,
#    raise:
#       InsufficientBalanceError("Insufficient balance.")
# 7. If everything is valid, perform the withdrawal and print:
#       "Withdrawal successful."
#       "Remaining balance: <remaining_balance>"
# 8. Use an else block for the successful transaction.
# 9. Use finally to always print:
#       "Transaction completed."

class InsufficientBalanceError(Exception):
    pass

balance = 5000
try:
    withdraw_amt = int(input("Enter withdraw amount: "))

    if withdraw_amt != int:
        raise ValueError("Please enter a valid amount.")

    if withdraw_amt <= 0:
        raise ValueError("Withdrawl amount must be greater than 0")

    if withdraw_amt>balance:
        raise InsufficientBalanceError("Insufficient balance")

except Exception as e:
    print(e)

else:
    print("Withdrawl successful")
    print("Remaining balance: ", balance-withdraw_amt)

finally:
    print("Transaction complete")






