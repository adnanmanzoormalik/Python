from functools import wraps
def log(func):
    @wraps(func)
    def wrapper():
        print("Processing...")
        func()
        print("Processing ended\n")
    return wrapper

@log
def login():
    "This is login()"
    print("Logged in")

@log
def logout():
    print("Logged out")

login()
logout()

print(login.__name__)
print(login.__doc__)